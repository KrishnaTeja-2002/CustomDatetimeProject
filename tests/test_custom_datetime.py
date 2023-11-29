import datetime
import pytest
from main import MyDatetime  

def test_datetime_creation_no_args():
    # Check if a MyDatetime object is created with the current date and time when no arguments are provided
    datetime_obj_no_args = MyDatetime()
    
    assert isinstance(datetime_obj_no_args, MyDatetime)
    assert datetime_obj_no_args.year == datetime.datetime.utcnow().year
    assert datetime_obj_no_args.month == datetime.datetime.utcnow().month
    assert datetime_obj_no_args.day == datetime.datetime.utcnow().day
    assert datetime_obj_no_args.hour == datetime.datetime.utcnow().hour
    assert datetime_obj_no_args.minute == datetime.datetime.utcnow().minute
    assert datetime_obj_no_args.second == datetime.datetime.utcnow().second

def test_datetime_creation_with_args():
    # Check if a MyDatetime object is created with the provided arguments
    datetime_obj_with_args = MyDatetime(2023, 11, 28, 15, 30, 45)
    
    assert isinstance(datetime_obj_with_args, MyDatetime)
    assert datetime_obj_with_args.year == 2023
    assert datetime_obj_with_args.month == 11
    assert datetime_obj_with_args.day == 28
    assert datetime_obj_with_args.hour == 15
    assert datetime_obj_with_args.minute == 30
    assert datetime_obj_with_args.second == 45

def test_from_iso8601_valid():
    # Check if a MyDatetime object is created from a valid ISO 8601 string
    iso8601_string = "2023-11-28T15:30:45"
    datetime_obj = MyDatetime.from_iso8601(iso8601_string)
    
    assert isinstance(datetime_obj, MyDatetime)
    assert datetime_obj.year == 2023
    assert datetime_obj.month == 11
    assert datetime_obj.day == 28
    assert datetime_obj.hour == 15
    assert datetime_obj.minute == 30
    assert datetime_obj.second == 45

def test_from_iso8601_invalid():
    # Check if ValueError is raised when creating a MyDatetime object from an invalid ISO 8601 string
    invalid_iso8601_string = "invalid"
    with pytest.raises(ValueError):
        MyDatetime.from_iso8601(invalid_iso8601_string)

def test_is_valid_date_valid():
    # Check if a valid date is recognized as valid
    assert MyDatetime.is_valid_date(2023, 11, 28)

def test_is_valid_date_invalid():
    # Check if an invalid date is recognized as invalid
    assert not MyDatetime.is_valid_date(2023, 13, 28)

def test_to_iso8601():
    # Check if the to_iso8601 method returns the expected ISO 8601 string
    datetime_obj = MyDatetime(2023, 11, 28, 15, 30, 45)
    iso8601_string = datetime_obj.to_iso8601()
    assert iso8601_string == "2023-11-28T15:30:45"

def test_to_human_readable():
    # Check if the to_human_readable method returns the expected human-readable string
    datetime_obj = MyDatetime(2023, 11, 28, 15, 30, 45)
    human_readable_string = datetime_obj.to_human_readable()
    assert human_readable_string == "2023-11-28 15:30:45"
