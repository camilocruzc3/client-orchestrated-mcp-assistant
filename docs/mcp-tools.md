# MCP Tools

The public design uses generic names so the server can represent different public PDF catalogs.

## `latest_documents`

Returns the most recent normalized documents.

Example result:

```json
[
  {
    "identifier": "DOC-2026-001",
    "published_at": "2026-01-15",
    "subject": "Example public document",
    "download_urls": ["https://example.com/documents/doc-2026-001.pdf"]
  }
]
```

## `list_documents`

Returns the complete catalog currently available from the configured adapter. A short-lived cache may be used to reduce repeated browser work.

## `search_documents`

Input:

```json
{"query": "risk management"}
```

Searches normalized identifiers and subjects without treating the query as a regular expression.

## `download_document`

Input:

```json
{"url": "https://example.com/documents/doc-2026-001.pdf"}
```

Validates the scheme, hostname and PDF path before writing to local storage. The result should report success, local filename and destination path without exposing unrelated filesystem information.

## `send_notification`

Input:

```json
{
  "recipient": "reviewer@example.com",
  "subject": "Document available",
  "message": "The requested PDF has been downloaded."
}
```

Uses SMTP configuration from environment variables. Production environments should add recipient policies, rate limits, audit records and explicit confirmation for external side effects.
