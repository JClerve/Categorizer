"""Compare claude vs codex results and write SME review files.

Usage: python scripts/compare.py
Writes review/disagreements.csv (topic_id differs) and review/spot_check.csv
(random 10% of agreed items). Only batches where both agents have a result are compared.
"""
import csv
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A, B = "claude", "codex"
COLS = ["topic_id", "paper", "cognitive_intent", "confidence", "rationale"]


def load(path):
    return {r["question_id"]: r for r in json.loads(path.read_text(encoding="utf-8"))}


def stem(q):
    for key in ("stem", "question", "text"):
        if q.get(key):
            return q[key]
    return json.dumps(q, ensure_ascii=False)


disagree, agree, skipped = [], [], []
for a_path in sorted((ROOT / "output" / A).glob("*.result.json")):
    b_path = ROOT / "output" / B / a_path.name
    if not b_path.exists():
        skipped.append(a_path.name)
        continue
    batch = a_path.name.replace(".result.json", "")
    questions = json.loads((ROOT / "input" / f"{batch}.json").read_text(encoding="utf-8"))
    ra, rb = load(a_path), load(b_path)
    for q in questions:
        qid = q["question_id"]
        x, y = ra.get(qid), rb.get(qid)
        if not x or not y:
            skipped.append(f"{batch}:{qid}")
            continue
        row = {"batch": batch, "question_id": qid, "question": stem(q)}
        for c in COLS:
            row[f"{A}_{c}"], row[f"{B}_{c}"] = x[c], y[c]
        (agree if x["topic_id"] == y["topic_id"] else disagree).append(row)

fields = ["batch", "question_id", "question"] + [f"{s}_{c}" for c in COLS for s in (A, B)]
review = ROOT / "review"
review.mkdir(exist_ok=True)
sample = random.Random(42).sample(agree, k=max(1, len(agree) // 10)) if agree else []
for name, rows in (("disagreements.csv", disagree), ("spot_check.csv", sample)):
    # utf-8-sig so Excel opens it with the right encoding
    with open(review / name, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields + ["sme_topic_id", "sme_note"])
        w.writeheader()
        w.writerows(rows)

total = len(agree) + len(disagree)
print(f"compared {total} questions: {len(agree)} agree, {len(disagree)} disagree"
      + (f" ({len(agree) / total:.1%} agreement)" if total else ""))
print(f"spot_check: {len(sample)} rows")
if skipped:
    print(f"skipped (missing in one agent): {skipped}")
