# -*- coding: utf-8 -*-
"""
Main API module
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
import json.scanner
import logging

import fastapi

import main_package.config
import main_package.main

print(json.__name__)

# The API, which can be hosted with uvicorn.
api = fastapi.FastAPI()


# Handle HTTP Get on "/ping"
@api.get("/ping")
def ping():
    """Ping liveness check

    return:
        A mapping with a 'message' = "pong", and a "timstamp" = current UTZ time
    """
    return {
        "message": "pong",
        "version": main_package.__version__,
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
    }


@api.get("/main_package")
def handler(arg: str):
    """Example endpoint calling some logic.

    Args:
        arg (str):
            The argument

    Returns:
        str:
            The result
    """
    return {"result": main_package.main.entrypoint(arg)}


@api.on_event("startup")
async def startup_event():
    """Start-up event handler

    Runs once when the API starts.
    """
    logging.info(f"Starting up API '{main_package.__name__}'")


@api.on_event("shutdown")
async def shutdown_event():
    """Tear-down event handler

    Runs once whe the API is (gracefully) shut down.
    """
    logging.info(f"Shutting down '{main_package.__name__}'")


def run_local(
    host=main_package.config.api_host,
    port=main_package.config.api_port,
):
    """Run a self-hosted API instance."""
    try:
        import uvicorn
    except ModuleNotFoundError:
        logging.error(
            """
You are trying to run the API locally, but you do not seem to have the
`uvicorn` package intsalled. You can either:
    - install `uvicorn` manually (e.g. `pip intall uvicorn`), or
    - if for local development: `pip install --editable .[local]`
"""
        )
    uvicorn.run(api, host=host, port=port)


if __name__ == "__main__":
    run_local()
