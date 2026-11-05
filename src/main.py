from typing import Annotated, Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, StringConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict

from . import classifier


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    allowed_origins: str = "http://localhost:3000,http://localhost"

    @property
    def origins(self) -> list[str]:
        return [origin.strip() for origin in self.allowed_origins.split(",") if origin.strip()]


settings = Settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    max_age=3600,
)


class PredictionInput(BaseModel):
    text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=10000)]
    classifier: Literal["bayes", "rnn"] = "bayes"


@app.get("/")
def home() -> str:
    return "API goes BRRRRRRRRRRR\nYeet"


@app.post("/mann-eller-kvinne")
def mann_eller_kvinne(payload: PredictionInput) -> dict[str, str | dict[str, float]]:
    """
    Input fields:
        text: str | input data for classifier (1-10000 characters)
        classifier: str | which classifier to use (bayes or rnn), default: bayes

    Output fields:
        text: str | the input text
        classifier: str | which classifier was used
        probability: dict
            male: float | estimated probability for the male class
            female: float | estimated probability for the female class
    """
    return classifier.predict(payload.text, payload.classifier)
