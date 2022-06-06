import boto3
fraudDetector = boto3.client('frauddetector')

def createmodel():
    fraudDetector.create_model (
    modelId = 'transaction_model',
    eventTypeName = 'transaction_event',
    modelType = 'TRANSACTION_FRAUD_INSIGHTS',
    description= 'Model for fraud detection of online transaction')
