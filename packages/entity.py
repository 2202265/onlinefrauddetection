import boto3
fraudDetector = boto3.client('frauddetector')

def create_entity():
    fraudDetector.put_entity_type(name = 'customer',description = 'sample customer entity type')

def delete_entity():
    fraudDetector.delete_entity_type(name='customer')
