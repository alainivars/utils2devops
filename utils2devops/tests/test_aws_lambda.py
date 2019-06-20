from unittest import TestCase, mock

from _pytest import unittest

from utils2devops.aws.aws_lambda import list_lambda_function
from utils2devops.tests.aws_base import SingletonSession

functions_mock = {
    'ResponseMetadata': {
        'RequestId': '4077d71d-936b-11e9-91ae-0b5a911986a2',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'date': 'Thu, 20 Jun 2019 14:54:06 GMT',
            'content-type': 'application/json',
            'content-length': '755',
            'connection': 'keep-alive',
            'x-amzn-requestid': '4077d71d-936b-11e9-91ae-0b5a911986a2'
        },
        'RetryAttempts': 0
    },
    'Functions': [{
        'FunctionName': 'hf-al-s3-get-object',
        'FunctionArn': 'arn:aws:lambda:us-east-2:397270606208:function:hf-al-s3-get-object',
        'Runtime': 'python3.7',
        'Role': 'arn:aws:iam::397270606208:role/service-role/hf-role-s3-ro',
        'Handler': 'lambda_function.lambda_handler',
        'CodeSize': 566,
        'Description': 'An Amazon S3 trigger that retrieves metadata for the object that has been updated.',
        'Timeout': 3,
        'MemorySize': 128,
        'LastModified': '2019-06-20T09:08:10.964+0000',
        'CodeSha256': 'Wg0ZsXe2tOdL+IBvvNe0JrZpkKKFgRDA1aE4BN6Xr7E=',
        'Version': '$LATEST',
        'TracingConfig': {
            'Mode': 'PassThrough'
        },
        'RevisionId': 'd471c835-6bb0-44cb-b542-9af4cacc7984'
    }]
}
conf_mock = {
    'ResponseMetadata': {
        'RequestId': '5e6c7294-936b-11e9-a565-f92e534a48b2',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'date': 'Thu, 20 Jun 2019 14:54:56 GMT',
            'content-type': 'application/json',
            'content-length': '2451',
            'connection': 'keep-alive',
            'x-amzn-requestid': '5e6c7294-936b-11e9-a565-f92e534a48b2'
        },
        'RetryAttempts': 0
    }, 'Configuration': {
        'FunctionName': 'hf-al-s3-get-object',
        'FunctionArn': 'arn:aws:lambda:us-east-2:397270606208:function:hf-al-s3-get-object',
        'Runtime': 'python3.7',
        'Role': 'arn:aws:iam::397270606208:role/service-role/hf-role-s3-ro',
        'Handler': 'lambda_function.lambda_handler',
        'CodeSize': 566,
        'Description': 'An Amazon S3 trigger that retrieves metadata for the object that has been updated.',
        'Timeout': 3,
        'MemorySize': 128,
        'LastModified': '2019-06-20T09:08:10.964+0000',
        'CodeSha256': 'Wg0ZsXe2tOdL+IBvvNe0JrZpkKKFgRDA1aE4BN6Xr7E=',
        'Version': '$LATEST',
        'TracingConfig': {
            'Mode': 'PassThrough'
        },
        'RevisionId': 'd471c835-6bb0-44cb-b542-9af4cacc7984'
    }, 'Code': {
        'RepositoryType': 'S3',
        'Location': 'https://awslambda-us-east-2-tasks.s3.us-east-2.amazonaws.com/snapshots/397270606208/hf-al-s3-get-object-bab8190f-c4cc-4eec-8754-e5bc796a30aa?versionId=Ek13bezG0edscJA1g0WrNkk9IzyL87H6&X-Amz-Security-Token=AgoJb3JpZ2luX2VjEFUaCXVzLWVhc3QtMiJGMEQCIFlW2J%2FAGlW6iqg3h8WWpZ%2FixcXHjGsTqFlB3UFIZdhwAiAmEn9OX4CiYMU5h%2F1TrML2jmXvGpnTaKWMohmehnwckCrjAwiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDEwNDI0NjAxNzg2NSIMizSQ%2B%2BBDXsZzIKAlKrcD8vgbFF9iU6O%2Bv2g5jaX9b1YvoqW6egmzFjC9r1f5mQy5bH%2BUiqjmjXjlV06BWVsUtpn896XISiL4kRtL7qDCYYBpEHH%2BNgeVPei73lPuCI0Zbge7iTaHhnJ0YQ1s8W5T2bs1igWv2kQr%2BQ%2BKxSUmi3PAkM8F9CZ34qS9f%2FsXxScnUFYapePZ%2BvehcrY1vFpfA6%2FdtWpz45eM4IACGuOYk55JDz33rnlxsYsHBV4HpkDWb%2FcB5rhyv3GU9XjQVrk5Ur9bn%2FcZ6e1OyoLb9DmwmTsC40eKycnmNeyxHmEU5mErFAFS18j8qnSIJxLTjmT%2F4vi7fVxTx7P9Lsqg8hkHslUeL6ItHejw%2FTjIEH0T6ro6r4gZPvoNNbKUYXYk9t94qtHffNlKqP2yx6mj8OsRyXalD6jHbaBjMNoukgAfmqMZTWfGP23Mb2R0Z2x0BgPZnG1%2BCJ8t1RZqxZiHm3lNxHpcLxnpVEn8Upu3j1y%2B29HKEbS7cQH%2BpE%2BJNmlW0i%2ByRShGlnQNNOkPOT5uvdpP16%2FKzymZ8HQJfK3fWQD%2BACaPeh1YMOM6rNY%2BPMRT40V35g11ntNeZzDci67oBTq1AejD5gOXlAjZ2%2BE%2BbfWqOYBv%2BBd42W9YZZJCOCDoswb89ceibWevmN0ud2xis6gLQDvTbxOGEaTP8SK7MYoD9no3ylpbvCZ8t3Q6NenxSuLEENUChaDYFK7YDcFUZitWg5Wv8hRl3YDooTGT0vUNBSqNlWCelbdWSRFH5OSjlkMwA%2Bh8YqlD7xIUuFsAh9678VSiysCP3VkuhNAAPhHwMC6m9U8AUHUGGhg5Q9Mx3s%2Fz%2F36%2BdHY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190620T145456Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIARQRML75EV35K6NVO%2F20190620%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=ddf968db2b9e380df4a4c1d90fef7bfa47cf08da362cef3c084ff3e4c2a16a1d'
    }, 'Tags': {
        'lambda-console:blueprint': 's3-get-object-python'
    }
}
result = [
    'resource "aws_lambda_function" "hf-al-s3-get-object" {\n',
    '\tfunction_name = "hf-al-s3-get-object"\n',
    '\thandler = "lambda_function.lambda_handler"\n',
    '\trole = "arn:aws:iam::397270606208:role/service-role/hf-role-s3-ro"\n',
    '\tdescription = "An Amazon S3 trigger that retrieves metadata for the object ',
    'that has been updated."\n',
    '\tmemory_size = "128"\n',
    '\truntime = "python3.7"\n',
    '\ttimeout = "3"\n',
    '\tsource_code_hash = "Wg0ZsXe2tOdL+IBvvNe0JrZpkKKFgRDA1aE4BN6Xr7E="\n',
    '\ttags {\n',
    '\t\t"lambda-console:blueprint" = "s3-get-object-python"\n',
    '\t}\n',
    '}\n',
]
expected_result = ''.join(result)

