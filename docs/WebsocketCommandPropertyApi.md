# swagger_client.WebsocketCommandPropertyApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**websocket_command_property_all_by_command_get**](WebsocketCommandPropertyApi.md#websocket_command_property_all_by_command_get) | **GET** /WebsocketCommandProperty/AllByCommand | Retrieves all websocket command properties relevant to its parent command.
[**websocket_command_property_all_get**](WebsocketCommandPropertyApi.md#websocket_command_property_all_get) | **GET** /WebsocketCommandProperty/All | Retrieves all websocket command properties owned by the stated user with a pagination of  1000 items.

# **websocket_command_property_all_by_command_get**
> WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel websocket_command_property_all_by_command_get(command_guid=command_guid, index=index)

Retrieves all websocket command properties relevant to its parent command.

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
api_instance = swagger_client.WebsocketCommandPropertyApi(swagger_client.ApiClient(configuration))
command_guid = 'command_guid_example' # str | The unique identifier of the command. (optional)
index = 0 # int | The 'page' of the list you are viewing, in 1000s. (optional) (default to 0)

try:
    # Retrieves all websocket command properties relevant to its parent command.
    api_response = api_instance.websocket_command_property_all_by_command_get(command_guid=command_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketCommandPropertyApi->websocket_command_property_all_by_command_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_guid** | **str**| The unique identifier of the command. | [optional] 
 **index** | **int**| The &#x27;page&#x27; of the list you are viewing, in 1000s. | [optional] [default to 0]

### Return type

[**WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel**](WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **websocket_command_property_all_get**
> WebsocketCommandPropertyViewModelICollectionPaginatedViewModel websocket_command_property_all_get(index=index)

Retrieves all websocket command properties owned by the stated user with a pagination of  1000 items.

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
api_instance = swagger_client.WebsocketCommandPropertyApi(swagger_client.ApiClient(configuration))
index = 0 # int | The 'page' of the list you are viewing, in 1000s. (optional) (default to 0)

try:
    # Retrieves all websocket command properties owned by the stated user with a pagination of  1000 items.
    api_response = api_instance.websocket_command_property_all_get(index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketCommandPropertyApi->websocket_command_property_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list you are viewing, in 1000s. | [optional] [default to 0]

### Return type

[**WebsocketCommandPropertyViewModelICollectionPaginatedViewModel**](WebsocketCommandPropertyViewModelICollectionPaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

