#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    try:
        n = int(param)
        if n >= 0:
            # Generate a string with numbers from 0 to n-1, each separated by a newline character
            count = '\n'.join(str(i) for i in range(n))
            # Adding a trailing newline to match the test expectation
            return count + '\n'
    except ValueError:
        pass
    return 'Invalid parameter'


@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation!'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
