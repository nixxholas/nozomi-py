# swagger_client.ComputeValueApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_value_all_index_get**](ComputeValueApi.md#compute_value_all_index_get) | **GET** /ComputeValue/All/{index} | Obtain all compute value generated.
[**compute_value_get_guid_get**](ComputeValueApi.md#compute_value_get_guid_get) | **GET** /ComputeValue/Get/{guid} | Obtain the compute value specified.
[**compute_value_last_compute_guid_get**](ComputeValueApi.md#compute_value_last_compute_guid_get) | **GET** /ComputeValue/Last/{computeGuid} | Obtain the last compute value of the compute in question.

# **compute_value_all_index_get**
> ComputeValueViewModelIEnumerablePaginatedViewModel compute_value_all_index_get(index, compute_guid=compute_guid)

Obtain all compute value generated.

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
api_instance = swagger_client.ComputeValueApi(swagger_client.ApiClient(configuration))
index = 56 # int | The 'page' of the list of results in x
compute_guid = 'compute_guid_example' # str | The compute guid relating to the values in question, optional. (optional)

try:
    # Obtain all compute value generated.
    api_response = api_instance.compute_value_all_index_get(index, compute_guid=compute_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeValueApi->compute_value_all_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results in x | 
 **compute_guid** | **str**| The compute guid relating to the values in question, optional. | [optional] 

### Return type

[**ComputeValueViewModelIEnumerablePaginatedViewModel**](ComputeValueViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_value_get_guid_get**
> ComputeValueViewModel compute_value_get_guid_get(guid)

Obtain the compute value specified.

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
api_instance = swagger_client.ComputeValueApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid of the compute value in question.

try:
    # Obtain the compute value specified.
    api_response = api_instance.compute_value_get_guid_get(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeValueApi->compute_value_get_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid of the compute value in question. | 

### Return type

[**ComputeValueViewModel**](ComputeValueViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_value_last_compute_guid_get**
> ComputeValueViewModel compute_value_last_compute_guid_get(compute_guid)

Obtain the last compute value of the compute in question.

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
api_instance = swagger_client.ComputeValueApi(swagger_client.ApiClient(configuration))
compute_guid = 'compute_guid_example' # str | The compute in question.

try:
    # Obtain the last compute value of the compute in question.
    api_response = api_instance.compute_value_last_compute_guid_get(compute_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeValueApi->compute_value_last_compute_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_guid** | **str**| The compute in question. | 

### Return type

[**ComputeValueViewModel**](ComputeValueViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

