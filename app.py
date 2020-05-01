import os
import socket
import logging
from sanic import Sanic
from sanic.response import json
from sanic_function_deps.function_helper import create_function_deps

app = Sanic()
function_deps = create_function_deps()
logger = logging.getLogger()

APP_TOKEN = os.environ['TOKEN']
APP_PORT = int(os.environ.get('PORT', 8000))
APP_TIMEOUT = int(os.environ.get('TIMEOUT', 10))


@app.route('/', methods=["POST"])
@function_deps(['token', 'domain', 'port'])
async def test(token: str, domain: str, port: int):

    if token != APP_TOKEN:
        return json(
            {
                'error': 'Incorrect token',
                'domain': domain,
                'port': port,
                'status': 'N/A'}
        )

    s = socket.socket()
    s.settimeout(APP_TIMEOUT)
    try:
        s.connect((domain, port))
    except Exception:
        return json({'status': 'Offline', 'domain': domain, 'port': port})
    finally:
        s.close()
    return json({'status': 'Online', 'domain': domain, 'port': port})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)
