from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except ValueError:
        return "Error: Entrada binaria no válida"

@app.route('/convert/text-to-binary', methods=['POST'])
def convert_text_to_binary():
    data = request.get_json()
    text = data.get('text', '')
    binary_result = text_to_binary(text)
    return jsonify({"binary": binary_result})

@app.route('/convert/binary-to-text', methods=['POST'])
def convert_binary_to_text():
    data = request.get_json()
    binary = data.get('binary', '')
    text_result = binary_to_text(binary)
    return jsonify({"text": text_result})

if __name__ == '__main__':
    app.run(debug=True)
