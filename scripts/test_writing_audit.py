#!/usr/bin/env python3
import unittest
from writing_audit import audit, visible_text


class WritingAuditTests(unittest.TestCase):
    def test_flags_review_candidate(self):
        result = audit("This marks a pivotal moment.")
        self.assertEqual(result["review_candidates"][0]["rule"], "inflated-significance")

    def test_no_authorship_verdict(self):
        result = audit("Experts agree.")
        self.assertEqual(result["authorship_assessment"], "not_performed")
        self.assertNotIn("score", result)

    def test_ordinary_formal_text(self):
        self.assertFalse(audit("The pilot may reduce errors, but the sample is small.")["review_candidates"])

    def test_punctuation_and_single_word_not_flags(self):
        self.assertFalse(audit("We delve into the mechanism; the result is uncertain.")["review_candidates"])

    def test_fenced_code(self):
        self.assertFalse(audit("```python\nprint('experts agree')\n```\n")["review_candidates"])

    def test_unclosed_fence(self):
        self.assertFalse(audit("~~~\nExperts agree")["review_candidates"])

    def test_indented_code(self):
        self.assertFalse(audit("    Experts agree\n")["review_candidates"])

    def test_inline_code(self):
        self.assertFalse(audit("Use `experts agree` as the test input.")["review_candidates"])

    def test_quotation(self):
        self.assertFalse(audit('The quote is “experts agree.”')["review_candidates"])

    def test_block_quote(self):
        self.assertFalse(audit("> Experts agree.\n")["review_candidates"])

    def test_url_mask(self):
        self.assertNotIn("https", visible_text("See https://example.org/test."))

    def test_line_numbers(self):
        result = audit("A useful opening.\n\nExperts agree.")
        self.assertEqual(result["review_candidates"][0]["line"], 3)

    def test_number_change(self):
        result = audit("The cost is 30 USD.", "The cost is 20 USD.")
        self.assertIn("numbers", [x["category"] for x in result["preservation_changes"]])

    def test_negation_change(self):
        result = audit("It is approved.", "It is not approved.")
        self.assertIn("logical_force", [x["category"] for x in result["preservation_changes"]])

    def test_url_change(self):
        result = audit("[report](https://example.org/b)", "[report](https://example.org/a)")
        self.assertIn("urls", [x["category"] for x in result["preservation_changes"]])

    def test_quote_change(self):
        result = audit('“It helps.”', '“It may help.”')
        self.assertIn("quotations", [x["category"] for x in result["preservation_changes"]])

    def test_code_change(self):
        result = audit("`x=2`", "`x=1`")
        self.assertIn("code", [x["category"] for x in result["preservation_changes"]])

    def test_exact_requirement(self):
        result = audit("Deadline pending.", exact=["Friday at noon"])
        self.assertEqual(result["preservation_changes"][0]["category"], "required_exact")

    def test_identical_original(self):
        text = "It may help 20 users. “Keep this.” `x=1` https://example.org"
        self.assertFalse(audit(text, text)["preservation_changes"])

    def test_repeated_paragraph(self):
        paragraph = "This paragraph explains the actual requirement in enough detail to exceed the review threshold."
        result = audit(paragraph + "\n\n" + paragraph)
        self.assertIn("repeated-paragraph", [x["rule"] for x in result["review_candidates"]])


if __name__ == "__main__":
    unittest.main()
