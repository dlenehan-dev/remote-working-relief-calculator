import pytest
from calculations import calculate_relief, is_leap_year
def test_is_leap_year_true():
    assert is_leap_year(2024) is True


def test_is_leap_year_false():
    assert is_leap_year(2023) is False


@pytest.mark.parametrize(
    "year,expected",
    [
        (2024, True),
        (2020, True),
        (2023, False),
        (1900, False),
        (2000, True),
    ],
)
def test_is_leap_year_parametrized(year, expected):
    assert is_leap_year(year) is expected







def test_calculate_relief_non_leap_year():
    relief = calculate_relief(
        total_allowable_bills=3650,
        remote_days=365,
        employer_contribution=0,
        year=2023,
    )

    # (3650 * 365 / 365) * 0.30 = 1095
    assert relief == pytest.approx(1095.0)

def test_calculate_relief_negative_taxable_amount():
    relief = calculate_relief(
        total_allowable_bills=1000,
        remote_days=100,
        employer_contribution=5000,
        year=2024,
    )

    assert relief == 0

