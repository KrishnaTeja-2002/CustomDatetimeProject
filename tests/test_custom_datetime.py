import pytest
from datetime import datetime
from custom_datetime import CustomDatetime, CustomDatetimeSubclass

def test_constructor_with_iso_format():
    dt = CustomDatetime(2023, 11, 25, 12, 30, 45)
    assert dt.to_iso_format() == "2023-11-25T12:30:45"

def test_constructor_with_individual_args():
    dt = CustomDatetime(year=2023, month=11, day=25, hour=12, minute=30, second=45)
    assert dt.to_human_readable_format() == "11/25/2023 12:30:45"

def test_default_values():
    current_datetime = datetime.utcnow()
    dt = CustomDatetime()
    assert dt.year == current_datetime.year
    assert dt.month == current_datetime.month
    assert dt.day == current_datetime.day
    assert dt.hour == current_datetime.hour
    assert dt.minute == current_datetime.minute
    assert dt.second == current_datetime.second

def test_date_validation_valid_date():
    assert CustomDatetime.validate_date(2023, 11, 25) is True

def test_date_validation_invalid_date():
    with pytest.raises(ValueError):
        CustomDatetime.validate_date(2023, 13, 25)

def test_static_method():
    result = CustomDatetime.static_method()
    assert result == "Static method executed."

def test_abstract_method():
    with pytest.raises(TypeError):
        CustomDatetime(2023, 11, 25).abstract_method()

def test_custom_exception_handling():
    dt = CustomDatetime(2023, 11, 25)
    result = dt.custom_exception_handling()
    # Add assertions based on the expected behavior of your exception handling method

def test_class_method_example():
    result = CustomDatetime.class_method_example()
    assert result == "Class method executed for CustomDatetime."
print("Thats good all clear")
