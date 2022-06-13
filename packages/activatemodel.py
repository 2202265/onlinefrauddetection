import boto3
fraudDetector = boto3.client('frauddetector')

def activate_model():
    fraudDetector.update_model_version_status (
    modelId = 'transaction_model',
    modelType = 'TRANSACTION_FRAUD_INSIGHTS',
    modelVersionNumber = '1.0',
    status = 'ACTIVE'
    )
