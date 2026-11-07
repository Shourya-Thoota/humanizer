# Local mechanical review

Run `scripts/writing_audit.py` for long English plain-text or Markdown drafts when a mechanical sweep helps. Skip it for tiny replies, non-English text, rich office formats, or an exact-output task where it adds no value. It uses Python's standard library, reads local files, makes no network requests, and never rewrites input.

From this skill directory:

```bash
python3 scripts/writing_audit.py /path/to/draft.md
python3 scripts/writing_audit.py /path/to/revised.md --original /path/to/original.md --require-exact "Friday at noon"
```

Interpret `review_candidates` as passages to inspect, not detected errors. Check context and surrounding citations before editing. Interpret `preservation_changes` as changes in token inventories, not a semantic verdict. An intentional correction can appear; a changed assignment, causal claim, scope, spelling of a number, or subtle voice shift can be missed.

Common Markdown fenced/indented/inline code, blockquotes, straight-double and curly quotation spans, and URLs are masked from phrase review. Recognition is incomplete: nested markup, straight single quotes, multiline prose quotations, HTML, escaped delimiters, and unusual fences need manual checking. Protected spans are not modified. URL punctuation can be included in a token, so inspect apparent changes before acting.

The comparison checks recognized code, quotations, URLs, numeric tokens, a small list of logical-force words, and optional exact fragments. It does not reliably understand dates, units, formulas, citations, names, English paraphrases, or truth. It deliberately emits no AI score or “human” label; an empty report is not approval.

## Regression tests

After changing the script, run the bundled tests:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_writing_audit.py' -v
```

`scripts/test_writing_audit.py` checks 20 deterministic cases: candidate detection, non-authorship labeling, valid formal prose and punctuation, code/quote/URL masking, line numbers, preservation differences, exact fragments, identical inputs, and duplicate paragraphs. Passing these does not demonstrate model writing quality, authorship accuracy, or human-reader preference.

## Routing test cases

Use these when changing the skill description. The expected routes are acceptance criteria, not claims of live model tests.

- “Write a concise email asking for my report by Friday.” Expected: humanizer's drafting contract, appropriate register, no full audit or voice onboarding.
- “This paragraph sounds generic. Rewrite it without changing the facts.” Expected: humanizer edit, relevant pattern reference, one final text.
- “Calculate the time complexity of this function and return only JSON.” Expected: technical analysis/exact-format rules; no prose rewrite of code or JSON and no humanizer ceremony.
- “Tell me whether a human or AI wrote this.” Expected: explain the limit; offer concrete editorial observations, never an authorship probability.
