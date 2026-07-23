"""Validation helpers for controlled PDF downloads."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from urllib.parse import unquote, urlparse


class DownloadPolicyError(ValueError):
    """Raised when a requested download violates the configured policy."""


@dataclass(frozen=True)
class DownloadPolicy:
    """Validate remote PDF URLs and derive safe local filenames."""

    allowed_domain: str
    allow_subdomains: bool = True

    def __post_init__(self) -> None:
        normalized = self.allowed_domain.strip().lower().lstrip(".")
        if not normalized or "/" in normalized or ":" in normalized:
            raise ValueError("allowed_domain must be a hostname")
        object.__setattr__(self, "allowed_domain", normalized)

    def validate_url(self, url: str) -> str:
        """Return a safe filename when the URL complies with the policy."""
        parsed = urlparse(url.strip())
        hostname = (parsed.hostname or "").lower()

        if parsed.scheme not in {"http", "https"}:
            raise DownloadPolicyError("Only HTTP and HTTPS URLs are allowed")

        domain_matches = hostname == self.allowed_domain
        if self.allow_subdomains:
            domain_matches = domain_matches or hostname.endswith(
                f".{self.allowed_domain}"
            )

        if not domain_matches:
            raise DownloadPolicyError("The URL hostname is not allowlisted")

        if not parsed.path.lower().endswith(".pdf"):
            raise DownloadPolicyError("Only PDF paths are allowed")

        raw_name = unquote(Path(parsed.path).name)
        safe_name = self.sanitize_filename(raw_name)

        if not safe_name:
            raise DownloadPolicyError("A safe filename could not be derived")

        return safe_name

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Remove characters that are unsafe on common desktop filesystems."""
        cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", filename).strip()
        cleaned = cleaned.rstrip(". ")

        if cleaned in {"", ".", ".."}:
            return ""

        return cleaned
