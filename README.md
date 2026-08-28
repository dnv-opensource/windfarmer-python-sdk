# WindFarmer Python SDK

Python tooling for calling the WindFarmer Services API.

## Repo layout

- [openapi-specs/](openapi-specs) — OpenAPI spec(s) for the WindFarmer Services API.
- [dnv_windfarmer_client/](dnv_windfarmer_client) — Low-level API client and models. **Generated code, do not edit by hand** (see below).
- [dnv_windfarmer_sdk/](dnv_windfarmer_sdk) — Hand-written SDK that wraps the generated client with a friendlier API.
- [testharness/](testharness) — A small standalone project for manually exercising the SDK against a real API.

## Prerequisites

This repo uses [`uv`](https://docs.astral.sh/uv/) for Python packaging, dependency management and virtual environments. Install it by following the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/), then see the [uv guide to projects](https://docs.astral.sh/uv/guides/projects/) for an overview of common commands (`uv sync`, `uv run`, `uv add`, etc.).

Generating the API client also requires [Docker](https://docs.docker.com/get-docker/) to be installed and running.

## Generating the API client

The [dnv_windfarmer_client/](dnv_windfarmer_client) package is generated from the OpenAPI spec using [openapi-generator](https://openapi-generator.tech/) and should not be edited directly — any manual changes will be lost the next time it is regenerated.

To (re)generate it, run one of the generator scripts from the repo root:

```bash
./generate_client.sh      # Linux/macOS
```

```powershell
./generate_client.ps1     # Windows/PowerShell
```

Both scripts run the `openapi-generator-cli` Docker image against [openapi-specs/wfservices-final.json](openapi-specs/wfservices-final.json) and write the generated code into [dnv_windfarmer_client/](dnv_windfarmer_client).

## Trying it out

[testharness/main.py](testharness/main.py) contains a small demo that calls the API status endpoint and runs an AEP calculation using sample data.

Create an environment variable called `WINDFARMER_ACCESS_KEY`, containing your API key from [the DNV Renewables Services portal](https://renewablesservices.dnv.com/).

```bash
cd testharness
uv run main.py
```

## Building the packages

Both packages are built with `uv build`, which produces a wheel and sdist in a `dist/` folder for each package.

### Bash on Linux
```bash
./generate_client.sh                 # (re)generate dnv_windfarmer_client — see above
cd dnv_windfarmer_client && uv build && cd ..
cd dnv_windfarmer_sdk && uv build && cd ..
```

### Powershell on Windows
```powershell
.\generate_client.ps1                # (re)generate dnv_windfarmer_client — see above
Push-Location dnv_windfarmer_client; uv build; Pop-Location
Push-Location dnv_windfarmer_sdk; uv build; Pop-Location
```
