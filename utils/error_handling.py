"""
Custom exceptions and safe CSV loading utilities.

This module provides reusable error types and a defensive CSV
reader used throughout the application.
"""

import csv

class MissingFileError(Exception):
    """Raised when an expected CSV file cannot be found."""
    pass


class NonNumericValueError(Exception):
    """Raised when a CSV file contains non-numeric data."""
    pass

class EmptyFileError(Exception):
    """Raised when a CSV file contains no usable numeric values."""
    pass


def safe_read_csv(file_path: str) -> list[float]:
    """
    Safely read numeric values from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A list of numeric values read from the file.

    Raises:
        MissingFileError: If the file does not exist.
        NonNumericValueError: If a non-numeric value is encountered.
        EmptyFileError: If no numeric values are found.
    """

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            values = []

            for row in reader:
                if not row:
                    continue
                try:
                    num = float(row[0])
                    values.append(num)
                except ValueError:
                    raise NonNumericValueError(
                        f"Non-numeric value in {file_path}: {row}"
                    )

            if not values:
                raise EmptyFileError(f"File '{file_path}' contains no numeric data.")

            return values

    except FileNotFoundError:
        raise MissingFileError(f"File not found: {file_path}")