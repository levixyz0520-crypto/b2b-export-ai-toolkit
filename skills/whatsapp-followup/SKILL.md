---
name: whatsapp-followup
description: Draft permission-aware WhatsApp follow-ups for B2B export conversations. Use for post-quotation check-ins, sample or specification follow-up, stalled conversation handling, and concise multilingual-ready messages.
---

# WhatsApp Follow-up

## Purpose

Continue an existing business conversation helpfully and without pressure.

## Inputs

- Sanitized conversation summary
- Last interaction date, topic, stage, timezone, and follow-up consent
- Specific question or assistance to offer

## Outputs

- One concise message
- Suggested send window and stop condition
- Any claims or attachments requiring review

## Workflow

1. Confirm an existing relationship or valid permission to message.
2. Summarize the last relevant context accurately.
3. Ask one clear question or offer specific help.
4. Respect local time and frequency limits.
5. Include a natural pause or opt-out path.

## Guardrails

- Do not create fake urgency, scarcity, or prior agreement.
- Do not repeatedly message an unresponsive recipient.
- Do not include confidential pricing or documents without authorization.
- Follow applicable privacy, messaging, and anti-spam rules.
- Stop when asked and require human approval before sending.

## Example

Input: fictional buyer received sofa specifications seven days ago.

Output: ask whether specifications need clarification and offer to pause if timing is not right.
