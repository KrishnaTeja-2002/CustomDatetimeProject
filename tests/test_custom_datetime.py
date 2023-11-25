# tests/test_custom_datetime.py
import pytest
from custom_datetime import CustomDatetime

def test_constructor_with_iso_format():
    dt = CustomDatetime(2023, 11, 25, 12, 30, 45)
    assert dt.to_iso_format() == "2023-11-25T12:30:45"

def test_constructor_with_individual_args():
    dt = CustomDatetime(year=2023, month=11, day=25, hour=12, minute=30, second=45)
    assert dt.to_human_readable_format() == "11/25/2023 12:30:45"
