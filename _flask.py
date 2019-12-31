from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    print(request.args)
    return '1'

app.handle_http_exception = hello


# def handle_bad_request(e):
#     return 'opa', 400


app.register_error_handler(400, hello)

app.run(port=3000)
