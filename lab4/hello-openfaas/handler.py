import os
import sys
import json


def handle(req):
    http_query = os.getenv("Http_Query")
    sys.stderr.write("This should be an error message.\n")
    return json.dumps({ "Hello": "OpenFaaS", 'test': http_query })
