# core-audit-demo

> Reference consumer for the
> [**CORE Constitutional Audit**](https://github.com/DariuszNewecki/CORE)
> GitHub Action.

This repository exists to demonstrate end-to-end that the CORE audit
gate works against a real external repository — PR annotations land in
the diff view and the action's exit code can drive branch protection.
It is the verification artifact for F-10.4 in the CORE roadmap.

## What the audit checks

The repository copies CORE's `.intent/` directory and inherits CORE's
constitutional ruleset. Every public function and class in `src/` must
carry a `# ID: <uuid>` comment on the line immediately above the
`def`/`class` keyword. The CORE audit catches violations of this rule
(and several dozen others) and surfaces them as inline annotations on
the offending lines.

## How to wire CORE into your own repo (5-minute quickstart)

1. Drop CORE's `.intent/` into your repository's root. (For a truly
   minimal starter constitution see CORE issue #545 — work in progress.)
2. Add `.github/workflows/audit.yml`:
   ```yaml
   name: Constitutional Audit
   on: [push, pull_request]
   jobs:
     audit:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: DariuszNewecki/CORE@main
           with:
             severity: block
   ```
3. (Optional) In your repo settings, require the **Constitutional Audit**
   check on your protected branches. Findings now block merge.

## Running the audit locally

```bash
pip install core-runtime
core-admin code audit --offline --format=text --severity=block
```

Exit code semantics: `0` no findings; `1` findings present; `2`
configuration error; `64` internal error (treat as gate failure).

## License

MIT. See [LICENSE](./LICENSE).
