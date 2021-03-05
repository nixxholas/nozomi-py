# CreateRequestInputModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**request_type** | [**RequestType**](RequestType.md) |  | [optional] 
**response_type** | [**ResponseType**](ResponseType.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**delay** | **int** |  | [optional] 
**failure_delay** | **int** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**components** | [**list[CreateComponentInputModel]**](CreateComponentInputModel.md) |  | [optional] 
**properties** | [**list[CreateRequestPropertyInputModel]**](CreateRequestPropertyInputModel.md) |  | [optional] 
**items** | [**list[CreateItemRequestInputModel]**](CreateItemRequestInputModel.md) |  | [optional] 
**websocket_commands** | [**list[CreateWebsocketCommandInputModel]**](CreateWebsocketCommandInputModel.md) |  | [optional] 
**socket_data_count** | **int** |  | [optional] 
**socket_kill_switch_delay** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

