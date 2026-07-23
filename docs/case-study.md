# Case Study

## Context

Desktop AI clients can reason about a user's request but require explicit tools to interact with local files or external document sources. The private implementation addressed this gap by exposing a small set of document operations through the Model Context Protocol.

## Problem

A user needed to discover public PDF documents, search their metadata, download selected files and optionally send a notification without leaving the conversational interface. Implementing all reasoning inside a custom application would duplicate the model, chat interface and agent loop already provided by the desktop client.

## Solution

A local Python MCP server was created with tools for:

- Retrieving recent document metadata.
- Listing the complete available catalog.
- Searching by identifier or subject.
- Downloading a validated PDF.
- Sending an optional email notification.

The client remains the orchestrator. It interprets the user's request, selects a tool, receives structured output and decides whether another tool call is required.

## Engineering highlights

- Asynchronous browser automation for dynamic public pages.
- HTML parsing and metadata normalization.
- Short-lived in-memory caching.
- Controlled local file writes.
- Environment-based SMTP configuration.
- Separation of scraper, downloader, notifier and MCP registration concerns.

## Security approach

The implementation restricts downloads to an allowlisted domain and PDF paths, sanitizes filenames and excludes credentials from source control. The public reconstruction further removes the identity of the original source, personal paths, binaries and generated documents.

## Result

The project demonstrates a practical client-orchestrated agent pattern: use an existing AI desktop client for reasoning and provide narrowly scoped local capabilities through MCP.

## Honest scope

This repository is a portfolio reconstruction, not a complete production service. It does not claim multi-user deployment, enterprise authorization, automated evaluation, continuous integration or fully unattended operation.
