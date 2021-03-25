from flask import Flask

dapp = Flask(__name__)

@dapp.route('/')
def head():
    return 'Hello Worldum'
@dapp.route('/second')
def s():
    return 'This is second page'
@dapp.route('/subthird')
def t():
    return 'This is subthird of third'

@dapp.route('/fourth/<string:id>')
def f(id):
    return f'Id of this page is {id}'

if __name__== '__main__':
    dapp.run(debug=True)