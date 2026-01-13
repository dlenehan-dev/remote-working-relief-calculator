import pytest
from pydantic import ValidationError
from models import ReliefRequest

def test_relief_request_valid_input():
    model = ReliefRequest(
        electricity=100,
        gas=200,
        broadband=300,
        year=2024,
        remote_days=100,
        employer_contribution=0,
    )

    assert model.year == 2024


def test_relief_request_negative_electricity():
    with pytest.raises(ValidationError):
        ReliefRequest(
            electricity=-1,
            gas=0,
            broadband=0,
            year=2024,
            remote_days=100,
            employer_contribution=0,
        )


