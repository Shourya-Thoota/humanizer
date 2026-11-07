# Voice matching and slop-rubric modes

Read for user-voice drafting, Voice Card creation or refresh, or the original no-ai-slop rubric. Humanizer is the only writing skill; these modes run inside the same pass. User instructions and protected meaning outrank reference preferences, and the hub controls output modes.

## Voice matching (formerly match-my-writing-style)

Use only when writing in the user's voice is appropriate: a reply the user will send, or an explicit "sound like me" request. Do not impose the user's voice on someone else's draft, quotations, a requested different persona, or neutral audit findings.

1. Check provided context and any known approved Voice Card first; reuse it without rescanning. For user-authored drafts, prefer their actual voice over a generic professionalism filter. An explicit persona, audience, legal requirement, or requested tone overrides the profile.
2. Identify channel and audience. Ask only if the distinction materially changes the draft. Match the relevant register, not quirks from an unrelated channel.
3. With no profile, use supplied samples and the draft's own cadence, vocabulary, punctuation, English variety, and channel; `voice-calibration.md` covers local sample analysis. For a simple task draft provisionally; do not block on onboarding or invent personal habits.
4. For profile creation or refresh read `voice-card.md`. Ask for a bounded sample source and consent before collecting across email, chat, documents, or calendar. Prefer 15 to 30 genuine samples across three channels; fewer samples mean lower confidence, not permission to fabricate habits.
5. Present the profile for correction, including words never used, phrases to preserve, and misreadings. Save or update it in the user's chosen location only after approval; a Google Doc is an option, not a mandatory external write.

Preserve personality, useful contractions, characteristic openings and closings, and channel formatting. Current formatting instructions beat historical examples. Do not insert inline warnings or editorial notes into ready-to-send copy. The profile changes only on explicit correction or an approved update; user edits may justify an offer to update, not an automatic rescan. Keep sample excerpts and recipient details out of public deliverables.

Integration approval alone does not authorize a fresh source scan. Do not create or update a Voice Card merely because an edit was requested.

## Slop rubric (formerly no-ai-slop)

Its main editing rules and vocabulary list already live in `editing-rules.md`. The full original guide is preserved in `slop-source-guide.md` and its acceptance rubric in `slop-eval.md`.

- Read `slop-eval.md` when the user asks for the original rubric, when checking a revised editing workflow, or when running acceptance examples.
- Read `slop-source-guide.md` only for a source-specific check beyond the indexed patterns. Apply its rules under the hub's minimum-edit and output-mode contract.
- No scientific-tells reference was ever bundled; do not fabricate one or treat the rubric as an authorship test.

## One pass, no loops

Voice context, slop rules, and quality checks feed one minimum-edit pass and one internal final check. Do not stack audit, draft, and final versions or add automatic "What changed" sections from older instructions.

## Route examples

| Request | Result |
|---|---|
| "Tighten this two-line note." | Plain humanizer edit in the draft's voice; no Voice Card work. |
| "Rewrite my investor email so it sounds like me." | Reuse the approved Voice Card's email register, or the draft and samples if none; one rewrite. |
| "Keep this guest author's swear words and long asides." | Preserve that author's quirks; do not apply the user's Voice Card. |
| "Does this sound AI-written? Don't edit it." | Quote passage, name pattern, short remedy. No rewrite, score, or authorship verdict. |
| "Check this rewrite against the no-ai-slop rubric." | Read `slop-eval.md`; report results with no second edit. |
| "Make this formal, but keep the code and quoted testimony verbatim." | Read `guide-mode.md`; edit only surrounding prose. |
| "Create my Voice Card from these three samples." | Voice-profile mode with `voice-card.md`; low-confidence coverage noted, no broader collection. |
| "Explain the API error." | Lightweight prose check only; exact code and error text preserved. |
