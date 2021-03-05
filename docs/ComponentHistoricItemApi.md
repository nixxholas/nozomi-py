# swagger_client.ComponentHistoricItemApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**component_historic_item_all_component_guid_get**](ComponentHistoricItemApi.md#component_historic_item_all_component_guid_get) | **GET** /ComponentHistoricItem/All/{componentGuid} | Obtain all the component historical values created

# **component_historic_item_all_component_guid_get**
> ComponentHistoricItemViewModelIEnumerablePaginatedViewModel component_historic_item_all_component_guid_get(component_guid, index=index)

Obtain all the component historical values created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ComponentHistoricItemApi(swagger_client.ApiClient(configuration))
component_guid = 'component_guid_example' # str | The unique identifier of the component.
index = 0 # int | The 'page' of the list of results in 100s. (optional) (default to 0)

try:
    # Obtain all the component historical values created
    api_response = api_instance.component_historic_item_all_component_guid_get(component_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentHistoricItemApi->component_historic_item_all_component_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_guid** | **str**| The unique identifier of the component. | 
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s. | [optional] [default to 0]

### Return type

[**ComponentHistoricItemViewModelIEnumerablePaginatedViewModel**](ComponentHistoricItemViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

