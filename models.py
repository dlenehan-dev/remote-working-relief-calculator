"""
Pydantic models for API request and response validation.
"""

# models.py

from pydantic import BaseModel, Field

class ReliefRequest(BaseModel):
    """Input model for relief calculation requests."""
    electricity: float = Field(..., ge=0)
    gas: float = Field(..., ge=0)
    broadband: float = Field(..., ge=0)
    year: int = Field(..., ge=2000, le=2100)
    remote_days: int = Field(..., ge=0, le=366)
    employer_contribution: float = Field(..., ge=0)

class ReliefResponse(BaseModel):
    """Response model containing calculated relief data."""
    year: int
    total_allowable: float
    remote_days: int
    employer_contribution: float
    relief: float
