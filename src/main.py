from fastapi import FastAPI
from pydantic import BaseModel

import classifier

from dotenv import load_dotenv
from os import getenv


# Get environment variables
load_dotenv()
frontend_url = getenv("FRONTEND_URL")
port = getenv("PORT")


app = FastAPI()


class PredictionInput(BaseModel):
    text: str
    clf: str


@app.get("/")
def home():
    return "API goes BRRRRRRRRRRR\nYeet"


@app.post("/mann-eller-kvinne")
def mann_eller_kvinne(payload: PredictionInput):
    """
    Input fields:
        text: str | input data for classifier
        clf: str | which classifier to use, default: bayes

    Output fields:
        clf: str | which classifier was used
        probs: JSON
            M: float | estimated probability for the male class
            F: float | estimated probability for the female class
    """

    print("Received", payload)

    if not payload.text:
        response = {"status": "failed", "message": "Du må gi meg noe tekst da idiot!"}
        print("Responding with", response)
        return response

    response = classifier.predict(payload.text, payload.clf)
    print("Responding with", response)
    return response
