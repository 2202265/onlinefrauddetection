from packages import entity
from packages import variables
from packages import event
from packages import createmodel
from packages import trainmodel


import boto3
fraudDetector = boto3.client('frauddetector')

response = fraudDetector.get_detectors()
print(response)
