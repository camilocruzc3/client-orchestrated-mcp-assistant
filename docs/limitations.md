# Limitations

- This public repository is not yet a complete runnable end-to-end server.
- The original document-source adapter is intentionally omitted.
- The design is optimized for one local user and one desktop client.
- The cache is in memory and resets when the process stops.
- There is no persistent job queue or unattended scheduler.
- Automated unit, integration and security tests are not yet included.
- CI/CD, dependency scanning and release automation are not yet configured.
- Email actions do not yet include recipient allowlists, approval workflows or rate limits.
- The initial implementation does not provide enterprise identity, RBAC or per-document authorization.
- Browser-based extraction depends on the external page structure remaining compatible.
- Production observability, metrics and distributed tracing are not implemented.

These limitations are documented to keep the portfolio claims aligned with the available evidence.
