# 🟠 GeekBridge

### Connect Languages. Bridge Ideas. Work Smarter.

GeekBridge is a modular Windows desktop toolkit for Persian/Arabic text shaping and multilingual translation. Built with Python and PySide6.

> **Status:** Early development. This repository contains a prototype, not a stable production release.

## Current capabilities

- PySide6 desktop GUI with dark theme and GK identity
- Persian/Arabic glyph shaping using `arabic-reshaper`
- Optional BiDi visual-order conversion (off by default)
- LibreTranslate online provider
- DeepL online provider (requires your own API key)
- Argos Translate offline adapter (optional package and local language models required)
- Background translation worker
- Clipboard copy/paste
- Windows packaging script and GitHub Actions workflow

## Persian text shaping

Text shaping and bidirectional reordering are separate operations:

- **Shape only (default):** converts Arabic-script characters to connected presentation forms while keeping logical character order.
- **BiDi reorder (advanced):** optionally changes visual order for applications that require it.

The correct mode depends on the target application. Test on a copy of important documents.

## Installation

Requirements: Windows 10/11 and Python 3.10+.

```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -e .
py -m geekbridge
```

Optional offline translation dependency:

```powershell
py -m pip install -e ".[offline]"
```

Argos language-pair models must also be installed locally.

## Translation providers

- **LibreTranslate:** configure a reachable endpoint. Public endpoints may impose rate limits, restrictions, or API-key requirements.
- **DeepL:** provide your own API key and select the correct Free or Pro endpoint.
- **Argos Translate:** local translation after installing the runtime and required language models.

Online translation sends submitted text to the selected provider. Do not send confidential text to public translation services. API keys in this prototype are session-only.

## Build a Windows EXE

On Windows, run `scripts/build_windows.bat`. Expected output: `dist/GeekBridge.exe`.

### GitHub Actions

1. Push the source to GitHub.
2. Open **Actions**.
3. Select **Build GeekBridge for Windows**.
4. Select **Run workflow**.
5. Download the `GeekBridge-Windows-x64` artifact after a successful run.

The workflow artifact is an executable build, not a signed installer.

## Development

```powershell
py -m pip install -e ".[dev]"
py -m pytest
py -m ruff check src tests
```

## Roadmap

- [x] Modular application foundation
- [x] Initial PySide6 desktop shell
- [x] Persian/Arabic glyph shaping
- [x] Optional BiDi processing
- [x] LibreTranslate, DeepL and Argos provider adapters
- [x] Background translation worker
- [x] Initial Windows build workflow
- [ ] Complete Persian/English localization and RTL/LTR layout switching
- [ ] Automated tests against target applications
- [ ] Secure API-key storage using Windows Credential Manager
- [ ] Argos language-model management UI
- [ ] Global clipboard monitoring and hotkeys
- [ ] OCR, AI writing and workflow automation
- [ ] Signed installer and verified stable release

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Never commit API keys, personal documents, clipboard history, or local databases.

## License

MIT. See [LICENSE](LICENSE).
