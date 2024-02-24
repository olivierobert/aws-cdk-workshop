from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)


class AwsCdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines an AWS Lambda resource
        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('aws_cdk_workshop/lambda'),
            handler='hello.handler'
        )
