"""Split one JSON array of questions into input/batch_NNN.json files.

Usage: python scripts/split.py all_questions.json [--size 40]
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("file")
ap.add_argument("--size", type=int, default=40)
args = ap.parse_args()

questions = json.loads(Path(args.file).read_text(encoding="utf-8"))
ids = [q.get("question_id") for q in questions]
missing = [i for i, qid in enumerate(ids) if not qid]
if missing:
    raise SystemExit(f"items without question_id at positions: {missing[:10]}")
dupes = {qid for qid in ids if ids.count(qid) > 1}
if dupes:
    raise SystemExit(f"duplicate question_id: {sorted(dupes)[:10]}")

out = ROOT / "input"
out.mkdir(exist_ok=True)
for n, start in enumerate(range(0, len(questions), args.size), 1):
    path = out / f"batch_{n:03}.json"
    path.write_text(json.dumps(questions[start:start + args.size], indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {n} batches of up to {args.size} to {out}")
