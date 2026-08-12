---
name: quotation-analysis
description: Review and analyze B2B export quotation inputs and outputs. Use to calculate line totals, surface missing Incoterms or commercial assumptions, compare quote scenarios, and prepare an indicative quote for human commercial review.
---

# Quotation Analysis

## Purpose

Make quotation calculations and assumptions transparent before authorized commercial approval.

## Inputs

- Currency, items, quantities, and unit prices
- Adjustments, Incoterm, validity, lead time, payment, packing, and logistics assumptions

## Outputs

- Line totals, subtotal, adjustments, and total
- Missing terms and inconsistency warnings
- Explicit indicative status and human-review checklist

## Workflow

1. Sanitize buyer and internal identifiers.
2. Validate units, currency, quantities, and price precision.
3. Calculate with decimal arithmetic and show each step.
4. Identify missing or conflicting commercial terms.
5. Label assumptions and exclusions.
6. Route the result to an authorized person for approval.

## Guardrails

- Do not invent costs, margins, freight, duties, taxes, exchange rates, or terms.
- Do not represent an indicative analysis as a binding offer.
- Do not expose proprietary prices or margins without authorization.
- Do not provide legal, customs, tax, or sanctions clearance.
- Require human approval before sharing externally.

## Example

Input: fictional line items from `examples/furniture-export/quotation-input.json`.

Output: calculated totals plus reminders to review Incoterm, validity, payment, lead time, and tax/duty treatment.
