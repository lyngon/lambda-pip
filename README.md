# Lambda Pip

Facilitates adding Python dependencies to AWS Lambda layers when using AWS CDK

### Example:
```python
class Stack(aws_cdk.Stack):
    def __init__(
        self, scope: constructs.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Install requirements in a Lambda Layer
        dependency_layer = aws_cdk.aws_lambda.LayerVersion(
            self,
            "my-lambda-dependency-layer",
            code=aws_cdk.aws_lambda.Code.from_asset(
                ".",
                bundling=aws_cdk.BundlingOptions(
                    image=aws_cdk.DockerImage.from_registry("lyngon/lambda-pip:3.9"),
                    command=["-r", "requirements.txt"],
                ),
            ),
        )

        # Lambda Function, with the layer
        my_lambda = aws_cdk.aws_lambda.Function(
            self,
            "my-lambda",
            runtime=aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
            code=aws_cdk.aws_lambda.Code.from_asset("src/aws/lambda"),
            handler="my_lambda.entrypoint",
            layers=[dependency_layer],
        )
```
