from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is your Flask API.'


@app.route('/api/run_code', methods=['POST'])
def hello_world():
    return 'Hello, World! This is your Flask API.'

if __name__ == '__main__':
    app.run(debug=True)
