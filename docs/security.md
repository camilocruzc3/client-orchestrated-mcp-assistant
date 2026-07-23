# Security

## Existing controls represented

- Secrets are read from environment variables.
- Download URLs are parsed before use.
- Only configured domains are accepted.
- Only HTTP(S) PDF paths are eligible for download.
- Local filenames are sanitized.
- Existing files are not downloaded again by default.
- Generated documents, logs, local client configuration and binaries are excluded from version control.

## Risks

MCP tools can create side effects based on conversational input. The main risks are malicious URLs, unsafe filenames, oversized responses, misleading content types, repeated email actions, secret leakage and excessive trust in the connected client.

## Production recommendations

- Keep TLS certificate validation enabled.
- Validate response `Content-Type` and PDF magic bytes.
- Enforce file-size and request-time limits.
- Resolve DNS carefully to reduce SSRF and rebinding risks.
- Store downloads outside executable directories.
- Add recipient allowlists or confirmation for email actions.
- Apply rate limits and structured audit logs.
- Use a secret manager instead of persistent plaintext environment variables where appropriate.
- Run with least-privilege filesystem and network permissions.
- Pin and scan dependencies.
- Add tests for URL-policy bypass attempts.

## Public-repository privacy

The repository excludes the original source identity, personal paths, credentials, downloaded PDFs and operational configuration. Screenshots should follow the same boundary before publication.
