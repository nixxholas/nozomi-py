# swagger_client.WebsocketCommandApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**websocket_command_all_by_request_get**](WebsocketCommandApi.md#websocket_command_all_by_request_get) | **GET** /WebsocketCommand/AllByRequest | Obtain all of the websocket commands created, relative to the request.
[**websocket_command_all_get**](WebsocketCommandApi.md#websocket_command_all_get) | **GET** /WebsocketCommand/All | Obtain all websocket commands you have created/own.

# **websocket_command_all_by_request_get**
> WebsocketCommandViewModelICollectionPaginatedViewModel websocket_command_all_by_request_get(request_guid=request_guid, index=index)

Obtain all of the websocket commands created, relative to the request.

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
api_instance = swagger_client.WebsocketCommandApi(swagger_client.ApiClient(configuration))
request_guid = 'request_guid_example' # str | The unique identifier of the request. (optional)
index = 0 # int | The 'page' of the list of results in 100s. (optional) (default to 0)

try:
    # Obtain all of the websocket commands created, relative to the request.
    api_response = api_instance.websocket_command_all_by_request_get(request_guid=request_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketCommandApi->websocket_command_all_by_request_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_guid** | **str**| The unique identifier of the request. | [optional] 
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s. | [optional] [default to 0]

### Return type

[**WebsocketCommandViewModelICollectionPaginatedViewModel**](WebsocketCommandViewModelICollectionPaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **websocket_command_all_get**
> WebsocketCommandViewModelIEnumerablePaginatedViewModel websocket_command_all_get(index=index)

Obtain all websocket commands you have created/own.

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
api_instance = swagger_client.WebsocketCommandApi(swagger_client.ApiClient(configuration))
index = 0 # int | The 'page' of the list of results in 100s. (optional) (default to 0)

try:
    # Obtain all websocket commands you have created/own.
    api_response = api_instance.websocket_command_all_get(index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketCommandApi->websocket_command_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s. | [optional] [default to 0]

### Return type

[**WebsocketCommandViewModelIEnumerablePaginatedViewModel**](WebsocketCommandViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

