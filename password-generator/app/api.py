from flask import Flask, request, jsonify
from generator import generate_password
from structures.singly_circular_list import SinglyCircularList

app = Flask(__name__)
password_history = SinglyCircularList()

@app.route('/generate', methods=['GET'])
def generate():
    length = int(request.args.get('length', 12))
    digits = request.args.get('digits', 'true').lower() == 'true'
    symbols = request.args.get('symbols', 'true').lower() == 'true'
    uppercase = request.args.get('uppercase', 'true').lower() == 'true'

    try:
        password = generate_password(length, digits, symbols, uppercase)
        password_history.append(password)  # ← записуємо в історію
        return jsonify({"password": password})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/history', methods=['GET'])
def history():
    return jsonify({"history": password_history.display()})

@app.route("/")
def home():
    return "<h1>Password Generator API</h1><p>Use <code>/generate</code> with parameters to generate a password.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)