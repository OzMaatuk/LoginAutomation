# Login Automation Framework

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/python/)
[![CI](https://github.com/yourusername/login_automation/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/login_automation/actions/workflows/ci.yml)

A clean, modular, and extensible **Playwright-based** login automation framework in Python — perfect for LinkedIn, manual 2FA handling, and easy to extend to any site.

## Features

- Factory pattern — add new platforms in minutes
- Full configuration via `config.ini` or `.env`
- Headless & headed mode support
- Smart persistent context (reuse cookies/sessions)
- Robust error handling & logging
- Manual login mode (great for CAPTCHA/2FA)
- 100% tested with `pytest`
- GitHub Actions CI ready

## Supported Platforms

| Platform  | Status          | Notes                          |
|---------|-----------------|--------------------------------|
| LinkedIn| Fully working   | Automatic login                |
| Manual  | Working         | 2-minute window for manual login |
| Others  | Ready to add    | Just follow the pattern       |

## Project Structure

```
login_automation/
├── config.py                  # Config + env loading
├── driver.py                  # Playwright driver wrapper
├── logger.py                  # Centralized logging
├── main.py                    # Entry point
├── login/
│   ├── factory.py             # Platform factory
│   ├── login.py               # Base Login class
│   ├── linkedin.py
│   └── manual.py
├── constants/
│   ├── constants.py
│   └── linkedin.py
└── tests/                     # Comprehensive test suite
```

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/login_automation.git
cd login_automation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

```bash
playwright install
```

### 3. Set Your Credentials (Securely)

Create a `.env` file in the root:

```env
USERNAME=your_email@domain.com
PASSWORD=your_very_secure_password
```

Never commit real credentials!

### 4. Run

```bash
python main.py
```

For CAPTCHA or 2FA → switch to manual mode in `config.ini`:

```ini
[general]
platform = manual
```

You’ll get **2 minutes** to log in manually in the opened browser.

## Adding a New Platform (e.g. Twitter, Facebook)

1. Create `login_automation/constants/twitter.py` → `ConstantsTwitter`
2. Create `login_automation/login/twitter.py` → `LoginTwitter`
3. Add to `SUPPORTED_PLATFORMS` in `constants.py`

Done. The factory auto-discovers it.

## Testing

```bash
pytest -v
```

All edge cases covered: timeouts, bad credentials, factory errors, manual mode, etc.

## GitHub Actions

Automated testing on **Python 3.9 → 3.12** on every push/PR.

## How to Release a New Version
* Update version in pyproject.toml → e.g. version = "0.2.0"
* Commit + push
* Go to GitHub → Releases → Draft a new release → Tag v0.2.0 → Publish

## Security Best Practices

- `.env` is in `.gitignore`
- Never hardcode passwords
- Use persistent context only locally (not in CI)

## License

MIT © 2025

---
Made with love for automation addicts
