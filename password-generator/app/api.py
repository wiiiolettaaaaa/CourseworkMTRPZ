from flask import Flask, request, jsonify
from generator import generate_password

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    length = int(request.args.get('length', 12))
    digits = request.args.get('digits', 'true').lower() == 'true'
    symbols = request.args.get('symbols', 'true').lower() == 'true'
    uppercase = request.args.get('uppercase', 'true').lower() == 'true'

    try:
        password = generate_password(length, digits, symbols, uppercase)
        return jsonify({"password": password})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)