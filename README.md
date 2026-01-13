# Remote Working Relief Calculator

A Python application that calculates remote working tax relief based on
Irish Revenue rules.

The project demonstrates:
- Clean Python project structure
- Business logic separation
- Error handling and logging
- Unit testing with pytest
- REST API using FastAPI

---

## Features

- Command-line interface (CLI)
- REST API for programmatic access
- CSV-based bill loading
- Custom exception handling
- Unit test coverage

---

## Project Structure

config/
utils/
data/
tests/
api.py
calculations.py
main.py
models.py

## Setup

Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Running the CLI
python main.py

Running the API
uvicorn api:app --reload


Once running, visit:

http://127.0.0.1:8000

Running Tests
pytest

Example API Request
curl -X POST http://127.0.0.1:8000/relief \
-H "Content-Type: application/json" \
-d '{
  "electricity": 1000,
  "gas": 800,
  "broadband": 400,
  "year": 2024,
  "remote_days": 180,
  "employer_contribution": 0
}'

Notes

This project is intended as a learning and portfolio exercise and reflects
real-world Python development practices.


