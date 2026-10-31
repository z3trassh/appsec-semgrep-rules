def check(url):
    # ruleid: ssrf-allowlist-prefix
    if not url.startswith("http://cdn.lab.test"):
        raise ValueError

    # ruleid: ssrf-allowlist-prefix
    allowed = url.startswith("https://api.internal")
    return allowed


def ok(url):
    from urllib.parse import urlsplit

    # ok: ssrf-allowlist-prefix
    if urlsplit(url).hostname != "cdn.lab.test":
        raise ValueError

    # ok: ssrf-allowlist-prefix
    return url.startswith("/relative/path")
