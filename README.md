# NACLO Practice Problem Generator

A simple tool that generates NACLO‑style linguistics practice problems so students can study more than just official problems.

## What it does

- Generates *new* practice problems (not copied from official NACLO files).
- Focuses on patterns like:
  - Past‑tense morphology (e.g., `walk` → `walked`)
  - Plural forms
  - Simple phonology rules (e.g., vowel harmony)
- Outputs JSON‑style problems that can be used later on a website or in notebooks.

## Quick start

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/naclo-practice-problem-generator
   cd naclo-practice-problem-generator
   ```

2. Install dependencies:

   ```bash
   pip install nltk spacy
   python -m spacy download en_core_web_sm
   ```

3. Run the example (generates a sample past‑tense problem):

   ```bash
   python generator/rule_engine.py
   python generator/problem_generator.py
   ```

   You’ll see a JSON‑style problem printed and saved to `examples/past_tense_t001.json`.

## Folder structure

- `generator/` – main logic (rules, problem generator).
- `rules/` – rule types (morphology, phonology, etc.).
- `examples/` – sample generated problems.
- `utils/` – helper tools (parsers, IO, tests).

## How to contribute

- Add a new rule type (e.g., `rules/morphology/plural.py`).
- Improve the rule engine or add more test cases.
- Help design templates for clean problem output (JSON, LaTeX, or HTML).

---

Built by Kishan Patel for NACLO practice.
