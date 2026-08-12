---
name: buyer-qualification
description: Qualify prospective B2B export buyers with a transparent evidence-based rubric. Use to score buyer fit, identify missing qualification data, prioritize human review, or explain why a lead is high, medium, or low confidence.
---

# Buyer Qualification

## Purpose

Prioritize research and sales attention without presenting a score as proof of creditworthiness or intent.

## Inputs

- Sanitized buyer profile
- Product interest, expected volume, timing, and buying role
- Source evidence and organization-specific scoring rubric

## Outputs

- Numeric score and tier
- Criterion-by-criterion evidence
- Missing fields, confidence, and recommended next action

## Workflow

1. Validate that the company identity and source evidence are usable.
2. Apply the stated rubric consistently.
3. Award points only for present, relevant evidence.
4. List missing fields and conflicts.
5. Explain the tier and route the result to human review.

## Guardrails

- Do not infer protected traits or use them in scoring.
- Do not claim credit, sanctions, legal, or compliance clearance.
- Do not manufacture evidence to raise a score.
- Keep scoring logic visible and editable.
- Do not automatically reject or contact a buyer based only on the score.

## Example

Input: the fictional `examples/furniture-export/buyer-profile.json`.

Output: a score with each awarded criterion, missing fields, and a human-review recommendation.
