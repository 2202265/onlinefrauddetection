import boto3
fraudDetector = boto3.client('frauddetector')


def create_detector():
    fraudDetector.put_detector (
    detectorId = 'transaction_fraud_detector',
    description='fraud detection of online transaction',
    eventTypeName = 'transaction_event')

def delete_detector(detector_id):
    fraudDetector.delete_detector(
    detectorId=detector_id
    )

def create_detector_version():
    fraudDetector.create_detector_version(
    detectorId='transaction_fraud_detector',
    description='Fraud detector for online transaction',
    rules=[
        {
            'detectorId': 'transaction_fraud_detector',
            'ruleId': 'decline_rule',
            'ruleVersion': '1'
        },
        {
            'detectorId' : 'transaction_fraud_detector',
            'ruleId' : 'friction_rule',
            'ruleVersion' : '1'
        },
        {
            'detectorId' : 'transaction_fraud_detector',
            'ruleId' : 'approve_rule',
            'ruleVersion' : '1'
        }
    ],
    modelVersions=[
        {
            'modelId': 'transaction_model',
            'modelType': 'TRANSACTION_FRAUD_INSIGHTS',
            'modelVersionNumber': '1.0',
            'arn': 'arn:aws:frauddetector:eu-west-1:163076715085:model/TRANSACTION_FRAUD_INSIGHTS/transaction_model'
        },
    ],
    ruleExecutionMode='FIRST_MATCHED'
    )

def update_detector_version_status(status_name):
    fraudDetector.update_detector_version_status(
    detectorId='transaction_fraud_detector',
    detectorVersionId='1',
    status=status_name
    )

def delete_detector_version(detector_id,version_id):
    fraudDetector.delete_detector_version(
    detectorId=detector_id,
    detectorVersionId=version_id
    )
