"""Redact common sensitive values before data enters a workflow."""

import re
from typing import Any

_EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
_PHONE = re.compile(r"(?<!\w)(?:\+?\d[\d ()-]{7,}\d)")
_SECRET = re.compile(r"(?i)\b(api[_ -]?key|token|password|secret)\b\s*[:=]\s*[^\s,;]+")
_SENSITIVE_KEYS = {"email", "phone", "mobile", "password", "token", "api_key", "secret"}


def sanitize(value: Any) -> Any:
    """Recursively redact common personal contact details and credential-like values."""
    if isinstance(value, dict):
        return {
            str(key): "[REDACTED]" if str(key).lower() in _SENSITIVE_KEYS else sanitize(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        redacted = _EMAIL.sub("[REDACTED_EMAIL]", value)
        redacted = _PHONE.sub("[REDACTED_PHONE]", redacted)
        return _SECRET.sub(lambda match: f"{match.group(1)}: [REDACTED]", redacted)
    return value
