# dnv_windfarmer_client.AnnualEnergyProductionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annual_energy_production_post**](AnnualEnergyProductionApi.md#annual_energy_production_post) | **POST** /AnnualEnergyProduction | Gets the energy calculation result for the given inputs.


# **annual_energy_production_post**
> AnnualEnergyProductionResults annual_energy_production_post(energy_calculation_inputs)

Gets the energy calculation result for the given inputs.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.annual_energy_production_results import AnnualEnergyProductionResults
from dnv_windfarmer_client.models.energy_calculation_inputs import EnergyCalculationInputs
from dnv_windfarmer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dnv_windfarmer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = dnv_windfarmer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dnv_windfarmer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnv_windfarmer_client.AnnualEnergyProductionApi(api_client)
    energy_calculation_inputs = dnv_windfarmer_client.EnergyCalculationInputs() # EnergyCalculationInputs | Energy efficiencies calculation inputs.

    try:
        # Gets the energy calculation result for the given inputs.
        api_response = api_instance.annual_energy_production_post(energy_calculation_inputs)
        print("The response of AnnualEnergyProductionApi->annual_energy_production_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnualEnergyProductionApi->annual_energy_production_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **energy_calculation_inputs** | [**EnergyCalculationInputs**](EnergyCalculationInputs.md)| Energy efficiencies calculation inputs. | 

### Return type

[**AnnualEnergyProductionResults**](AnnualEnergyProductionResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calculation results were retrieved successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

