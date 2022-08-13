from packages import entity
from packages import variables
from packages import event
from packages import model
from packages import label
from packages import detector
from packages import outcome
from packages import rules
from packages import prediction

##===Starting the services
# Step 1 Create entity
# entity.create_entity('customer','sample customer entity type')
# Step 2 Create event variables
# variables.create_variables()
# Step 3 create label
# label.create_label('legit','label for legitimate events')
# label.create_label('fraud','label for fraud events')
# step 4 create event type
# event.create_event()
# step 5 import training dataset to AmazonFraudDetector
# event.upload_event_data('batch_import_training_dataset')
# event.batch_import_status('batch_import_training_dataset')

#step 6 create model

# model.createmodel()
#step 7 Train model
# model.train_model()
# Check training status
# model.get_model_version()
#step 8 deploy model
# model.activate_model()
# model.get_model_version()

#step 9 create detector
# detector.create_detector()

#step 10 Create outcome
# outcome.create_outcome()

#step 11 Create rules
# rules.create_rule()


#step 12 create detector version
# detector.create_detector_version()

#step 13 update detector version status
# detector.update_detector_version_status()




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



# First fraud_prediction
# prediction.payment_transaction()
