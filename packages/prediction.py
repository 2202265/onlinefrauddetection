import boto3
fraudDetector = boto3.client('frauddetector')
response = fraudDetector.get_event_prediction(
detectorId='transaction_fraud_detector',
detectorVersionId='1',
eventId='35624089d931246b127c7d3321a2c39d95',
eventTypeName='transaction_event',
entities=[
{
'entityType': 'customer',
'entityId': '004-12-3461'
},
],
eventTimestamp='2022-01-12T03:53:34Z',
eventVariables={
'customer_email': 'sarin123@hotmail.com',
'order_price': '89.55',
'billing_city':'New Market',
'product_category':'grocery_pos',
'billing_street':'121 Joseph Forge',
'user_agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/46.0.847.0 Safari/535.2',
'ip_address':'71.92.210.40',
'card_bin':'495601',
'billing_zip':'22844'
}
)
print(response)
