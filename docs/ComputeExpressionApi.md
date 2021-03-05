# swagger_client.ComputeExpressionApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_expression_all_index_get**](ComputeExpressionApi.md#compute_expression_all_index_get) | **GET** /ComputeExpression/All/{index} | Obtains all of the relevant compute expressions you own.
[**compute_expression_get_guid_get**](ComputeExpressionApi.md#compute_expression_get_guid_get) | **GET** /ComputeExpression/Get/{guid} | Obtains the specific compute expression.

# **compute_expression_all_index_get**
> ComputeExpressionViewModelIEnumerablePaginatedViewModel compute_expression_all_index_get(index, compute_guid=compute_guid)

Obtains all of the relevant compute expressions you own.

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
api_instance = swagger_client.ComputeExpressionApi(swagger_client.ApiClient(configuration))
index = 56 # int | The 'page' of the list of results of every x items.
compute_guid = 'compute_guid_example' # str | Filter by the compute if needed. (optional)

try:
    # Obtains all of the relevant compute expressions you own.
    api_response = api_instance.compute_expression_all_index_get(index, compute_guid=compute_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeExpressionApi->compute_expression_all_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | 
 **compute_guid** | **str**| Filter by the compute if needed. | [optional] 

### Return type

[**ComputeExpressionViewModelIEnumerablePaginatedViewModel**](ComputeExpressionViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_expression_get_guid_get**
> ComputeExpressionViewModel compute_expression_get_guid_get(guid)

Obtains the specific compute expression.

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
api_instance = swagger_client.ComputeExpressionApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The Guid of the compute expression in question.

try:
    # Obtains the specific compute expression.
    api_response = api_instance.compute_expression_get_guid_get(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeExpressionApi->compute_expression_get_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The Guid of the compute expression in question. | 

### Return type

[**ComputeExpressionViewModel**](ComputeExpressionViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

