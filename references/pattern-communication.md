## Communication patterns

These contextual examples adapt [Wikipedia's field guide](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Preserve real evidentiary limitations and relationship-sensitive courtesy; no phrase here is proof of authorship.

### 30. Collaborative communication artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., is there anything else, let me know, more detailed breakdown, here is a..., a Wikipedia-style article

**Problem:** Text meant as chatbot correspondence gets pasted as content. Also watch for instructions meant only for the user: "Delete this section before submission," numbered "submission notes," checklists of what to do before publishing, and advice hidden in HTML comments.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.


### 31. Hedging disclaimers about sources and how to read them

**Words to watch:** While specific details are limited/scarce..., not widely available/documented/disclosed, in the provided/available sources, in the search results, based on available information, maintains a low profile, keeps personal details private, [claim] should be treated/presented as... rather than..., does not by itself establish, it does not establish that

**Problem:** Wikipedia lists these among the most common current signs. They come in two kinds:
1. A chatbot that couldn't find information says it "isn't publicly documented," then guesses what it "likely" is. Both the claim that it's undocumented and the guess are speculation. About people, this turns into "maintains a low profile."
2. Since mid-2026, models add disclaimers telling the reader how to treat a source, usually as a negative parallelism: "should be treated as religious tradition rather than as an archaeological explanation," or "It does not establish that..."

**Before:**
> The guidance explains why subsurface conditions require separate attention from visible planting. It does not establish that Benjakitti has a particular contamination problem or groundwater configuration.

**After:**
> The guidance explains why subsurface conditions need separate attention from visible planting.

This shortening is valid only if the removed limitation is redundant in context. If readers might otherwise infer a site-specific contamination claim, retain the limitation.

**Fix:** Say what the source supports. State a relevant unknown once and plainly; never turn “not found in the reviewed sources” into “not publicly documented,” and never delete a limit that prevents a false inference.


### 32. Customer-service tone in messages and replies

**Words to watch:** I hope this message finds you well, I am writing to..., Dear [X] Team, I understand your concern(s) regarding..., I have carefully reviewed..., I apologize for any inconvenience I may have caused, If there are specific issues, please point them out and I will address them

**Problem:** AI-written emails, comments, and replies sound like a clerk or a support agent. Long replies split into headed sections are part of the same look.

**Before:**
> I hope this message finds you well. I have carefully reviewed your feedback and apologize for any inconvenience this may have caused. If there are specific issues, please point them out and I will address them promptly.

**After:**
> Thanks for the notes. Which part should I fix first?


### 33. Sycophantic/Servile tone

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.


## Change summaries

Applies to commit messages, PR descriptions, changelogs, edit summaries, and this skill's own "What changed" notes.

### 34. Canned change summaries

**Words to watch:** ensured... adheres to, refined, enhanced, enriched, streamlined, improved clarity/flow/readability, in compliance with, neutral/encyclopedic tone, preserved/preserving, retained/retaining, avoided/avoiding, aimed to, added sourced content, improved sourcing, addressed reviewer feedback

**Problem:** AI summaries stack vague improvements ("improved clarity, flow, and readability; refined tone"), reassure the reader that the work follows the rules, mention what was *not* changed ("while preserving the original meaning"), stress that content is "sourced" without saying what it says, itemize technical names, and announce the obvious ("addressed reviewer feedback"). A person names the specific change. Short summaries with ordinary abbreviations ("ce" for copy edit, "typo") are unlikely to be AI.

**Before:**
> Revised the section for clarity and flow; refined tone and enhanced readability while preserving the original meaning and technical details.

**After:**
> Cut the two-paragraph intro, merged the duplicate setup steps, and fixed the wrong port number.

If the user requests a What changed section, name the actual edits. Don't say you "preserved meaning" or "improved flow." Do not add change notes by default.
