"""Generate conservative first-contact email drafts."""

from typing import Any


def create_email(data: dict[str, Any]) -> dict[str, str]:
    """Create a deterministic plain-text email that avoids invented claims."""
    contact = str(data.get("contact_name") or "there").strip()
    company = str(data.get("company_name") or "your company").strip()
    product = str(data.get("product") or data.get("product_interest") or "our products").strip()
    sender = str(data.get("sender_name") or "Export team").strip()
    subject = f"Exploring {product} supply for {company}"
    body = (
        f"Hello {contact},\n\n"
        f"I am reaching out to ask whether {company} is currently evaluating {product}. "
        "If relevant, we can share specifications, packing options, lead-time assumptions, "
        "and a clearly itemized quotation.\n\n"
        "Would a short product summary be useful? If this is not relevant, please let me know "
        "and I will not follow up.\n\n"
        f"Best regards,\n{sender}"
    )
    return {"subject": subject, "body": body}
