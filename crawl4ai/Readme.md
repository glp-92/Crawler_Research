# Instalacion

Los siguientes paquetes son requeridos por debian para poder instalar con exito la libreria

```bash
sudo apt-get install libxml2-dev libxslt-dev
```

Instalar todas las dependencias

```bash
uv sync --all-groups
```

`Playwright`, la utilidad de automatizacion para navegador, necesita los binarios de `Chromium` para ejecutarse

```bash
uv run playwright install chromium
```