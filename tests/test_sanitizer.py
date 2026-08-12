from export_ai.sanitizer import sanitize


def test_sanitizer_redacts_nested_sensitive_values() -> None:
    result = sanitize({
        "email": "person@example.com",
        "notes": ["Call +1 202 555 0100", "api_key=abc123"],
        "safe": "fictional buyer",
    })
    assert result["email"] == "[REDACTED]"
    assert "[REDACTED_PHONE]" in result["notes"][0]
    assert "abc123" not in result["notes"][1]
    assert result["safe"] == "fictional buyer"
