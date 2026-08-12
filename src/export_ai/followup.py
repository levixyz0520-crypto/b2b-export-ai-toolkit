"""Generate respectful, deterministic sales follow-up messages."""

from typing import Any


def create_followup(data: dict[str, Any]) -> dict[str, str]:
    """Create a concise follow-up with an explicit opt-out."""
    contact = str(data.get("contact_name") or "there").strip()
    topic = str(data.get("topic") or data.get("product") or "the information shared").strip()
    channel = str(data.get("channel") or "whatsapp").lower().strip()
    message = (
        f"Hello {contact}, just checking whether you had a chance to review {topic}. "
        "I can clarify specifications, packing, lead time, or quotation assumptions. "
        "If the timing is not right, tell me and I will pause follow-ups."
    )
    return {"channel": channel, "message": message}
