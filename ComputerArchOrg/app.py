from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signed-addition')
def signed_addition():
    return render_template('signed_add.html')

@app.route('/signed-subtraction')
def signed_subtraction():
    return render_template('signed_sub.html')

@app.route('/binary-multiplication')
def binary_multiplication():
    return render_template('bin_mul.html')

@app.route('/booth-multiplication')
def booth_multiplication():
    return render_template('booth_mul.html')

@app.route('/binary-division')
def binary_division():
    return render_template('bin_div.html')

# Signed Addition Endpoint
@app.route('/calculate_addition', methods=['POST'])
def calculate_addition():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result_decimal = num1 + num2
    result_binary = bin(result_decimal)[2:]
    return jsonify(result_decimal=result_decimal, result_binary=result_binary)

# Signed Subtraction Endpoint
@app.route('/calculate_subtraction', methods=['POST'])
def calculate_subtraction():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result_decimal = num1 - num2
    result_binary = bin(result_decimal)[2:] if result_decimal >= 0 else '-' + bin(result_decimal)[3:]
    return jsonify(result_decimal=result_decimal, result_binary=result_binary)

# Binary Multiplication Endpoint
@app.route('/calculate_multiplication', methods=['POST'])
def calculate_multiplication():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result_decimal = num1 * num2
    result_binary = bin(result_decimal)[2:]
    return jsonify(result_decimal=result_decimal, result_binary=result_binary)

# Booth's Multiplication Endpoint
@app.route('/calculate_booths', methods=['POST'])
def calculate_booths():
    data = request.get_json()
    multiplicand = int(data['multiplicand'])
    multiplier = int(data['multiplier'])
    result_decimal = booth_multiplication(multiplicand, multiplier)
    result_binary = bin(result_decimal)[2:]
    return jsonify(result_decimal=result_decimal, result_binary=result_binary)

# Booth's Multiplication function
def booth_multiplication(multiplicand, multiplier):
    product = multiplicand * multiplier  # Placeholder for Booth's actual algorithm
    return product

# Binary Division (Restoring Method) Endpoint
@app.route('/calculate_division', methods=['POST'])
def calculate_division():
    data = request.get_json()
    dividend = int(data['dividend'])
    divisor = int(data['divisor'])
    quotient, remainder = restoring_division(dividend, divisor)
    return jsonify(quotient_decimal=quotient, quotient_binary=bin(quotient)[2:],
                   remainder_decimal=remainder, remainder_binary=bin(remainder)[2:])

# Binary Division (Restoring Method) function
def restoring_division(dividend, divisor):
    quotient = dividend // divisor  # Placeholder for Restoring Division actual algorithm
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    app.run(debug=True)
