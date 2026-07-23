# Technical Decisions

## Client-orchestrated design

The AI desktop client provides the model, chat interface and reasoning loop. The local server focuses on deterministic capabilities. This reduces duplicated infrastructure and keeps tool execution close to the user's machine.

## MCP over `stdio`

Standard input/output is appropriate for a local desktop integration because it avoids opening a network port and allows the client to manage the server process directly.

## FastMCP

FastMCP provides concise tool registration and structured contracts, making the server easier to inspect than a custom protocol implementation.

## Playwright for dynamic sources

A browser-based adapter was selected because some public document catalogs depend on dynamically rendered pages. BeautifulSoup is then used to parse the captured HTML.

## pandas for normalization and search

The working implementation uses a DataFrame to normalize dates, sort records and perform case-insensitive metadata search. This is practical for a small public catalog, although a lighter data model may be preferable for a reusable package.

## Short-lived cache

A brief in-memory cache reduces repeated browser launches while keeping data reasonably fresh. It is process-local and intentionally simple.

## Environment-based SMTP configuration

Credentials are kept outside source code. This is suitable for local development, while production deployments should use a dedicated secret-management solution.

## Public reconstruction

The portfolio repository uses generic document terminology and selected reusable components instead of copying the private implementation verbatim. This preserves technical evidence without exposing the original source or operational context.
