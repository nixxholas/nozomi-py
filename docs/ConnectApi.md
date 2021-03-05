# swagger_client.ConnectApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_validate_head**](ConnectApi.md#connect_validate_head) | **HEAD** /Connect/Validate | Allows the client to validate his API key.

# **connect_validate_head**
> str connect_validate_head()

Allows the client to validate his API key.

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
api_instance = swagger_client.ConnectApi(swagger_client.ApiClient(configuration))

try:
    # Allows the client to validate his API key.
    api_response = api_instance.connect_validate_head()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectApi->connect_validate_head: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

