# Contributing to GeekBridge

Thank you for considering a contribution.

## Development setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -e ".[dev]"
```

## Before submitting a pull request

- Keep core logic independent from the Qt UI.
- Add tests for new features and bug fixes.
- Run `py -m pytest` and `py -m ruff check src tests`.
- Update documentation when user-facing behavior changes.
- Never commit secrets, API keys, personal documents, clipboard contents, or local databases.

## Translation providers

Implement the provider interface, return a `TranslationResult`, and raise `TranslationError` for provider failures. Never hard-code credentials.

## Pull requests

Use a focused branch and explain the motivation, implementation, and how the change was tested.
