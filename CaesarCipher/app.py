# app.py
from flask import Flask, request, jsonify
import json

from CaesarCipher.utils import get_cipher

app = Flask(__name__)

@app.route('/', methods=['GET'])
def cipher_api():
    params = request.args.get('params')
    if params:
        params = json.loads(params)
        string = params.get('string')
        encrypt = params.get('encrypt', True)
        key = params.get('key', None)
        
        if string is None:
            return jsonify({"error": "String parameter is missing"}), 400
        
        try:
            result = get_cipher(string, key, encrypt)
            return jsonify({"result": result})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Params are missing"}), 400

if __name__ == '__main__':
    app.run(debug=True)
