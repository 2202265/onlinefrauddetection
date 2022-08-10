import boto3
fraudDetector = boto3.client('frauddetector')


response = fraudDetector.get_event_prediction(
detectorId='transaction_fraud_detector',
detectorVersionId='1',
eventId='32b7f7d1513fb4b2d5ed459ddc81fd06b9',
eventTypeName='transaction_event',
entities=[
{
'entityType': 'customer',
'entityId': '373-82-4202'
},
],
eventTimestamp='2021-12-25T02:22:51Z',
eventVariables={
'customer_email': 'navarropamela@powell.com',
'order_price': '308.45',
'payment_currency': 'INR',
'billing_city':'Sneads Ferry'
}
)
print(response)
