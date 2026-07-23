# Roadmap

## Phase 1 — Portfolio foundation

- Professional README.
- Architecture and case-study documentation.
- Generic MCP tool contracts.
- Security, limitations and technical decisions.
- Safe environment template.
- Reusable download-policy component.

## Phase 2 — Minimal runnable server

- Generic FastMCP server entrypoint.
- Pluggable document-source interface.
- Synthetic HTML catalog adapter.
- Metadata normalization without organization-specific rules.
- Local download directory configuration.
- Optional SMTP adapter with safer validation.

## Phase 3 — Quality

- Unit tests for URL and filename policies.
- Integration tests with a synthetic document catalog.
- Tool contract tests.
- Type checking and linting.
- GitHub Actions for automated validation.

## Phase 4 — Security hardening

- Content-Type and PDF-signature validation.
- Maximum download size.
- Request and browser timeouts.
- Recipient policy and confirmation for email.
- Structured audit events.
- Dependency pinning and vulnerability scanning.

## Phase 5 — Distribution

- Reproducible packaging.
- Cross-platform launch guidance.
- Health diagnostics for local clients.
- Versioned releases and changelog.

The roadmap describes intended public reconstruction work, not completed production capabilities.
