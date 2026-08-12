from export_ai.buyer_qualification import qualify_buyer


def test_complete_profile_scores_100() -> None:
    fields = {
        "company_name": "Demo",
        "country": "Exampleland",
        "website": "https://demo.example",
        "buyer_type": "distributor",
        "product_interest": ["sofa"],
        "estimated_volume": "trial order",
        "target_timeline": "Q4",
        "decision_role": "buyer",
        "source_urls": ["https://demo.example/about"],
    }
    result = qualify_buyer(fields)
    assert result["score"] == 100
    assert result["tier"] == "high"
    assert result["missing_fields"] == []


def test_empty_profile_is_low_tier() -> None:
    result = qualify_buyer({})
    assert result["score"] == 0
    assert result["tier"] == "low"
