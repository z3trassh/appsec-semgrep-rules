# appsec-semgrep-rules

[Semgrep](https://semgrep.dev/) rules that catch the bug classes from my
[web-vuln-labs](https://github.com/z3trassh/web-vuln-labs): the point is to find
a class of bug once and then detect it everywhere, instead of re-reading every
diff by hand.

Each rule ships with a `*.test.py` file holding lines annotated `# ruleid:` (must
match) and `# ok:` (must not), which is how Semgrep tests rules.

| Rule | Catches |
| --- | --- |
| `python.ssrf-allowlist-prefix` | A URL allowlist written as `.startswith(...)` instead of a parsed-host check |
| `python.jwt-alg-from-header` | A JWT verifier that branches on the header `alg` the client controls |
| `python.requests-no-timeout` | `requests` calls with no timeout, which hang a worker and enable slow DoS |

## Run

```bash
pip install semgrep
semgrep --config rules/ rules/
```

## Test the rules themselves

```bash
semgrep --test rules/
```

## Scope

These rules are heuristics. They raise findings to review, not proof of a bug,
and a clean run does not mean the code is safe. Tune them to your codebase before
you rely on them in CI.

## License

[MIT](LICENSE)
