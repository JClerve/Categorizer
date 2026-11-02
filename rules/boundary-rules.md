# Boundary rules

Many questions touch several sections. Classify by **what the question tests** (what you need
to know to pick the right answer), not by the words that appear in the stem. A vignette about
a patient with schizophrenia that asks for the receptor a drug blocks is a pharmacology question.

Apply the first rule that fits. If two rules fit equally, pick one, set confidence < 0.7 and
name both candidate IDs in the rationale.

DRAFT — to be refined by SME review of disagreements.

## Paper A vs Paper B (the most important split)

| The question tests… | Goes to | Not to |
|---|---|---|
| Receptor action, mechanism, transporter, enzyme, binding, adverse-effect mechanism | 3.3 | disorder section |
| Half-life, CYP450, kinetics, interactions via metabolism, TDM levels (lithium, clozapine) | 3.2 | 3.4 |
| General prescribing principles: dose ranges, switching, treatment resistance definitions, special populations as a general rule | 3.4 | disorder section |
| Choosing / managing treatment for a specific disorder in a specific patient group | disorder section (6.1.x, 7.5.x, 9.7.x, 10.x, 12.4) | 3.4 |
| Neurobiology / pathophysiology of a disorder | 2.11 (or 2.13 for dementias) | 6.1.x / 7.5.x |
| Prevalence, risk factors, presentation, course, outcome of a disorder | disorder section | 2.11 |
| Defining or recognising a psychopathological phenomenon (e.g. "what is this symptom called?") | 4.1 | disorder section |
| ICD / DSM criteria, classification structure | 4.2 | disorder section |
| Psychological theory (learning, memory, attachment theory, social psychology) | 1.x | 8.x |
| Delivering / choosing a psychological therapy | 8.x (7.8 for older people) | 1.x |

## Age and setting override

When the question is clinical (Paper B), the patient group picks the section:
- Aged 65+ / older adult framing → 7.x (dementias → 7.5.1–7.5.4; delirium → 7.5.5).
- Under 18 → 9.x.
- Intellectual disability is central → 12.x.
- Offending, court, prison, secure unit, fitness to plead → 11.x.
- Pregnancy, postpartum, breastfeeding, menstrual cycle, menopause → 6.2.
- Patient on a medical/surgical ward, physical illness, end of life → 6.3.
- Substance or gambling problem as the main issue → 10.x (under-18 → 9.7.9, older → 7.5.9).

## Specific tie-breakers

- Drug in pregnancy: teratogenic risk of a drug as a fact → 3.3; managing a pregnant/postnatal patient → 6.2.
- ECT: neurochemical effects → 3.3; neurobiology → 2.12; indications, risks, practical aspects → 5.3.
- rTMS / DBS / VNS: technique physiology → 2.3; indications and practice → 5.3.
- Delirium: phenomenology of consciousness → 4.1; neurobiology → 2.11; older patient → 7.5.5; younger medical inpatient → 6.3.
- Medically unexplained symptoms / FND: neurobiology → 2.11; disorder → 6.1.8; liaison management → 6.3; psychological approach → 8.7.
- Attachment: theory → 1.12; neurobiology → 2.10; attachment disorder in a child → 9.7.7; perinatal bonding → 6.2.
- Sleep: psychology of sleep → 1.2; neural circuits → 2.7; older adults → 7.10.
- Substances: neurochemistry → 2.5; neurobiology of addiction → 2.11; drug mechanism → 3.3; clinical management → 10.x.
- Capacity, consent, confidentiality, human rights → 5.6. Financial abuse, driving, vulnerable adults → 5.7.
- Mental Health Act use in an acute crisis → 6.4; general legal principles → 5.6; forensic sections → 11.2.
- Risk assessment: general principles and safety plans → 4.3; acute self-harm/suicide → 6.4 (9.9 for under-18, 7.6 for older); structured violence tools (HCR-20, PCL-R) → 11.3.
- Rating scales: which scale for what → 4.3; reliability/validity statistics → 13.5.
- Drug trial phases and licensing → 3.1; trial design, randomisation, NNT, appraisal → 13.3.
- Defence mechanisms, transference: psychodynamic theory or therapy → 8.1; using them to interpret an assessment → 4.3. Low confidence if unclear.
- Any calculation (NNT, sensitivity, odds ratio, SMR) → section 13 matching the study type.
- Genetics of a syndrome causing intellectual disability: genetic mechanism → 2.9; clinical features/behavioural phenotype → 12.3 / 12.4.

## cognitive_intent

- `knowledge`: recall of a fact, definition, mechanism, theory, statistic or calculation.
- `clinical_application`: a patient scenario where the answer is a diagnosis, next step,
  management choice or risk decision.

A vignette that only dresses up a fact recall (e.g. "a patient on lithium… which enzyme…") is `knowledge`.
