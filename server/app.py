from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

@app.route('/count/<int:number>')
def count(number):
    output = "\n".join(str(i) for i in range(number)) + "\n"
    return output


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)