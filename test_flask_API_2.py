from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    input_text = data.get('input_text')
    target_language = data.get('target_language', 'en')  # Default to English
    translator = Translator(to_language=target_language)
    translated_text = translator.translate(input_text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
