from flask import Flask, request
from flask_cors import CORS, cross_origin

import classifier


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': ['https://genderapi.lblend.moe', 'http://localhost:3000']}})
cross_origin(
    origins=['https://genderapi.lblend.moe', 'http://localhost:3000'],
    methods=['GET', 'POST'],
    always_send=True,
    automatic_options=True,
    headers=['Content-Type']
)


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
