# Install

Following packages are needed on debian to successfully install the library

```bash
sudo apt-get install libxml2-dev libxslt-dev
```

Sync dependencias

```bash
uv sync --all-groups
```

`Playwright`, browser automation tool, needs a `Chromium` browser binary to run

```bash
uv run playwright install chromium
```