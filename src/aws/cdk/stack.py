# -*- coding: utf-8 -*-
"""
AWS CDK Stack Definition
When run in AWS.
"""
__author__ = "Anders Åström"
__contact__ = "anders@lyngon.com"
__copyright__ = "2022, Lyngon Pte. Ltd."
__license__ = """Proprietary Software

Copyright (c) 2022 Lyngon Pte. Ltd.

This software and associated documentation files (the "Software") is proprietary.

The the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, is exclusively limited to Lyngon Pte. Ltd. and is subject
to the following conditions:

The above copyright notice and this notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import aws_cdk
import aws_cdk.aws_lambda_python_alpha
import constructs

import main_package.config


class Stack(aws_cdk.Stack):
    def __init__(
        self, scope: constructs.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Install the package in a Lambda Layer
        main_package_layer = aws_cdk.aws_lambda_python_alpha.PythonLayerVersion(
            self,
            main_package.__name__,
            entry=".",
        )

        # _main_packgage_layer = aws_cdk.aws_lambda.LayerVersion(
        #     self,
        #     main_package.__name__,
        #     code=aws_cdk.aws_lambda.Code.from_asset(
        #         ".",
        #         bundling=aws_cdk.BundlingOptions(
        #             image=aws_cdk.DockerImage.from_registry("lyngon/py-lambda-builder"),
        #             command=(
        #                 "pip install"
        #                 f" -r requirements-{main_package.config.environment}.txt"
        #                 " .[aws]"
        #             ),
        #         ),
        #     ),
        # )

        # My little lambda function
        my_lambda = aws_cdk.aws_lambda.Function(
            self,
            "MyLambda",
            runtime=aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
            code=aws_cdk.aws_lambda.Code.from_asset("aws/lambda"),
            handler="my_lambda.entrypoint",
            timeout=aws_cdk.Duration.seconds(10),
            layers=[main_package_layer],
        )

        my_lambda


aws_app = aws_cdk.App()

Stack(
    aws_app,
    "MyStack",
    env=aws_cdk.Environment(
        account=main_package.config.aws_account,
        region=main_package.config.aws_region,
    ),
)

aws_app.synth()
