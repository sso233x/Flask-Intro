from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = request.args.get("a")
    b = request.args.get("b")
    return f"{int(a) + int(b)}"

@app.route('/sub')
def sub_route():
    a = request.args.get("a")
    b = request.args.get("b")
    return f"{int(a) - int(b)}"

@app.route('/mult')
def mult_route():
    a = request.args.get("a")
    b = request.args.get("b")
    return f"{int(a) * int(b)}"

@app.route('/div')
def div_route():
    a = request.args.get("a")
    b = request.args.get("b")
    return f"{int(a) / int(b)}"

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route('/math/<route>')
def all_in_one_route(route):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[route](a,b)
    return str(result)