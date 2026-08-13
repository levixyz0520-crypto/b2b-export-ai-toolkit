"""Create a structured research checklist from a buyer or company profile."""

from typing import Any


def research_customer(data: dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic research plan without making network requests."""
    company = str(data.get("company_name") or data.get("company") or "Unknown company").strip()
    country = str(data.get("country") or "Unknown").strip()
    products = _strings(data.get("products") or data.get("product_interest"))
    return {
        "company_name": company,
        "country": country,
        "product_interest": products,
        "research_questions": [
            "Verify the legal company name and official website.",
            "Identify product-market fit and likely buying role.",
            "Check public evidence of import, retail, distribution, or project activity.",
            "Record source URLs and retrieval dates for every material claim.",
            "Flag missing, conflicting, or sensitive information for human review.",
        ],
        "status": "needs_research",
    }


def _strings(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [part.strip() for part in str(value).split(",") if part.strip()]
