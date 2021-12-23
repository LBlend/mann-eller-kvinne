from fastapi import FastAPI, HTTPException
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
    classifier: str


@app.get("/")
def home():
    return "API goes BRRRRRRRRRRR\nYeet"


@app.post("/mann-eller-kvinne")
def mann_eller_kvinne(payload: PredictionInput):
    """
    Input fields:
        text: str | input data for classifier
        classifier: str | which classifier to use, default: bayes

    Output fields:
        classifier: str | which classifier was used
        probs: JSON
            male: float | estimated probability for the male class
            female: float | estimated probability for the female class
    """

    if not payload.text:
        raise HTTPException(status_code=400, detail="Du må gi meg noe tekst da idiot!")

    response = classifier.predict(payload.text, payload.classifier)
    return response
