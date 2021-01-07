from flask import Flask, request
from flask_cors import CORS, cross_origin

import classifier


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': ['https://mannellerkvinne.lblend.moe', 'http://localhost:3000']}})
cross_origin(
    origins=['https://mannellerkvinne.lblend.moe', 'http://localhost:3000'],
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
    '''
    Input fields:
        text: str | input data for classifier
        clf: str | which classifier to use, default: bayes

    Output fields:
        clf: str
        probs: JSON
            M: float | estimated probability for the male class
            F: float | estimated probability for the female class
    '''
    data = request.get_json()
    print('Received', data)
    text = data['text']
    if not text:
        return 'Du må gi meg noe tekst da idiot!'

    clf = data.get('clf', 'bayes')
    response = classifier.predict(text, clf)
    print('Responding with', response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
