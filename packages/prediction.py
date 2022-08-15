import boto3
fraudDetector = boto3.client('frauddetector')
response = fraudDetector.get_event_prediction(
detectorId='transaction_fraud_detector',
detectorVersionId='1',
eventId='32a4892528f4a8c57f7c991e91d2aa7b16',
eventTypeName='transaction_event',
entities=[
{
'entityType': 'customer',
'entityId': '174-88-0351'
},
],
eventTimestamp='2021-12-11T14:46:25Z',
eventVariables={
'customer_email': 'iflores@hotmail.com',
'order_price': '105.44',
'billing_city':'Ossian',
'product_category':'grocery_pos',
'billing_street':'4529 Brian Trail Suite 869',
'user_agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)',
'ip_address':'195.181.159.94',
'card_bin':'300361'
}
)
print(response)
