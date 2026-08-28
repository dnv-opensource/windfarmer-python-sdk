# dnv_windfarmer_sdk

A Python SDK for the [WindFarmer Services API](https://windfarmer.dnv.com/), providing a friendly interface on top of the lower-level generated `dnv-windfarmer-client` package.

The SDK takes care of things the low-level client doesn't do for you, such as:

- Submitting Annual Energy Production (AEP) calculations asynchronously and polling for completion.
- Automatically fetching atmospheric conditions and attaching them to the calculation inputs when required (CFD.ML v2).
- Reporting calculation progress via a progress bar.

## Installation

```bash
pip install dnv_windfarmer_sdk
```

## Authentication

All API calls require an access token. Obtain one from [https://renewablesservices.dnv.com/](https://renewablesservices.dnv.com/) and keep it out of source control — for example, by loading it from an environment variable:

### Bash
```bash
export WINDFARMER_ACCESS_KEY=<your token>
```

### Powershell
```powershell
$env:WINDFARMER_ACCESS_KEY=<your token>
```

## Quick start

```python
import os

import windfarmer as wf
from dnv_windfarmer_client import EnergyCalculationInputs

# Check the API is up and see which versions are deployed
status = wf.status()
print(status.wind_farmer_services_api_version, status.calculation_library_version)

# Build (or load/deserialize) your calculation inputs
energy_calculation_inputs = EnergyCalculationInputs.from_dict({...})

# Run an AEP calculation and wait for the results
aep_results = wf.annual_energy_production(energy_calculation_inputs)

for wind_farm_result in aep_results.wind_farm_aep_outputs:
    print(wind_farm_result.wind_farm_name, wind_farm_result.full_annual_energy_yield_mwh_per_year)
```

By default `WindFarmerApi` targets the production API at `https://windfarmer.dnv.com/api/v3`. To target a different environment, set `windfarmer.API_URL`

```python
wf.API_URL = 'https://windfarmer-dev.example.com/api/v3'
```

## `WindFarmerApi` reference

All methods construct their own client per call, so a single `WindFarmerApi` instance can be reused for multiple requests.

| Method | Description |
| --- | --- |
| `status()` | Returns the deployed API and calculation library versions. |
| `annual_energy_production(inputs)` | Recommended way to run an AEP calculation. Submits asynchronously, polls until complete, and returns the `AnnualEnergyProductionResults`. Automatically fetches atmospheric conditions first if the inputs use CFD.ML v2. |
| `annual_energy_production_sync(inputs)` | Runs an AEP calculation on the synchronous endpoint and returns the results directly. Only suitable for small/quick calculations, as the request may time out for larger wind farms. |
| `annual_energy_production_async(inputs)` | Submits an AEP calculation to the async endpoint and returns a `CalculationQueuedResult` (job ID) without waiting for completion. |
| `atmospheric_conditions(latitude, longitude, radius_km=50.0, land_fraction_threshold=0.2)` | Returns the `ComprehensiveSiteClassification` (atmospheric conditions) for a location, used to configure CFD.ML v2 calculations. |

### Calculation inputs and results types

The `EnergyCalculationInputs` and result types used by these methods are defined in the `dnv-windfarmer-client` package, which is installed automatically as a dependency. They can be built directly or deserialized from JSON via `from_dict`/`from_json`, as shown above.

### Error handling

Failed calculations raise `dnv_windfarmer_client.ApiException`. Underlying HTTP/client errors from individual API calls are currently logged to stdout rather than raised — wrap calls in a `try`/`except ApiException` block if you need to handle failures programmatically.
