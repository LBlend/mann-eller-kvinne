from flask import Flask, request
import classifier


app = Flask(__name__)


@app.route('/')
def home():
    return 'API goes BRRRRRRRRRRR\nYeet'


@app.route('/mann-eller-kvinne', methods=['POST'])
def mann_eller_kvinne():
    data = request.get_json()
    print(data)
    text = data['text']
    if not text:
        return 'Du må gi meg noe tekst da idiot!'

    return classifier.predict(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
