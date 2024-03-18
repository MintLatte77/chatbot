import flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/meal')
def meal():
    json_data = request.get_json()
    timezone = json_data['userRequest']['timezone']
    return {"version": "2.0","template":{"outputs": [{"simpleText": {"text": json_data}}]}}

app.run("0.0.0.0")
