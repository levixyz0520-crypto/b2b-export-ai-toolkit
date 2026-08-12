# B2B Export AI Toolkit

[简体中文](README.zh-CN.md)

B2B Export AI Toolkit is an open-source, AI-ready foundation for customer research, buyer qualification, outreach, quotation analysis, follow-up, and sales workflow automation. The first examples cover furniture export, while the Python modules and structured-data contracts are intentionally industry-neutral.

> **Status:** v0.1 is an early-stage foundation. It provides deterministic utilities, examples, and agent skills—not autonomous selling, verified market intelligence, or production CRM integrations. Outputs require human review.

## Who it is for

- Export sales and operations teams that want auditable workflow building blocks
- Developers building privacy-conscious export tools
- Researchers, consultants, and educators documenting repeatable B2B processes
- Contributors adapting the toolkit to new products, markets, and industries

## Why this project exists

Export workflows are often fragmented across spreadsheets, private templates, and opaque automation. This project creates a small, inspectable common layer that can later connect to AI models and business systems without making those services mandatory.

## Installation

Python 3.10 or newer is required.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
```

For development:

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

## Usage

Commands accept a JSON file, inline JSON object, or plain text and emit stable JSON. No OpenAI API key is needed.

```bash
export-ai research examples/furniture-export/buyer-profile.json
export-ai qualify examples/furniture-export/buyer-profile.json
export-ai email examples/furniture-export/outreach-input.json
export-ai followup examples/furniture-export/followup-scenario.json
export-ai quote examples/furniture-export/quotation-input.json
export-ai sanitize '{"email":"fictional@example.invalid","note":"call +1 202 555 0100"}'
```

The modules are also reusable from Python:

```python
from export_ai.buyer_qualification import qualify_buyer

result = qualify_buyer({"company_name": "Example", "country": "Exampleland"})
```

## Project principles

1. **Deterministic before autonomous:** keep v0.1 behavior reproducible and reviewable.
2. **Evidence over inference:** distinguish sourced facts, assumptions, and missing data.
3. **Privacy by design:** minimize inputs, sanitize exports, and never commit private sales data.
4. **Human accountability:** people approve outreach, commercial terms, and consequential decisions.
5. **Industry-neutral core:** furniture is an example, not a hard-coded product model.
6. **Small dependency surface:** prefer standard-library code and transparent data contracts.

## Repository map

- `src/export_ai/` — deterministic workflow modules and CLI
- `examples/furniture-export/` — fictional, privacy-safe structured examples
- `skills/` — concise Codex/agent workflows with guardrails
- `tests/` — deterministic core and CLI tests

The numbered legacy directories referenced in the initial foundation brief were not present in this repository at implementation time, so no existing knowledge was removed or migrated.

## Roadmap

- **v0.1:** deterministic core, furniture examples, skills, tests, and community files
- **v0.2:** documented schemas, pluggable data sources/model adapters, richer validation, localization, and CRM-safe import/export interfaces
- **Later:** opt-in integrations, evaluation datasets, additional export industries, and workflow orchestration

Roadmap items are intentions, not delivery commitments.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md), follow the [Code of Conduct](CODE_OF_CONDUCT.md), and open an issue before large changes. Bug reports, tests, translations, industry-safe examples, and documentation improvements are welcome.

## Privacy and security

Use fictional or properly authorized data only. Do not commit customer records, personal contact lists, credentials, API keys, proprietary quotations, private communications, or confidential company information. Sanitize examples before sharing and verify every generated claim. Report vulnerabilities using [SECURITY.md](SECURITY.md), not a public issue.

## License

Licensed under the [MIT License](LICENSE).
