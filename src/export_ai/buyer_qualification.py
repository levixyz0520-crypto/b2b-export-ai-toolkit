"""Score buyer profiles with a transparent, deterministic rubric."""

from typing import Any


def qualify_buyer(data: dict[str, Any]) -> dict[str, Any]:
    """Score a buyer from 0 to 100 and return reasons and missing fields."""
    criteria = {
        "company_name": 10,
        "country": 10,
        "website": 10,
        "buyer_type": 15,
        "product_interest": 15,
        "estimated_volume": 15,
        "target_timeline": 10,
        "decision_role": 10,
        "source_urls": 5,
    }
    score = 0
    evidence: list[str] = []
    missing: list[str] = []
    for field, points in criteria.items():
        if _present(data.get(field)):
            score += points
            evidence.append(f"{field}: +{points}")
        else:
            missing.append(field)
    tier = "high" if score >= 75 else "medium" if score >= 45 else "low"
    return {"score": score, "tier": tier, "evidence": evidence, "missing_fields": missing}


def _present(value: Any) -> bool:
    return value is not None and value != "" and value != [] and value != {}
