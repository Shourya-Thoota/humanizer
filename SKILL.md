---
name: humanizer
description: "Write, edit, and review natural, specific prose for answers, emails, messages, reports, and creative drafts. Includes minimum-edit slop cleanup, detect-only reviews, and matching the user's voice with an approved Voice Card. Not AI-authorship detection, detector evasion, exact quotation, or code transformation."
allowed-tools: Read Write Edit Grep Glob AskUserQuestion Bash
metadata:
  version: 4.0.0
---
# Humanizer

The single writing skill: drafting, editing, slop cleanup, detect-only review, and voice matching. Former no-ai-slop and match-my-writing-style guidance is built in; do not load or reinstall them. Use the lightweight contract for ordinary answers and drafts without requiring the user to say “humanize.” Read detailed references only when needed. This hub and `references/writing-quality-gate.md` govern when older examples disagree.

## Editing contract

Default to one final answer or draft, or edited text only for an edit. No editing preamble, internal audit, change summary, or extra rewrite unless requested. Follow the user's format and higher-priority instructions. For detect-only, quote each relevant passage, name the concrete problem, give a short remedy, and stop without rewriting or judging authorship.

Preserve meaning, claims, actors, dates, numbers/units, negation, modality, scope, causal strength, citations/destinations, code, direct quotations, technical terms, dialect, and intentional voice. Keep working humor, bluntness, uncertainty, fragments, politeness, and formal writing. Contextual patterns are not word bans; do not impose casual American English, dramatic fragments, or artificial variation.

Never invent facts, anecdotes, experiences, opinions, feelings, sources, or fake imperfections to sound human. Do not remove substantive caveats, safety qualifications, or inconvenient facts. Never strengthen correlation into causation, possibility into certainty, or an estimate into a fact. Do not repair citations by guessing. Human-sounding is a quality goal, not a claim of being human or a guarantee of reader/detector judgment.

## Workflow

1. Identify purpose, reader, genre, mode, point, and evidence. For editing read the whole draft first. Use provided facts; clarify only material missing information.
2. For a substantial draft/edit read `references/writing-quality-gate.md` and relevant `references/registers-and-examples.md` sections. Draft from the actual point, not a generic intro/body/conclusion template.
3. For a specific problem use `references/pattern-index.md` and only its matching sections; read `references/writing-indicators.md` for a comprehensive audit or its relevant category. Read `references/editing-rules.md` for cuts/structure.
4. For writing in the user's voice, Voice Card work, or the original no-ai-slop rubric, read `references/linked-workflow.md`. Reuse approved voice context; no automatic private-source scans. Otherwise preserve the draft's author, not the user's unrelated persona.
5. Make the minimum effective edit or complete one grounded draft. Repair vague reasoning with supported substance, not synonym cycling. For audit mode return findings and stop.
6. Run the preservation/quality gate and `references/edit-checklist.md` internally. For long Markdown/text drafts, run `scripts/writing_audit.py` as described in `references/writing-tools.md` when mechanical review helps. Its findings are review candidates, never an AI score.
7. Fix failures, compare with the original/brief, and return only the requested output. Do not claim reader testing, fact-checking, or voice fidelity that was not verified.

For evidence and changing claims read `references/writing-evidence.md`; `references/reference-map.md` routes legacy tone guides, examples, and document modes.
