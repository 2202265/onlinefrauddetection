import boto3
fraudDetector = boto3.client('frauddetector')

def create_event():
    fraudDetector.put_event_type (
    name = 'transaction_event', description ='Event for fraud detection of online transaction',
    eventVariables = ['card_bin','customer_name','billing_street','billing_city','billing_state','billing_zip',
    'billing_latitude','billing_longitude','customer_job','ip_address','customer_email','phone','user_agent',
    'product_category','order_price','payment_currency','merchant'],
    labels = ['legit', 'fraud'],
    entityTypes = ['customer'])

def upload_event_data():
    fraudDetector.create_batch_import_job (
    jobId = 'batch_import',
    inputPath = 's3://dataset-onlinetransaction/transaction_data.csv',
    outputPath = 's3://dataset-onlinetransaction/',
    eventTypeName = 'transaction_event',
    iamRoleArn = 'arn:aws:iam::163076715085:role/service-role/AmazonFraudDetector-DataAccessRole-1654473179346'
    )

def delete_event():
    fraudDetector.delete_event_type(name='transaction_event')

def delete_event_status():
    response = fraudDetector.get_delete_events_by_event_type_status(eventTypeName='transaction_event')
    print(response)
