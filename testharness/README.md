# Test Harness

A standalone project for manually exercising the `dnv_windfarmer_sdk` against a real WindFarmer Services API instance.

[main.py](main.py) authenticates using a bearer token, calls the API status endpoint, then runs an AEP calculation using the sample data in [data/](data).

## Running

Set the `WINDFARMER_ACCESS_KEY` environment variable to a valid access token, then run:

```bash
uv run main.py
```
