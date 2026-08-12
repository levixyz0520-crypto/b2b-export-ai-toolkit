from export_ai.customer_research import research_customer


def test_research_plan_preserves_profile_fields() -> None:
    result = research_customer(
        {"company_name": "Fictional Buyer", "country": "Exampleland", "products": ["sofa"]}
    )
    assert result["company_name"] == "Fictional Buyer"
    assert result["product_interest"] == ["sofa"]
    assert result["status"] == "needs_research"
