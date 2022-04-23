# -*- coding: utf-8 -*-
"""
Configurations

Including but not limited to:

    - Constants
    - Common helper functions
    - Application arguments
    - Environment variables
    - Secrets
    - Logging config
"""
__author__ = "Anders Åström"
__contact__ = "anders@lyngon.com"
__copyright__ = "2022, Lyngon Pte. Ltd."
__licence__ = """Proprietary Software

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
import datetime
import logging.config
import pathlib

import configargparse

###############################################################################
# #                              Constants                                  # #
###############################################################################

timezone = datetime.timezone(datetime.timedelta(hours=8), "SGT")

###############################################################################
# #                       Common Helper functions                           # #
###############################################################################


def now() -> datetime.datetime:
    """Get current local time (with timezone)

    :return:
        Current local time.
    """
    return datetime.datetime.now(timezone)


def is_prod() -> bool:
    """Checks if the environment name contains "prod"

    Returns:
        bool:
            `True` if it does, `False` otherwise.
    """
    return "prod" in environment


###############################################################################
# #                 Environment Variables and Arguments                     # #
###############################################################################

# Create an argument (and env.var.) parser, using defaults from "default.conf"
argparser = configargparse.ArgParser(
    default_config_files=["default.conf"],
)

argparser.add_argument(
    "-c",
    "--config",
    env_var="CONFIG",
    is_config_file=True,
    help="Configuration file path.",
)
argparser.add_argument(
    "-V",
    "--version",
    action="store_true",
    help="Get version",
)
argparser.add_argument(
    "--logging_config_file",
    env_var="LOGGING_CONFIG_FILE",
    default=pathlib.Path("logging.conf"),
    type=pathlib.Path,
    help="Base directory for logs.",
)
argparser.add_argument(
    "--environment",
    env_var="ENVIRONMENT",
    default="prod",
    type=str,
    help="Environment name. E.g. 'dev'",
)


argparser.add_argument(
    "--aws-account",
    env_var="AWS_ACCOUNT",
    type=str,
    help="AWS account ID",
)
argparser.add_argument(
    "--aws-region",
    env_var="AWS_REGION",
    type=str,
    help="AWS region",
)

argparser.add_argument(
    "--api_host",
    env_var="API_HOST",
    default="127.0.0.1",
    type=str,
    help="API listen adapter",
)
argparser.add_argument(
    "-p",
    "--api_port",
    env_var="API_PORT",
    default=3000,
    type=int,
    help="API listen port",
)

# Parse Args/Env vars, and assign to typed vars for more pleasant Dev experience
args = argparser.parse_args()

# If the version flag was set, then just output the version, and exit.
if args.version:
    import importlib.metadata

    package_version = importlib.metadata.version("main_package")
    print(package_version)
    exit(0)

logging_config_file: pathlib.Path = args.logging_config_file
environment: str = args.environment

aws_account: str = args.aws_account
aws_region: str = args.aws_region
package_name: str = args.service_name
api_host: str = args.api_host
api_port: int = args.api_port

###############################################################################
# #                      Logging Configuration                              # #
###############################################################################
pathlib.Path("logs").mkdir(
    mode=777,
    exist_ok=True,
)
logging.config.fileConfig(str(logging_config_file))
