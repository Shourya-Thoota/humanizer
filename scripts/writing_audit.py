#!/usr/bin/env python3
"""Local review candidates, not an authorship detector or automatic rewriter."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

RULES = [
    ("portable-opening", r"\bin today['’]s (?:rapidly (?:changing|evolving)|fast-paced) world\b",
     "Does this opening supply context, or merely delay the subject?"),
    ("inflated-significance", r"\b(?:marks? a pivotal moment|testament to|unparalleled (?:success|efficiency))\b",
     "Replace unsupported significance with supplied facts, if warranted."),
    ("vague-attribution", r"\b(?:experts agree|studies show|widely regarded as)\b",
     "Check nearby attribution and evidence; do not invent a source."),
    ("rhetorical-contrast", r"\bnot (?:just|merely|only)\b[^.!?\n]{1,100}\bbut\b",
     "Keep a meaningful distinction; review only an empty or false contrast."),
    ("filler", r"\b(?:in order to|it is important to note that|at the end of the day)\b",
     "Check whether the phrase earns its place in this register."),
    ("output-preamble", r"\bhere['’]s (?:your|the) (?:revised|rewritten|humanized) (?:version|text)\b",
     "Remove staging from edited-text-only output unless requested."),
]
URL = re.compile(r"https?://[^\s<>\"`]+")
NUMBER = re.compile(r"(?<![\w])[-+]?\d+(?:[,.]\d+)*(?:%|[A-Za-z]+)?")
FORCE = re.compile(r"\b(?:not|never|only|unless|may|might|can|must|should|all|some|estimated|proposed|approved)\b", re.I)


def protected_spans(text):
    """Recognize common Markdown spans; intentionally not a full parser."""
    spans = []
    offset = 0
    fence = None
    start = 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r" {0,3}(`{3,}|~{3,})", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                spans.append((start, offset + len(line), "code"))
                fence = None
        elif marker:
            fence, start = marker[1], offset
        elif re.match(r"(?: {4}|\t)", line):
            spans.append((offset, offset + len(line), "code"))
        elif re.match(r" {0,3}>", line):
            spans.append((offset, offset + len(line), "quotation"))
        offset += len(line)
    if fence:
        spans.append((start, len(text), "code"))
    patterns = [
        (r"(`+)([^\n]*?)\1", "code"),
        (r'"[^"\n]+"|“[^”\n]+”|‘[^’\n]+’', "quotation"),
        (URL.pattern, "url"),
    ]
    for pattern, kind in patterns:
        for match in re.finditer(pattern, text):
            if not any(match.start() < b and match.end() > a for a, b, _ in spans):
                spans.append((match.start(), match.end(), kind))
    return sorted(spans)


def visible_text(text):
    chars = list(text)
    for a, b, _ in protected_spans(text):
        for i in range(a, b):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


def inventory(text):
    spans = protected_spans(text)
    result = {
        "code": Counter(text[a:b] for a, b, k in spans if k == "code"),
        "quotations": Counter(text[a:b] for a, b, k in spans if k == "quotation"),
        "urls": Counter(URL.findall(text)),
        "numbers": Counter(NUMBER.findall(visible_text(text))),
        "logical_force": Counter(x.lower() for x in FORCE.findall(visible_text(text))),
    }
    return result


def audit(text, original=None, exact=()):
    visible = visible_text(text)
    findings = []
    for rule, expression, question in RULES:
        for match in re.finditer(expression, visible, re.I):
            findings.append({
                "rule": rule, "line": text.count("\n", 0, match.start()) + 1,
                "excerpt": text[match.start():match.end()],
                "review": question,
            })
    seen = {}
    for match in re.finditer(r"\S[^\n]*(?:\n(?!\s*\n)[^\n]+)*", visible):
        paragraph = " ".join(match[0].split())
        if len(paragraph) < 80:
            continue
        if paragraph in seen:
            findings.append({
                "rule": "repeated-paragraph",
                "line": text.count("\n", 0, match.start()) + 1,
                "excerpt": paragraph[:160],
                "review": "Check whether exact paragraph repetition is intentional.",
            })
        seen[paragraph] = True
    changes = []
    if original is not None:
        before, after = inventory(original), inventory(text)
        for category in before:
            removed = list((before[category] - after[category]).elements())
            added = list((after[category] - before[category]).elements())
            if removed or added:
                changes.append({"category": category, "removed": removed, "added": added})
    for fragment in exact:
        if fragment not in text:
            changes.append({"category": "required_exact", "removed": [fragment], "added": []})
    return {
        "tool": "humanizer-writing-review",
        "authorship_assessment": "not_performed",
        "semantic_verification": "not_performed",
        "review_candidates": findings,
        "preservation_changes": changes,
        "limitations": [
            "Heuristic English/Markdown review, not a full parser or fact checker.",
            "No AI probability, pass/fail quality score, rewriting, or network requests.",
            "Protected-span recognition is incomplete; compare original and final manually.",
            "Token inventories miss paraphrases, reordered assignments, scope and causal changes.",
            "A change can be legitimate; a clean report does not establish meaning preservation.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path)
    parser.add_argument("--original", type=Path)
    parser.add_argument("--require-exact", action="append", default=[])
    args = parser.parse_args()
    try:
        text = args.draft.read_text(encoding="utf-8")
        original = args.original.read_text(encoding="utf-8") if args.original else None
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read input: {exc}\n")
    print(json.dumps(audit(text, original, args.require_exact), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
