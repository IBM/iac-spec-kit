from __future__ import annotations

import os
import ssl
import httpx
import truststore
from datetime import datetime, timezone

ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client = httpx.Client(verify=ssl_context)


def _github_token(cli_token: str | None = None) -> str | None:
    """Return sanitized GitHub token (cli arg takes precedence) or None."""
    return ((cli_token or os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or "").strip()) or None


def _github_auth_headers(cli_token: str | None = None) -> dict:
    """Return Authorization header dict only when a non-empty token exists."""
    token = _github_token(cli_token)
    return {"Authorization": f"Bearer {token}"} if token else {}


def _parse_rate_limit_headers(headers: httpx.Headers) -> dict:
    """Extract and parse GitHub rate-limit headers."""
    info = {}
    if "X-RateLimit-Limit" in headers:
        info["limit"] = headers.get("X-RateLimit-Limit")
    if "X-RateLimit-Remaining" in headers:
        info["remaining"] = headers.get("X-RateLimit-Remaining")
    if "X-RateLimit-Reset" in headers:
        reset_epoch = int(headers.get("X-RateLimit-Reset", "0"))
        if reset_epoch:
            reset_time = datetime.fromtimestamp(reset_epoch, tz=timezone.utc)
            info["reset_epoch"] = reset_epoch
            info["reset_time"] = reset_time
            info["reset_local"] = reset_time.astimezone()
    if "Retry-After" in headers:
        retry_after = headers.get("Retry-After")
        try:
            info["retry_after_seconds"] = int(retry_after)
        except ValueError:
            info["retry_after"] = retry_after
    return info


def _format_rate_limit_error(status_code: int, headers: httpx.Headers, url: str) -> str:
    """Format a user-friendly error message with rate-limit information."""
    rate_info = _parse_rate_limit_headers(headers)
    lines = [f"GitHub API returned status {status_code} for {url}"]
    lines.append("")
    if rate_info:
        lines.append("[bold]Rate Limit Information:[/bold]")
        if "limit" in rate_info:
            lines.append(f"  \u2022 Rate Limit: {rate_info['limit']} requests/hour")
        if "remaining" in rate_info:
            lines.append(f"  \u2022 Remaining: {rate_info['remaining']}")
        if "reset_local" in rate_info:
            reset_str = rate_info["reset_local"].strftime("%Y-%m-%d %H:%M:%S %Z")
            lines.append(f"  \u2022 Resets at: {reset_str}")
        if "retry_after_seconds" in rate_info:
            lines.append(f"  \u2022 Retry after: {rate_info['retry_after_seconds']} seconds")
        lines.append("")
    lines.append("[bold]Troubleshooting Tips:[/bold]")
    lines.append("  \u2022 If you're on a shared CI or corporate environment, you may be rate-limited.")
    lines.append("  \u2022 Consider using a GitHub token via --github-token or the GH_TOKEN/GITHUB_TOKEN")
    lines.append("    environment variable to increase rate limits.")
    lines.append("  \u2022 Authenticated requests have a limit of 5,000/hour vs 60/hour for unauthenticated.")
    return "\n".join(lines)
