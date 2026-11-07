## Language and grammar patterns

Legacy vocabulary/era notes below are retained as guide observations, not verified model-specific frequency measurements. Use them only to notice potentially empty wording; do not assign authorship, infer a model, or enforce word bans. Research distinguishes corpus-level vocabulary change from individual authorship and shows strong model/genre variation. ([Kobak et al.](https://arxiv.org/html/2406.07016), [PNAS](https://www.pnas.org/doi/10.1073/pnas.2422455122))

Examples that add roles, quantities, or other facts require independent support. The hub's preservation contract and `writing-quality-gate.md` govern every transformation.

### 9. Overused "AI vocabulary" words

**High-frequency AI words (all eras):** Additionally (especially starting a sentence), align with, boasts (meaning "has"), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**By model era** (rough guide; the dates are approximate):

| Era | Model | Words that cluster |
|---|---|---|
| 2023 to mid-2024 | GPT-4 | Additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant |
| Mid-2024 to mid-2025 | GPT-4o | align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant |
| Mid-2025 to mid-2026 | GPT-5 | emphasizing, enhance, highlighting, showcasing, plus the media-coverage wording in pattern 2 |
| Mid-2026 on | GPT-6 | challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally, with heavy use of periods and commas and sentences held to roughly 8 to 20 words (see pattern 18) |

Grok overuses words that sound scientific (causal, empirical, correlate) and still overuses "underscore" in 2026.

**Problem:** Generic vocabulary clusters can replace useful detail, but a cluster is not an authorship verdict. Review actual precision and reader value; "underscore" can correctly denote a character or film music. Do not merely swap synonyms or treat a word's absence as proof.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.


### 10. Avoidance of "is"/"are" (copula avoidance)

**Words to watch:** serves as/stands as/marks/functions as/operates as/represents [a], boasts/features/maintains/offers [a], holds the distinction of being, refers to (in an opening sentence)

**Problem:** LLMs substitute elaborate constructions for simple copulas and marketing verbs ("features," "offers") for plain "has." AI copyedits often "improve" text this way. Newer output gets more elaborate: "ventured into politics as a candidate" instead of "was a candidate," "began his career as" instead of "was." In opening sentences, LLMs may write "X refers to..." as if the piece were about the word instead of the thing. Don't confuse this with "has been featured" (present perfect), which is fine.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet. Harian Metro holds the distinction of being the first Malay-language tabloid.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four separate spaces and over 3,000 square feet. Harian Metro is the first Malay-language tabloid.


### 11. Negative parallelisms and tailing negations

**Problem:** The text sounds like it is correcting a misconception nobody raised. Three shapes:
- Not just X, but also Y: "Not only... but...", "It's not just about..., it's...". This can span sentences, with "however" doing the contrast.
- Not X, but Y: "It's not..., it's...", "no..., no..., just...".
- Y rather than X: the reversed form, especially common in recent output ("prioritizing consolidation of power rather than ideological purity").

Clipped tailing-negation fragments such as "no guessing" or "no wasted motion," tacked onto the end of a sentence instead of written as a real clause, belong here too.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (Y rather than X):**
> The council chose to repave the road, prioritizing long-term durability rather than short-term savings.

**After:**
> The council chose to repave the road, favoring long-term durability over short-term savings.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item without forcing the user to guess.


### 12. Rule of three overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive, from "adjective, adjective, adjective" to "short phrase, short phrase, and short phrase." It's a stronger tell where people rarely bother with flourishes: commit messages, edit summaries, quick replies.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.


### 13. Elegant variation (synonym cycling)

**Problem:** Older AI models had repetition penalties that pushed them to swap in synonyms for words they had already used. This is mostly an older-model habit. Non-native writers also avoid repeats on purpose (Italian schools teach it, for example), so don't treat it as proof.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.


### 14. False ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.


### 15. Passive voice and subjectless fragments

**Problem:** LLMs often hide the actor or drop the subject entirely with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite these when active voice makes the sentence clearer and more direct.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.


### 16. Treating a title or topic as a named thing

**Problem:** When a piece has a descriptive title (a list, a broad topic), AI openers define the title as if it were a real-world entity instead of talking about the subject.

**Before:**
> The List of Songs About Mexico is a comprehensive compilation celebrating the nation's musical heritage.

**After:**
> These songs are about Mexico or set there.

