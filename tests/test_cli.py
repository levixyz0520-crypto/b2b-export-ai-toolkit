import json

import pytest

from export_ai.cli import load_input, main


def test_load_inline_json() -> None:
    assert load_input('{"company_name":"Demo"}') == {"company_name": "Demo"}


def test_cli_prints_json(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["qualify", '{"company_name":"Demo"}']) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["score"] == 10
