# CfdmlBlockageSettings

The CFD.ML blockage model settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cfdml_settings** | [**Cfdml**](Cfdml.md) | The CFD.ML model settings | 
**include_intermediate_results** | **bool** | Gets or sets whether to include intermediate result data or not. | [optional] [default to False]
**blockage_correction_application_method** | [**BlockageCorrectionApplicationMethod**](BlockageCorrectionApplicationMethod.md) | Setting to specify whether to apply blockage correction on wind speed or on energy. Default value: OnEnergy.  Note: if includeBlockage &#x3D;&#x3D; False this settings is ignored. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.cfdml_blockage_settings import CfdmlBlockageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CfdmlBlockageSettings from a JSON string
cfdml_blockage_settings_instance = CfdmlBlockageSettings.from_json(json)
# print the JSON string representation of the object
print(CfdmlBlockageSettings.to_json())

# convert the object into a dict
cfdml_blockage_settings_dict = cfdml_blockage_settings_instance.to_dict()
# create an instance of CfdmlBlockageSettings from a dict
cfdml_blockage_settings_from_dict = CfdmlBlockageSettings.from_dict(cfdml_blockage_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


