"""
Application configuration and default settings.

This module defines file paths and default values used by the
remote working relief calculator.
"""

from pathlib import Path

# CSV file locations
DATA_DIR = Path("data")

ELECTRICITY_FILE = DATA_DIR / "electricity.csv"
GAS_FILE = DATA_DIR / "gas.csv"
BROADBAND_FILE = DATA_DIR / "broadband.csv"

# Default inputs
YEAR = 2024
REMOTE_WORK_DAYS = 178
EMPLOYER_CONTRIBUTION = 0.0