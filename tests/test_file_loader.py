import pytest
from utils.file_loader import load_bill_file
from utils.error_handling import MissingFileError, EmptyFileError

def test_missing_file_raises_error():
    with pytest.raises(MissingFileError):
        load_bill_file("data/does_not_exist.csv")

def test_empty_file_raises_error():
    with pytest.raises(EmptyFileError):
        load_bill_file("tests/data/empty.csv")

def test_load_bill_file_valid(tmp_path):
    test_file = tmp_path / "test.csv"
    test_file.write_text("10\n20\n30\n")

    total = load_bill_file(str(test_file))

    assert total == 60
