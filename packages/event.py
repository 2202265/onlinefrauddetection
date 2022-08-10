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

def upload_event_data(job_id):
    fraudDetector.create_batch_import_job (
    jobId = job_id,
    inputPath = 's3://dataset-onlinetransaction/transaction_data.csv',
    outputPath = 's3://dataset-onlinetransaction/',
    eventTypeName = 'transaction_event',
    iamRoleArn = 'arn:aws:iam::163076715085:role/service-role/AmazonFraudDetector-DataAccessRole-1654473179346'
    )
def batch_import_status(job_id):
    response = fraudDetector.get_batch_import_jobs(
    jobId=job_id,
    maxResults=10,
    nextToken='')
    print(response)

def delete_event(event_name):
    fraudDetector.delete_event_type(name=event_name)

def delete_event_type(event_name):
    fraudDetector.delete_events_by_event_type(eventTypeName=event_name)

def delete_event_status(event_name):
    response = fraudDetector.get_delete_events_by_event_type_status(eventTypeName=event_name)
    print(response)

def delete_event_job_data(job_id):
    fraudDetector.delete_batch_import_job(jobId=job_id)
