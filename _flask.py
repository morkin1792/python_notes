from flask import Flask, request, make_response
from datetime import datetime
import sys

app = Flask(__name__)

logf = open('flask.log', 'a')

@app.route('/', methods= ['GET', 'POST'])
def hello():
    # logf.write()
    
    logf.write('* [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] connection from: ' + request.remote_addr + '\n')
    logf.write(request.get_data().decode() + '\n')
    logf.flush()
    resp = make_response('1')
    resp.headers['server'] = 'Server'
    origin = request.headers.get('Origin')
    if len(origin) < 1:
        origin = request.headers.get('origin')
    if len(origin) > 0:
        resp.headers['Access-Control-Allow-Origin'] = origin
    return resp

app.handle_http_exception = hello
app.register_error_handler(400, hello)

port = 8091
if len(sys.argv) > 1:
    port = sys.argv[1]
app.run(port=port, host='0.0.0.0')
