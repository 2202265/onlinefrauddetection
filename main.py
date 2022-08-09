from packages import entity
from packages import variables
from packages import event
from packages import model
from packages import label
from packages import detector
from packages import outcome
from packages import rules

# Step 1 Create entity
#entity.create_entity()
# Step 2 Create event variables
#variables.create_variables()
# Step 3 create label
#label.create_label_fraud()
#label.create_label_legit()
# step 4 create event type
#event.create_event()
#step 5 import dataset to AmazonFraudDetector
#event.upload_event_data()

#step 6 create model

#createmodel.createmodel()
#step 7 Train model
#trainmodel.train_model()

#step 8 deploy model
#trainmodel.activate_model()

#step 9 create detector
#detector.create_detector()

#step 10 Create outcome
#outcome.create_outcome()

#step 11 Create rules
#rules.create_rule()


#step 12 create detector version
#detector.create_detector_version()

#step 13 update detector version status
#detector.update_detector_version_status()




##================ Stopping the Services
#detector.update_detector_version_status('DRAFT')
#detector.delete_detector_version('online_transaction','1')
# rules.delete_rule('online_transaction', 'approve_rule', '1')
# rules.delete_rule('online_transaction', 'decline_rule', '1')
# rules.delete_rule('online_transaction', 'friction_rule', '1')
# detector.delete_detector('online_transaction')
# Undeploying the model - may take some time to finish
#model.update_model_version_status('transaction_model','TRANSACTION_FRAUD_INSIGHTS','1.0','INACTIVE')
# Check the status whether model is inactive
#model.get_model_version()
#model.delete_model_version('transaction_model','TRANSACTION_FRAUD_INSIGHTS','1.0')
 # delete model version
# model.delete_model('transaction_model','TRANSACTION_FRAUD_INSIGHTS')



#event.delete_event_job_data('batch_import') # delete store event job
# event.delete_event_type('transaction_event') # delete event
# event.delete_event_status('transaction_event') # check the deletion status
# event.delete_event('transaction_event')
# entity.delete_entity('customer') #delete the entity customer
# label.delete_label('fraud') #delete the  labels ,legit/fraud
# label.delete_label('legit')
# variables.delete_variables() #delete variables
# outcome.delete_outcome('approve')
# outcome.delete_outcome('block')
# outcome.delete_outcome('investigate')
