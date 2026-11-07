# Guide mode and writing modes (from the Kimi humanizer)

Read this when the user wants a formal/casual/technical mode, or wants a humanizer guide, reference document, or DOCX/PDF built from these patterns. File paths below are siblings in `references/`.


# Humanizer: Remove AI Writing Patterns

Transform AI-generated or robotic-sounding text into natural, human prose by identifying specific AI tells and rewriting them while preserving meaning.

## Reference Source

- **Type**: Instruction-only / SOP-based
- **Based on**: Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup)
- **Language**: English-optimized (patterns translate to other languages with adaptation)
- **Output**: Plain text, markdown, or any document format the user requests

## Workflow

When given text to humanize:

1. **Analyze** — Scan for AI patterns (see `ai_patterns.md`)
2. **Plan rewrites** — Identify sections needing change; prioritize worst offenders
3. **Rewrite** — Replace AI-isms with natural alternatives
4. **Preserve voice**: retain supplied personality, stance, and rhythm (see `voice_guide.md`); invent none.
5. **Verify** — Read aloud mentally; check for remaining robotic phrasing

## Core Principles

### Preserve Meaning
Never change facts, data, quotes, or core arguments. Only change how ideas are expressed.

### Match Intended Tone
Adapt to the user's requested tone: formal, casual, technical, persuasive, or humorous.

### Add Soul, Not Just Remove Patterns
Use only traits appropriate to the brief; formal neutrality is valid. Good writing can preserve:
- Varied sentence rhythm (short punchy sentences mixed with longer flowing ones)
- Opinions or reactions when appropriate
- Specific details over vague generalizations
- Intentional tangents, asides, and conversational transitions, without manufactured errors

## Modes

| Mode | Use When |
|------|----------|
| **Neutral** (default) | General-purpose; natural but adaptable to any context |
| **Casual** | Blogs, social media, emails, personal writing |
| **Formal** | Academic papers, business reports, professional documents |
| **Technical** | Documentation, specs, developer content |

To set mode: specify in your request, e.g., "Humanize this in casual mode" or "Make this sound more formal."

## Quick Pattern Reference

Contextual patterns to review, not words or constructions to remove automatically:

**Overused AI vocabulary:** delve, tapestry, landscape, showcase, revolutionize, foster, leverage, utilize, furthermore, additionally, crucial, pivotal, underscore, testament, vibrant, intricate, bolster, garner

**Significance inflation:** "marking a pivotal moment," "a testament to," "reflects broader trends," "contributing to the evolving landscape"

**Superficial -ing analyses:** "highlighting the importance of," "symbolizing the community's deep connection," "ensuring long-term sustainability"

**Promotional puffery:** "nestled within," "breathtaking region," "rich cultural heritage," "stunning natural beauty," "vibrant town"

**Vague attributions:** "Critics argue," "Some say," "Many believe," "Experts note" (without naming who)

**Negative parallelisms:** "Not just X, but Y," "It's not X, it's Y," "No X. No Y. Just Z."

**Em dash overuse** (in pre-2026 AI output): Sentences crammed with clauses separated by em dashes

**Rule of three:** Triplets like "No family. No calls. Just silence." or "innovation, creativity, and collaboration"

**Chatbot artifacts:** "It's important to note," "In today's world," "As an AI language model," "I hope this helps"

## Completeness Requirements

Only when explicitly asked for a full, unabridged guide, include the following original catalog and examples with their limitations. Ordinary edits, short guides, and scoped excerpts do not require the full catalog. Label legacy examples that assume extra evidence; do not present their unsupported additions as acceptable edits.

### Required: Full Pattern Catalog
Include EVERY pattern from `ai_patterns.md` across all five categories:
1. **Content Patterns** — all 7 patterns (Significance Inflation, Canned Notability, Superficial -ing Analyses, Promotional Language, Vague Connection/Association, Vague Attributions, Outline-like Conclusions)
2. **Language and Grammar** — all 4 patterns (AI Vocabulary, Avoidance of Copulatives, Negative Parallelisms, Excessive Conjunctive Phrases)
3. **Style and Structure** — all 4 patterns (Rule of Three, Em Dash Overuse, Uniform Sentence Length, Overuse of Boldface)
4. **Communication Artifacts** — all 3 patterns (Hedging Disclaimers, Chatbot Artifacts, Canned User Page Format)
5. **Historical Indicators** — both patterns (Section Summaries, Prompt Refusal Artifacts)

**CRITICAL:** Every pattern that has a Before/After example pair in the reference MUST include BOTH the Before and After example in the output. Do not show only the Before example.

### Required: Full Voice and Soul Section
Include ALL seven voice techniques from `voice_guide.md`:
1. Have Opinions
2. Vary Your Rhythm
3. Acknowledge Complexity
4. Use "I" When It Fits
5. Let Some Mess In
6. Be Specific About Feelings
7. Use Conversational Transitions

Include ALL supporting tables:
- Conversational transitions table (Instead of / Try)
- Tone calibration by context table (Casual / Formal / Technical / Persuasive)
- **What to Preserve vs. What to Change** comparison table

### Required: Full Before/After Examples
Include ALL example categories from `before_after_examples.md`:
- Significance Inflation (4 examples)
- AI Vocabulary Overuse (4 examples)
- Promotional Language (3 examples)
- Superficial -ing Analyses (3 examples)
- Vague Attributions (3 examples)
- Negative Parallelisms (3 examples)
- Hedging and Disclaimers (3 examples)
- Em Dash Overuse (2 examples)
- Rule of Three (3 examples)
- Chatbot Artifacts (3 examples)
- Full Paragraph Rewrites — ALL four contexts (Academic, Marketing, Technical Documentation, Personal Essay)
- Adding Soul Examples — ALL three examples

### Required: Core Elements
- Modes table (Neutral, Casual, Formal, Technical)
- Quick Reference Checklist (all 10 items)
- Summary Checklist from ai_patterns.md (all 10 items)

## Detailed Guidance

For the full pattern catalog with before/after examples, read `ai_patterns.md`.

For voice injection and soul-adding techniques, read `voice_guide.md`.

For an extensive collection of before/after rewrite examples, read `before_after_examples.md`.

## Document Generation Notes

When generating a DOCX, PDF, or other formatted document from this skill:
- Ensure the Table of Contents uses proper page number fields, not placeholder text
- Include a cover page with title, subtitle, and source attribution
- Use consistent heading hierarchy: H1 for main sections, H2 for subsections, H3 for individual patterns
- Format Before/After examples as distinct blocks for visual clarity
- Include page numbers and running headers

## Important Caveats

- **These are signs, not proof.** A pattern's presence doesn't guarantee AI authorship; humans use these constructions too. Use patterns as editing guidance, not detection evidence.
- **Not all formal writing is AI.** Academic, legal, and technical prose naturally uses complex vocabulary and structured arguments. Don't flatten legitimate sophistication.
- **Avoid creating new problems.** Don't introduce errors, informalities, or opinion where inappropriate (e.g., encyclopedic text, legal documents).
- **Read the result aloud.** If it sounds stilted, it needs more work.
