import boto3
fraudDetector = boto3.client('frauddetector')

def create_outcome():

    fraudDetector.put_outcome(
    name = 'block',
    description = 'block the transaction'
    )
    fraudDetector.put_outcome(
    name = 'investigate',
    description = 'this outcome sidelines event for review'
    )
    fraudDetector.put_outcome(
    name = 'approve',
    description = 'this outcome approves the event'
    )

def delete_outcome(outcome_name):
    fraudDetector.delete_outcome(name=outcome_name)
