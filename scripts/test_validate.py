"""Self-check for validate.py. Run: python scripts/test_validate.py"""
import json
import tempfile
from pathlib import Path

from validate import ROOT, load_topics, validate

topics = load_topics()
assert len(topics) > 100 and topics["3.3"] == "A" and topics["13.5"] == "B" and "6.1" not in topics

inp = ROOT / "input" / "_selftest.json"
inp.write_text(json.dumps([{"question_id": "q1"}, {"question_id": "q2"}]))
good = {"question_id": "q1", "topic_id": "3.3", "paper": "A", "cognitive_intent": "knowledge",
        "confidence": 0.9, "rationale": "Receptor action."}


def check(rows):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "_selftest.result.json"
        p.write_text(json.dumps(rows))
        return validate(p, topics)


try:
    assert check([good, {**good, "question_id": "q2"}]) == []
    errs = check([{**good, "paper": "B"}, {**good, "question_id": "q3", "topic_id": "6.1", "confidence": 2}])
    joined = "\n".join(errs)
    for expected in ("paper 'B' but 3.3", "unknown topic_id '6.1'", "confidence", "missing 1", "not in input"):
        assert expected in joined, (expected, errs)
    assert "input order" in "\n".join(check([{**good, "question_id": "q2"}, good]))
    print("OK")
finally:
    inp.unlink()
