# Contributing

Thank you for helping build an auditable toolkit for B2B exporters.

## Before contributing

- Use only fictional, public, or properly authorized information.
- Never submit credentials, private customer data, contact lists, proprietary quotations, or confidential communications.
- Open an issue before a large feature or architecture change.
- Keep the industry-neutral core separate from product-specific examples.

## Development workflow

1. Fork the repository and create a focused branch from `main`.
2. Install Python 3.10+ and run `python -m pip install -e ".[dev]"`.
3. Add type hints, public-function docstrings, and tests for behavior changes.
4. Run `ruff check .` and `pytest`.
5. Update documentation and `CHANGELOG.md` when user-visible behavior changes.
6. Submit a pull request that explains the change, rationale, tests, and privacy impact.

Use [Conventional Commits](https://www.conventionalcommits.org/) where practical, such as `feat: add importer qualification rule` or `fix: preserve zero-value quote adjustments`.

By contributing, you agree that your contribution is licensed under the MIT License and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).
