"""Calculate transparent indicative export quotations."""

from decimal import ROUND_HALF_UP, Decimal
from typing import Any


def analyze_quotation(data: dict[str, Any]) -> dict[str, Any]:
    """Calculate line totals and an indicative total using decimal arithmetic."""
    currency = str(data.get("currency") or "USD").upper()
    lines: list[dict[str, Any]] = []
    subtotal = Decimal("0")
    for index, item in enumerate(data.get("items", []), start=1):
        quantity = Decimal(str(item.get("quantity", 0)))
        unit_price = Decimal(str(item.get("unit_price", 0)))
        total = quantity * unit_price
        subtotal += total
        lines.append({
            "line": index,
            "description": str(item.get("description") or "Unspecified item"),
            "quantity": _number(quantity),
            "unit_price": _money(unit_price),
            "line_total": _money(total),
        })
    adjustments = sum(
        (Decimal(str(value)) for value in data.get("adjustments", {}).values()), Decimal("0")
    )
    grand_total = subtotal + adjustments
    return {
        "currency": currency,
        "items": lines,
        "subtotal": _money(subtotal),
        "adjustments_total": _money(adjustments),
        "total": _money(grand_total),
        "status": "indicative_only",
        "review_required": [
            "Incoterm",
            "validity",
            "payment terms",
            "lead time",
            "tax and duty treatment",
        ],
    }


def _money(value: Decimal) -> str:
    return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _number(value: Decimal) -> int | float:
    return int(value) if value == value.to_integral() else float(value)
