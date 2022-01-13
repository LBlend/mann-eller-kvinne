import classifier
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PredictionInput(BaseModel):
    text: str
    clf: str


@app.get("/")
def home() -> str:
    return "API goes BRRRRRRRRRRR\nYeet"


@app.post("/mann-eller-kvinne")
def mann_eller_kvinne(payload: PredictionInput) -> dict[str, str | dict[str, float]]:
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
        return "Du må gi meg noe tekst da idiot!"

    response = classifier.predict(payload.text, payload.clf)
    print("Responding with", response)
    return response