"""
for future add of feature:
input data from AWS
list_aliases
list_event_source_mappings
list_layers
list_tags
"lambda-console:blueprint"
list_versions_by_function
{
    "CodeSha256": "Wg0ZsXe2tOdL+IBvvNe0JrZpkKKFgRDA1aE4BN6Xr7E=",
    "CodeSize": 566,
    "Description": "An Amazon S3 trigger that retrieves metadata for the object that has been updated.",
    "FunctionArn": "arn:aws:lambda:us-east-2:397270606208:function:hf-al-s3-get-object:$LATEST",
    "FunctionName": "hf-al-s3-get-object",
    "Handler": "lambda_function.lambda_handler",
    "LastModified": "2019-06-20T09:08:10.964+0000",
    "MemorySize": 128,
    "RevisionId": "d471c835-6bb0-44cb-b542-9af4cacc7984",
    "Role": "arn:aws:iam::397270606208:role/service-role/hf-role-s3-ro",
    "Runtime": "python3.7",
    "Timeout": 3,
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "Version": "$LATEST"
}
"""


class AwsLambdaTestCase(TestCase):
    @mock.patch('boto3.Session', SingletonSession)
    def test_list_lambda_nominal(self):
        # nominal
        profile_name = 'test'
        region_name = 'us-east-2'
        session = SingletonSession(profile_name=profile_name)
        client = session.client(service_name='lambda', region_name=region_name)
        client.lambda_functions = functions_mock
        client.lambda_conf = conf_mock
        ls = list_lambda_function(profile_name, region_name)
        self.assertEqual(str(ls[0]), expected_result)


if __name__ == '__main__':
    unittest.main()
