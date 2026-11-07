## Markup and chatbot artifacts

### 26. Markdown where it doesn't belong

**Problem:** Chatbots default to Markdown. Pasted somewhere that doesn't render it (an email, a Word doc, a form, a wiki, a text message), it leaves **asterisks** around words, ## before headings, [text](url) links, --- lines, and ``` code fences. Markdown by itself isn't a strong sign, since developers and people on Reddit, Discord, Slack, Obsidian, and Notes write it all the time. Markdown mixed with another format, or a code fence wrapped around ordinary prose, is a strong one.

**Fix:** Convert to the destination's format: real bold or none, plain headings, inline links or bare URLs, no fences around prose.


### 27. Leaked citation and tool markup

These strings can identify leftover tool markup, not who authored the surrounding prose. In edit mode, remove broken display artifacts only when the real citation/link can be preserved; never guess a destination or remove working citations. In detect mode, quote the artifact and suggest a formatting remedy without an authorship claim.

| Tool | Leftovers |
|---|---|
| ChatGPT | :contentReference[oaicite:0]{index=0}, oai_citation, citeturn0search0, turn0image0, turn0news0, turn1file0, ({"attribution":{"attributableIndex":"X-Y"}}), "Example+1" link text |
| Gemini | [cite: 1], [cite: 3, 12, 13], [span_1](start_span), [span_1](end_span) |
| Grok | grok_card tags, grok_render_citation_card_json |
| DeepSeek | lenticular brackets with daggers, like 【85†L261-269】 |
| Perplexity | [attached_file:1], [web:1], links containing ppl-ai-file-upload |
| Unknown | :::writing{variant="document" id="12345"} with a closing ::: |
| URLs | utm_source=chatgpt.com, utm_source=openai, utm_source=copilot.com, referrer=grok.com |
| Other | ↩ characters around footnotes |

A tracking parameter is not proof of how a link was found or who wrote the text; parameters can be copied or added. Preserve destinations and functional parameters unless a specific cleanup is requested.


### 28. Placeholder text left in

**Watch for:** [Entertainer's Name], [Your Company], (Add your URL here), (If available), dates like 2025-xx-xx, notes like "Add if available with citation."

**Fix:** Fill the gap from the draft or the user, or ask. Never invent the missing detail.


### 29. Citations that don't hold up

**Signs:** several dead links in a new piece (especially links the Internet Archive never saw), DOIs that don't resolve or lead to unrelated papers, ISBNs with invalid checksums, book citations with no page number, or real books whose cited pages don't say what the text claims. Paywalled links that work for other people, bot-mangled URLs, and truncated copy-paste are not signs.

**Fix:** Never invent a citation or "repair" one by guessing. Flag each one you can't verify so the user can check it against the real source.
