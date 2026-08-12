from export_ai.followup import create_followup
from export_ai.outreach import create_email


def test_email_uses_only_supplied_context() -> None:
    result = create_email({"contact_name": "Alex", "company_name": "Demo", "product": "sofas"})
    assert "sofas" in result["subject"]
    assert "I will not follow up" in result["body"]


def test_followup_contains_pause_option() -> None:
    result = create_followup({"contact_name": "Alex", "topic": "the quote"})
    assert result["channel"] == "whatsapp"
    assert "pause follow-ups" in result["message"]
