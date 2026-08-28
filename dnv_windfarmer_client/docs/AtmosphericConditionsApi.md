# dnv_windfarmer_client.AtmosphericConditionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**atmospheric_conditions_get**](AtmosphericConditionsApi.md#atmospheric_conditions_get) | **GET** /AtmosphericConditions | Performs comprehensive site classification and returns atmospheric condition data compatible with WindFarmer.Calculations.DataModel for flow modeling applications. Includes atmospheric stability weights derived from ERA5 data and vertical profiles.


# **atmospheric_conditions_get**
> ComprehensiveSiteClassification atmospheric_conditions_get(lat=lat, lon=lon, radius=radius, land_fraction_threshold=land_fraction_threshold)

Performs comprehensive site classification and returns atmospheric condition data compatible with WindFarmer.Calculations.DataModel for flow modeling applications. Includes atmospheric stability weights derived from ERA5 data and vertical profiles.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.comprehensive_site_classification import ComprehensiveSiteClassification
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
    api_instance = dnv_windfarmer_client.AtmosphericConditionsApi(api_client)
    lat = 3.4 # float | Latitude of the site in decimal degrees (-85 to 85) (optional)
    lon = 3.4 # float | Longitude of the site in decimal degrees (-180 to 180) (optional)
    radius = 3.4 # float | Analysis radius in kilometers (0-100, default: 50.0) (optional)
    land_fraction_threshold = 3.4 # float | Threshold for land classification (0.0-1.0, default: 0.2) (optional)

    try:
        # Performs comprehensive site classification and returns atmospheric condition data compatible with WindFarmer.Calculations.DataModel for flow modeling applications. Includes atmospheric stability weights derived from ERA5 data and vertical profiles.
        api_response = api_instance.atmospheric_conditions_get(lat=lat, lon=lon, radius=radius, land_fraction_threshold=land_fraction_threshold)
        print("The response of AtmosphericConditionsApi->atmospheric_conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtmosphericConditionsApi->atmospheric_conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude of the site in decimal degrees (-85 to 85) | [optional] 
 **lon** | **float**| Longitude of the site in decimal degrees (-180 to 180) | [optional] 
 **radius** | **float**| Analysis radius in kilometers (0-100, default: 50.0) | [optional] 
 **land_fraction_threshold** | **float**| Threshold for land classification (0.0-1.0, default: 0.2) | [optional] 

### Return type

[**ComprehensiveSiteClassification**](ComprehensiveSiteClassification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comprehensive site classification with atmospheric conditions and metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

