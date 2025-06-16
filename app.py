from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def text_to_binary(text):
    if not isinstance(text, str):
        raise TypeError("El parametro 'text' debe ser una cadena")
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    if not isinstance(binary, str):
        raise TypeError("El parametro 'binary' debe ser una cadena")
    try:
        chars = []
        for b in binary.split():
            if len(b) != 8 or any(bit not in '01' for bit in b):
                raise ValueError
            chars.append(chr(int(b, 2)))
        return ''.join(chars)
    except ValueError:
        raise ValueError("Entrada binaria no válida")

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='ok')

@app.route('/convert/text-to-binary', methods=['POST'])
def convert_text_to_binary():
    data = request.get_json(silent=True)
    if not data or 'text' not in data:
        return jsonify(error="Se requiere el parametro 'text'"), 400
    try:
        binary_result = text_to_binary(data['text'])
    except TypeError as e:
        return jsonify(error=str(e)), 400
    return jsonify(binary=binary_result)

@app.route('/convert/binary-to-text', methods=['POST'])
def convert_binary_to_text():
    data = request.get_json(silent=True)
    if not data or 'binary' not in data:
        return jsonify(error="Se requiere el parametro 'binary'"), 400
    try:
        text_result = binary_to_text(data['binary'])
    except (TypeError, ValueError) as e:
        return jsonify(error=str(e)), 400
    return jsonify(text=text_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
