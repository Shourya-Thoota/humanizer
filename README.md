# Humanizer

An agent skill for natural, specific prose: drafting, minimum-edit cleanup, detect-only reviews, and matching your own voice. It removes the tells of generated writing without touching your meaning, claims, numbers, or citations.

**By [Vibhav Thoota](https://github.com/Shourya-Thoota) / [Pansophy LLC](https://github.com/Shourya-Thoota).**

## What it does

- **Drafting and editing.** One grounded draft or the minimum effective edit — no editing preamble, no change summary, no unrequested rewrite. Drafts are built from the actual point, not a generic intro/body/conclusion template.
- **Slop cleanup.** A pattern index of concrete AI-writing tells (mechanical emphasis, filler phrases, formulaic structure, hollow specificity) with matching remedies, applied only where they actually appear.
- **Detect-only reviews.** Quote each relevant passage, name the concrete problem, give a short remedy, and stop — no rewriting, no authorship judgment.
- **Voice matching.** Calibrate to an approved Voice Card so output matches how you actually write, not a generic "human" persona.
- **Preservation guarantees.** Meaning, claims, actors, dates, numbers and units, negation, scope, causal strength, citations, code, and intentional voice are preserved. It never invents facts, anecdotes, or fake imperfections to "sound human," and never strips caveats or inconvenient facts.

## What it is not

Not an AI-authorship detector, not detector evasion, not a rewriting engine for exact quotations, and not for code transformation. It deliberately emits no AI score and no "human" label.

## What's inside

```
SKILL.md                     # Editing contract and workflow
scripts/writing_audit.py     # Mechanical review of long drafts (findings are candidates, never a score)
tests/                       # Python tests for the audit script
references/pattern-index.md  # AI-writing patterns, with remedies
references/writing-indicators.md  # Comprehensive audit checklist
references/voice-*.md        # Voice Card calibration and matching
references/                  # Registers, examples, evidence, editing rules, quality gates
```

## Install

This is an [Agent Skill](https://agentskills.io) (a `SKILL.md` package). Clone it into your agent's skills directory:

```bash
git clone https://github.com/Shourya-Thoota/humanizer ~/.claude/skills/humanizer
```

Works with any agent that supports the Agent Skills format (Claude Code, Perplexity Computer, and others). The optional audit script needs Python 3 only.

## License

[MIT](LICENSE) — Copyright (c) 2026 Pansophy LLC.
