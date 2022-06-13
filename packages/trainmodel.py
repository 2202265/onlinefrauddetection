import boto3
fraudDetector = boto3.client('frauddetector')


def train_model():
    response = fraudDetector.create_model_version (
    modelId = 'transaction_model',
    modelType = 'TRANSACTION_FRAUD_INSIGHTS',
    trainingDataSource = 'INGESTED_EVENTS',
    trainingDataSchema = {
    'modelVariables' : ['card_bin','customer_name','billing_street','billing_city','billing_state','billing_zip',
    'billing_latitude','billing_longitude','customer_job','ip_address','customer_email','phone','user_agent',
    'product_category','order_price','payment_currency','merchant'],
    'labelSchema' : {
    'labelMapper' : {
    'FRAUD' : ['fraud'],
    'LEGIT' : ['legit']
    },
    'unlabeledEventsTreatment': 'IGNORE'
    }
    },
    ingestedEventsDetail={
    'ingestedEventsTimeWindow': {
    'startTime': '2021-11-01T00:00:00Z',
    'endTime': '2022-02-28T00:00:00Z'
    }
    }
    )
    print(response)

def get_model_version():
    response = fraudDetector.get_model_version(
    modelId='transaction_model',
    modelType='TRANSACTION_FRAUD_INSIGHTS',
    modelVersionNumber='1.0')
    print(response)

def activate_model():
    fraudDetector.update_model_version_status (
    modelId = 'transaction_model',
    modelType = 'TRANSACTION_FRAUD_INSIGHTS',
    modelVersionNumber = '1.0',
    status = 'ACTIVE')
