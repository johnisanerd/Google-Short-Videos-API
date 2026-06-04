# 🎬 Google Short Videos API: YouTube Shorts, Reels & TikTok results from one query

> The most efficient, reliable, and developer-friendly way to use the Google Short Videos API.

**Actor page:** [apify.com/johnvc/google-short-videos-api](https://apify.com/johnvc/google-short-videos-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-short-videos-api/input-schema](https://apify.com/johnvc/google-short-videos-api/input-schema?fpr=9n7kx3)

The Google Short Videos API returns the short-form video results Google surfaces for a search term, across platforms (YouTube Shorts, Facebook and Instagram Reels, TikTok, and more), plus the related "people also search for" suggestions shown on mobile. Every result comes back as a clean, flat JSON row tagged by type, so it drops straight into a table, a CSV, or an AI agent. Each row carries the video title, link, source platform, channel, duration, a preview clip URL when available, and the query and page it came from.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.10 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Short-Videos-API.git
   cd Apify-Google-Short-Videos-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-short-videos-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-short-videos-api-example.py
```

## Why Use This Google Short Videos API?

**Cross-platform in one call.** Instead of querying each platform separately, you get the short-form videos Google itself ranks for a term, spanning YouTube Shorts, Reels, TikTok, and other sources, in a single response.

**Clean, flat rows.** Each result is one row tagged with a `result_type`, so you can load it directly into a spreadsheet, a database, or an LLM context without reshaping nested data.

**Related searches included.** On mobile and tablet, the API also returns the "people also search for" suggestions, which are useful for keyword and topic research.

**Built for automation.** Pay-per-event pricing, structured JSON, and a published MCP server mean you can call it from code, schedule it, or hand it to an AI agent as a tool.

## Features

### Core Capabilities
- Search short-form videos by keyword across platforms (YouTube, Facebook, Instagram, TikTok, and more)
- Return the related "people also search for" block (mobile and tablet)
- Country, language, location, and Google-domain targeting
- Safe search, auto-correct, and duplicate filtering
- Multi-page pagination

### Data Quality
- Flat, predictable rows tagged by `result_type` (`short_video` or `people_also_search_for`)
- Fields per video: position, title, link, source, channel, duration, preview clip when available
- Stable output: a run that finds nothing still completes and reports zero results rather than failing

## Usage Examples

### Basic Example
```json
{
  "q": "workout tips",
  "max_pages": 1
}
```

### Advanced Example
```json
{
  "q": "electric cars",
  "device": "mobile",
  "gl": "us",
  "hl": "en",
  "location": "Austin, TX, Texas, United States",
  "safe": "active",
  "max_pages": 3
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `str` | YES | - | The search query for short videos |
| `device` | `str` | no | `mobile` | `mobile`, `tablet`, or `desktop`. Mobile or tablet also return "people also search for" |
| `location` | `str` | no | - | Localize results to a place. Cannot be combined with `uule` |
| `uule` | `str` | no | - | Encoded location string; takes precedence over `location` |
| `google_domain` | `str` | no | `google.com` | Google domain to query |
| `gl` | `str` | no | - | Two-letter country code |
| `hl` | `str` | no | - | Two-letter interface language code |
| `lr` | `str` | no | - | Language restriction (e.g. `lang_en`) |
| `tbs` | `str` | no | - | Advanced filter string |
| `safe` | `str` | no | `off` | `active` or `off` to filter explicit content |
| `nfpr` | `str` | no | `0` | Set `1` to exclude auto-corrected query results |
| `filter` | `str` | no | `0` | Set `1` to filter duplicate results |
| `max_pages` | `int` | no | `1` | Pages to fetch; `0` means all available. Each page returns about 10 videos |

## Output Format

Each dataset item is a flat row tagged by `result_type`. Real sample output for `q = "workout tips"`:

```json
[
  {
    "result_type": "short_video",
    "position": 1,
    "title": "The BEST Workout for Beginners",
    "link": "https://www.youtube.com/shorts/R8X-gXpe9C0",
    "clip": "https://encrypted-vtbn0.gstatic.com/video?q=tbn:...",
    "source": "YouTube",
    "channel": "ATHLEAN-X",
    "duration": "1:47",
    "query": "workout tips",
    "page_number": 1
  },
  {
    "result_type": "people_also_search_for",
    "title": "workout at home",
    "link": "https://www.google.com/search?q=workout+at+home",
    "query": "workout tips",
    "page_number": 1
  }
]
```

---

> Tip: the [Apify MCP configurator](https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api) shows a live, copy-paste setup panel for each client below. Open it and pick your client's tab (Claude Desktop, Claude.ai, Claude Code, Cursor, and more).

## Install in Claude Cowork Desktop

Cowork is the desktop app's automation mode. To give it the Google Short Videos API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Short Videos API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Short Videos API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-short-videos-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api`, using OAuth when prompted.
5. Ask Claude to run the Google Short Videos API.

Open Claude on the web: https://claude.ai

## Install in Cursor

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-short-videos-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Short Videos API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Short Videos API to power your data workflows with reliable, structured results.*

Last Updated: 2026.06.05
