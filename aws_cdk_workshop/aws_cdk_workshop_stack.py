from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

from .hitcounter import HitCounter
from cdk_dynamo_table_view import TableViewer

class AwsCdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines an AWS Lambda resource
        hello_service = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('aws_cdk_workshop/lambda'),
            handler='hello.handler'
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=hello_service
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler
        )

        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_counter.table,
            sort_by='-hits'
        )
