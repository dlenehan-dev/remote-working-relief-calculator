"""
Core business logic for calculating remote working tax relief.
"""

def is_leap_year(year: int) -> bool:
    """
    Determine whether a given year is a leap year.

    Args:
        year: Year to evaluate.

    Returns:
        True if leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



def calculate_relief(
    total_allowable_bills: float,
    remote_days: int,
    employer_contribution: float,
    year: int
) -> float:
    """
    Calculate remote working tax relief.

    Revenue formula:
        ((A × B) ÷ C – D) × 0.30

    Where:
        A = allowable bills
        B = remote working days
        C = days in year (365 or 366)
        D = employer contribution

    Args:
        total_allowable_bills: Sum of allowable utility bills.
        remote_days: Number of days worked remotely.
        employer_contribution: Employer-paid contribution.
        year: Tax year being claimed.

    Returns:
        Calculated tax relief amount.
    """



    days_in_year = 366 if is_leap_year(year) else 365

    base_amount = (total_allowable_bills * remote_days) / days_in_year
    taxable_relief = base_amount - employer_contribution

    if taxable_relief < 0:
        taxable_relief = 0

    return taxable_relief * 0.30