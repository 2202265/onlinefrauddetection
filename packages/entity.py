import boto3
fraudDetector = boto3.client('frauddetector')

def create_entity(entity_name,entity_description):
    fraudDetector.put_entity_type(name = entity_name,description = entity_description)

def delete_entity(entity_name):
    fraudDetector.delete_entity_type(name=entity_name)
