# main.py

"""
Command-line interface for the Remote Working Relief Calculator.

Provides an interactive CLI for calculating tax relief.
"""


from utils.logger import setup_logger
from utils.error_handling import MissingFileError, NonNumericValueError, EmptyFileError
from utils.file_loader import load_bill_file
from calculations import calculate_relief

# default config fallback
from config.settings import (
    ELECTRICITY_FILE,
    GAS_FILE,
    BROADBAND_FILE,
)

logger = setup_logger(__name__)


def ask_int(prompt: str) -> int:
    """
    Prompt the user for an integer value.

    Args:
        prompt: Input prompt text.

    Returns:
        Validated integer input from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def ask_float(prompt: str) -> float:
    """
    Prompt the user for a floating-point value.

    Args:
        prompt: Input prompt text.

    Returns:
        Validated floating-point input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid amount.")

def main():
    """
    Run the interactive remote working relief calculator.
    """
    logger.info("Remote Working Relief Calculator (Interactive Mode)")

    print("\n=== Remote Relief Calculator (Interactive) ===")

    # ----------------------------
    # Ask user for dynamic values
    # ----------------------------
    year = ask_int("Enter the year you are claiming for: ")
    remote_days = ask_int("Enter number of days you worked remotely: ")
    employer_contribution = ask_float("Enter employer contribution (0 if none): ")

    print("\nUsing CSV files saved in the /data directory...")  

    # ----------------------------
    # Load CSVs
    # ----------------------------
    try:
        electricity_total = load_bill_file(ELECTRICITY_FILE)
        gas_total = load_bill_file(GAS_FILE)
        broadband_total = load_bill_file(BROADBAND_FILE)

    except (MissingFileError, NonNumericValueError, EmptyFileError) as e:
        logger.error(f"Error loading CSV files: {e}")
        return

    total_allowable = electricity_total + gas_total + broadband_total

    logger.info(f"Total allowable bills (A): {total_allowable}")

    relief = calculate_relief(
        total_allowable_bills=total_allowable,
        remote_days=remote_days,
        employer_contribution=employer_contribution,
        year=year,
    )

    # ----------------------------
    # Results
    # ----------------------------
    print("\n===== REMOTE WORKING RELIEF RESULT =====")
    print(f"Year: {year}")
    print(f"Total Allowable Bills (A): {total_allowable:.2f}")
    print(f"Remote Days (B): {remote_days}")
    print(f"Employer Contribution (D): {employer_contribution}")
    print(f"Final Tax Relief: €{relief:.2f}")
    print("========================================\n")


if __name__ == "__main__":
    main()
