"""Check one agent result file against its input batch and the syllabus.

Usage: python scripts/validate.py output/<agent>/batch_001.result.json
Prints OK and exits 0, or lists every error and exits 1.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = {"question_id", "topic_id", "paper", "cognitive_intent", "confidence", "rationale"}
INTENTS = {"knowledge", "clinical_application"}


def load_topics():
    text = (ROOT / "rules" / "syllabus.md").read_text(encoding="utf-8")
    return dict(re.findall(r"^\| (\d+(?:\.\d+)+) \| ([AB]) \|", text, re.M))


def validate(result_path, topics):
    result_path = Path(result_path)
    input_path = ROOT / "input" / result_path.name.replace(".result.json", ".json")
    if not result_path.exists():
        return [f"result file not found: {result_path}"]
    if not input_path.exists():
        return [f"no matching input file {input_path}"]
    try:
        results = json.loads(result_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"invalid JSON: {e}"]
    if not isinstance(results, list):
        return ["top level must be a JSON array"]

    input_ids = [q["question_id"] for q in json.loads(input_path.read_text(encoding="utf-8"))]
    errors = []
    seen = []
    for i, r in enumerate(results):
        where = f"[{i}] {r.get('question_id', '?') if isinstance(r, dict) else '?'}"
        if not isinstance(r, dict):
            errors.append(f"{where}: not an object")
            continue
        if set(r) != FIELDS:
            errors.append(f"{where}: fields must be exactly {sorted(FIELDS)}, got {sorted(r)}")
        seen.append(r.get("question_id"))
        tid = r.get("topic_id")
        if tid not in topics:
            errors.append(f"{where}: unknown topic_id {tid!r}")
        elif r.get("paper") != topics[tid]:
            errors.append(f"{where}: paper {r.get('paper')!r} but {tid} is Paper {topics[tid]}")
        if r.get("cognitive_intent") not in INTENTS:
            errors.append(f"{where}: cognitive_intent must be one of {sorted(INTENTS)}")
        c = r.get("confidence")
        if isinstance(c, bool) or not isinstance(c, (int, float)) or not 0 <= c <= 1:
            errors.append(f"{where}: confidence must be a number 0-1")
        if not isinstance(r.get("rationale"), str) or not r.get("rationale", "").strip():
            errors.append(f"{where}: rationale must be a non-empty string")

    missing = [q for q in input_ids if q not in seen]
    extra = [q for q in seen if q not in input_ids]
    dupes = sorted({q for q in seen if seen.count(q) > 1})
    if missing:
        errors.append(f"missing {len(missing)} question(s): {missing}")
    if extra:
        errors.append(f"question_id not in input: {extra}")
    if dupes:
        errors.append(f"duplicate question_id: {dupes}")
    if not missing and not extra and not dupes and seen != input_ids:
        errors.append("results are not in input order")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    errs = validate(sys.argv[1], load_topics())
    for e in errs:
        print(e)
    print("OK" if not errs else f"{len(errs)} error(s)")
    sys.exit(1 if errs else 0)
