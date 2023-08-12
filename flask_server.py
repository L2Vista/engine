from flask_cors import CORS
from flask import Flask, request, jsonify

from conversation import conversation


app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    human_input = request.get_json().get('human_input')
    ai_output = conversation(human_input)
    return jsonify({'ai_output': ai_output[0], 'parsed': ai_output[1]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30327)
