# +-------------------------------------------------------------------------
# | Copyright (C) 2016 Yunify, Inc.
# +-------------------------------------------------------------------------
# | Licensed under the Apache License, Version 2.0 (the "License");
# | you may not use this work except in compliance with the License.
# | You may obtain a copy of the License in the LICENSE file, or at:
# |
# | http://www.apache.org/licenses/LICENSE-2.0
# |
# | Unless required by applicable law or agreed to in writing, software
# | distributed under the License is distributed on an "AS IS" BASIS,
# | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# | See the License for the specific language governing permissions and
# | limitations under the License.
# +-------------------------------------------------------------------------

import os

from flask import Flask, request
from qingstor.sdk.config import Config
from qingstor.sdk.request import Request

app = Flask(__name__)

# Get access_key_id and secret_access_key from system environment
access_key_id = os.environ.get('ACCESS_KEY_ID')
secret_access_key = os.environ.get('SECRET_ACCESS_KEY')

# Init a new config object with keyid
config = Config(access_key_id, secret_access_key)


def get_properties(data):
    """ Get properties from data

    :param data: the request data to be authorized
    :return: properties: request properties
    """
    properties = {}
    url = data['url'].split('/')
    if len(url) == 2 and url[1]:
        properties['bucket-name'] = url[1]
    if len(url) > 2 and url[2]:
        properties['object-key'] = url[2].split('?')[0]
    return properties


def get_auth(data):
    """ Get signature with specific operation

    :param data: the request data to be authorized
    :return: signature: authorized string
    """
    operation = {
        'Headers': data.get('headers', {}),
        'Method': data['method'],
        'Params': data.get('params', {}),
        'Properties': get_properties(data),
        'URI': data['url'],
    }
    signature = Request(config, operation).get_authorization()
    authorization = "QS %s:%s" % (access_key_id, signature)
    return authorization


@app.route('/', methods=['POST'])
def auth():
    return get_auth(request.json)


if __name__ == '__main__':
    app.run()
