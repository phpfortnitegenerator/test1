import json
import unittest
import rule_code
from botocore.stub import Stubber

from rule_util import aws_config

class TestHandlerCase(unittest.TestCase):

    def setUp(self):
        self.sampleInvokingEvent = {
            'configurationItem': {
                'configuration': {
                    'instanceType': 't2.micro',
                },
                'configurationItemCaptureTime': '2018-01-01T00:00:00.007Z',
                'configurationItemStatus': 'ResourceDiscovered',
                'resourceType': 'AWS::EC2::Instance',
                'resourceId': 'resourceId',
            },
            'messageType': 'ConfigurationItemChangeNotification'
        }

        self.sampleEvent = {
            'invokingEvent': json.dumps(self.sampleInvokingEvent),
            'ruleParameters': '{"desiredInstanceType":"t2.micro"}',
            'resultToken': 'result-token',
            'eventLeftScope': False,
            'executionRoleArn': 'arn:aws:iam::accountId:role/service-role/config-role',
            'configRuleArn': 'arn:aws:config:region:accountId:config-rule/config-rule-id',
            'configRuleName': 'configRuleName',
            'configRuleId': 'configRuleId',
            'accountId': 'accountId'
        }

    def evaluateConfiguration(self, testInvokingEvent, compliance):
        testEvent = self.sampleEvent.copy()
        testEvent['invokingEvent'] = json.dumps(testInvokingEvent);

        expected_response = {
            'FailedEvaluations': []
        }

        with Stubber(aws_config) as stubber:
            stubber.add_response('put_evaluations', expected_response)
            result = rule_code.lambda_handler(testEvent, {})
            self.assertEqual(result, compliance)

    def test_verify_noncompliant_resource(self):
        testInvokingEvent = self.sampleInvokingEvent.copy()
        testInvokingEvent['configurationItem']['configuration']['instanceType'] = 't2.small'
        self.evaluateConfiguration(testInvokingEvent, 'NON_COMPLIANT')

    def test_verify_compliant_resource(self):
        testInvokingEvent = self.sampleInvokingEvent.copy()
        testInvokingEvent['configurationItem']['configuration']['instanceType'] = 't2.micro'
        self.evaluateConfiguration(testInvokingEvent, 'COMPLIANT')

    def test_verify_nonapplicable_resource(self):
        testInvokingEvent = self.sampleInvokingEvent.copy()
        testInvokingEvent['configurationItem']['resourceType'] = 'AWS::SNS::Topic'
        self.evaluateConfiguration(testInvokingEvent, 'NOT_APPLICABLE')

if __name__ == '__main__':
    unittest.main()
