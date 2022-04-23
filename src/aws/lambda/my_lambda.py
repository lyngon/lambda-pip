# -*- coding: utf-8 -*-
"""
Lambda Function Wrappers
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
from typing import Any, Dict

import main_package.main


def entrypoint(event: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:

    args = []
    if event and "pathParameters" in event:
        args = event["pathParameters"]

    kwargs = {}
    if event and "queryStringParameters" in event:
        kwargs = event["queryStringParameters"]

    result = main_package.main.entrypoint(*args, **kwargs)

    return {"result": result}