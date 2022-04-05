from . import classifier
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost",
    ],
    allow_methods=["GET", "POST"],
)


class PredictionInput(BaseModel):
    text: str
    classifier: str


@app.get("/")
def home() -> str:
    return "API goes BRRRRRRRRRRR\nYeet"


@app.post("/mann-eller-kvinne")
def mann_eller_kvinne(payload: PredictionInput) -> dict[str, str | dict[str, float]]:
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

    print("Received", payload, sep="\t")
    if not payload.text:
        return "Du må gi meg noe tekst da idiot!"

    response = classifier.predict(payload.text, payload.classifier)
    print("Responding with", response, sep="\t")
    return response
