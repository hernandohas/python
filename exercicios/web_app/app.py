from flask import Flask, request
app = Flask(__name__)

# Requisições GET
@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/json')
def hello_jason():
    return {'chave': 'valor'}

@app.route('/<nome>')
def greet(nome):
    return f'<p style="color: red">Hello, {nome}</p>'

@app.route('/save', methods = ['POST'])
def save():
    json = request.json
    print (json)
    return json