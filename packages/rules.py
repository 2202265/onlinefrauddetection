import boto3
fraudDetector = boto3.client('frauddetector')

def create_rule():
    fraudDetector.create_rule(
    ruleId = 'decline_rule',
    detectorId = 'online_transaction',
    description='block transaction when the score is 950 or above',
    expression = '$transaction_model_insightscore >= 950',
    language = 'DETECTORPL',
    outcomes = ['block']
    )
    fraudDetector.create_rule(
    ruleId = 'friction_rule',
    detectorId = 'online_transaction',
    description='Review the transaction when the score is 855 or above and below 950',
    expression = '$transaction_model_insightscore >= 855 and $transaction_model_insightscore < 950',
    language = 'DETECTORPL',
    outcomes = ['investigate']
    )
    fraudDetector.create_rule(
    ruleId = 'approve_rule',
    detectorId = 'online_transaction',
    description='approve transaction when the score is below 855',
    expression = '$transaction_model_insightscore < 855',
    language = 'DETECTORPL',
    outcomes = ['approve']
    )

def delete_rule(detector_id,rule_id,version_id):
    fraudDetector.delete_rule(
    rule={
        'detectorId': detector_id,
        'ruleId': rule_id,
        'ruleVersion': version_id
    }
    )
