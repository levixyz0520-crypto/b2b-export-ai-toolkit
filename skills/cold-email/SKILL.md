---
name: cold-email
description: Draft respectful first-contact B2B export emails from verified buyer context. Use for privacy-conscious cold outreach, subject-line drafting, personalization from sourced facts, and opt-out-aware export sales messages.
---

# Cold Email

## Purpose

Create concise, relevant first-contact email drafts that a human can verify and approve.

## Inputs

- Approved company and contact context
- Product fit supported by evidence
- Sender identity, offer, desired next step, and locale

## Outputs

- Subject line and plain-text body
- Personalization facts used
- Claims requiring verification

## Workflow

1. Sanitize inputs and confirm the contact channel is lawfully obtained.
2. Use only verified personalization.
3. State relevance, value, and a low-friction next step.
4. Add a respectful opt-out.
5. Flag every commercial or compliance claim for human verification.

## Guardrails

- Do not fabricate familiarity, customers, certifications, capacity, prices, or urgency.
- Do not use deceptive reply prefixes or misleading subjects.
- Do not expose other recipients or personal data.
- Follow applicable anti-spam, privacy, and platform rules.
- Require human approval before sending.

## Example

Input: fictional distributor interested in compressed sofas.

Output: ask whether a specification and packing summary is useful; make no unsupported claim and provide an opt-out.
