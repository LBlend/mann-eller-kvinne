from . import classifier
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
import os


app = FastAPI()

# CORS configuration with environment variable support
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    max_age=3600,
)


class PredictionInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000, description="Text to classify")
    classifier: str = Field(default="bayes", pattern="^(bayes|rnn)$", description="Classifier to use")

    @field_validator('text')
    @classmethod
    def validate_text(cls, v: str) -> str:
        # Strip whitespace
        v = v.strip()
        if not v:
            raise ValueError("Text cannot be empty or only whitespace")
        # Check for reasonable length
        if len(v) > 10000:
            raise ValueError("Text is too long (max 10000 characters)")
        return v


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
    try:
        print("Received request with classifier:", payload.classifier)

        # Validate classifier exists
        if payload.classifier not in ["bayes", "rnn"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid classifier. Must be 'bayes' or 'rnn'"
            )

        response = classifier.predict(payload.text, payload.classifier)
        print("Prediction completed successfully")
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during prediction"
        )
