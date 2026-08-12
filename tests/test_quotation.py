from export_ai.quotation import analyze_quotation


def test_quote_uses_decimal_totals() -> None:
    result = analyze_quotation({
        "currency": "usd",
        "items": [{"description": "Demo", "quantity": 3, "unit_price": "10.125"}],
        "adjustments": {"fee": "1.00"},
    })
    assert result["currency"] == "USD"
    assert result["subtotal"] == "30.38"
    assert result["total"] == "31.38"
    assert result["status"] == "indicative_only"
