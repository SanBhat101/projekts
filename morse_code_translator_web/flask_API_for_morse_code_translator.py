from flask import Flask, jsonify, request
from flask_cors import CORS
from morse_code_translator import translate_to_morse

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hi! This is my Flask API.'

@app.route('/api/translate_to_morse', methods=['POST'])
def api_translate_to_morse():
    if request.is_json:
        data = request.get_json()
        if 'user_input' not in data:
            return jsonify({'message': 'User Input not found in the JSON payload! This is a POST request.'}), 400
        else:
            user_string = data['user_input']
            user_string=translate_to_morse(user_string)
            return jsonify({'result': user_string})
    else:
        return jsonify({'error': 'Invalid JSON payload'}), 400


@app.route('/api/to_morse', methods=['GET'])
def api_test_to_morse():
    user_string="abc $ def & ghi * test { kampai"
    user_string=translate_to_morse(user_string)
    return jsonify({'result': user_string})

if __name__ == '__main__':
    app.run(debug=True)
