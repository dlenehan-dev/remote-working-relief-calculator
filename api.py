"""
FastAPI application exposing the remote working relief calculator.
"""

from fastapi import FastAPI
from models import ReliefRequest, ReliefResponse
from calculations import calculate_relief

app = FastAPI(title="Remote Relief API")

from typing import Dict

@app.get("/")
def home() -> Dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Simple status message.
    """
    return {"message": "Remote Relief API is running."}


@app.post("/relief", response_model=ReliefResponse)
def get_relief(data: ReliefRequest) -> ReliefResponse:
    
    """
    Calculate tax relief based on submitted bill and work data.

    Args:
        data: Relief request payload.

    Returns:
        Calculated relief response.
    """

    total_allowable = data.electricity + data.gas + data.broadband

    relief = calculate_relief(
        total_allowable_bills=total_allowable,
        remote_days=data.remote_days,
        employer_contribution=data.employer_contribution,
        year=data.year,
    )

    return ReliefResponse(
        year=data.year,
        total_allowable=total_allowable,
        remote_days=data.remote_days,
        employer_contribution=data.employer_contribution,
        relief=relief,
    )

