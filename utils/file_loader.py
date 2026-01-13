"""
File loading utilities for bill data.

This module coordinates CSV loading, logging, and aggregation
of bill values.
"""

from utils.error_handling import (
    MissingFileError,
    NonNumericValueError,
    EmptyFileError,
    safe_read_csv,
)
from utils.logger import setup_logger

logger = setup_logger(__name__)


def load_bill_file(file_path: str) -> float:
    """
    Load a bill CSV file and return the total amount.

    Args:
        file_path: Path to the CSV file.

    Returns:
        Total sum of all numeric values in the file.

    Raises:
        MissingFileError
        NonNumericValueError
        EmptyFileError
    """

    logger.info(f"Reading file: {file_path}")

    values = safe_read_csv(file_path)
    total = sum(values)

    logger.info(f"Loaded {len(values)} entries from {file_path}")
    logger.info(f"Total for {file_path}: {total}")

    return total