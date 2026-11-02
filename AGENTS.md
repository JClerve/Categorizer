# Task

Classify each MRCPsych theory question in `input/` into one syllabus topic and paper.
You are a classifier only: do not answer, rewrite or judge the questions.

# Before you start

Read all of these, in full:
1. `rules/syllabus.md` — the only valid `topic_id`s and their paper.
2. `rules/boundary-rules.md` — how to decide between overlapping topics.
3. `rules/examples.md` — worked examples.

Your run prompt tells you your agent name (`claude` or `codex`). Write only to
`output/<agent>/`. Never edit `rules/`, `input/`, `scripts/`, or another agent's output.

# Process

1. Take ONE file from `input/` at a time, in name order. Skip it if
   `output/<agent>/<same name without .json>.result.json` already exists and validates.
2. Classify EVERY question in the file, in the same order. Never skip, merge or summarise.
3. For each question decide what it tests (see boundary rules), pick the most specific
   `topic_id` from `syllabus.md`, and copy its `paper` from the same row.
4. `cognitive_intent`: `knowledge` for recall of a fact, mechanism, theory or calculation;
   `clinical_application` for a patient vignette asking diagnosis, next step or management.
5. `confidence` from 0 to 1. Below 0.7 when unsure; then name the other candidate
   `topic_id` in the rationale. Do not guess silently.
6. Write `output/<agent>/<batch>.result.json`, e.g. `input/batch_001.json` →
   `output/<agent>/batch_001.result.json`.
7. Run `python scripts/validate.py output/<agent>/<batch>.result.json`.
   If it reports errors, fix the file and run it again. Move on only when it prints `OK`.
8. Repeat for the next file. At the end, report how many files and questions you classified.

# Output schema

A JSON array, one object per input question, in input order:

```json
[
  {
    "question_id": "q_0001",
    "topic_id": "3.3",
    "paper": "A",
    "cognitive_intent": "knowledge",
    "confidence": 0.9,
    "rationale": "Asks which receptor haloperidol blocks: pharmacodynamics."
  }
]
```

- `question_id`: copied exactly from input.
- `topic_id`: a string, exactly as in the first column of `syllabus.md`.
- `paper`: `"A"` or `"B"`, must match the topic's row.
- `cognitive_intent`: `"knowledge"` or `"clinical_application"`.
- `confidence`: number 0–1.
- `rationale`: one short sentence.

No other fields, no comments, no trailing text.

# Running (for humans)

```
python scripts/split.py all_questions.json          # -> input/batch_001.json ...
claude -p "You are agent 'claude'. Follow AGENTS.md for every file in input/."
codex exec "You are agent 'codex'. Follow AGENTS.md for every file in input/."
python scripts/compare.py                            # -> review/disagreements.csv, review/spot_check.csv
```

If you re-split with different questions, empty `output/claude/` and `output/codex/` first:
agents skip batches that already have a valid result.
