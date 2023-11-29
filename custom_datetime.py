import datetime

class MyDatetime:

    def __init__(self, year=None, month=None, day=None, hour=None, minute=None, second=None):
        

        if all(value is None for value in (year, month, day, hour, minute, second)):
            current_datetime = datetime.datetime.utcnow()
            self.year, self.month, self.day = current_datetime.year, current_datetime.month, current_datetime.day
            self.hour, self.minute, self.second = current_datetime.hour, current_datetime.minute, current_datetime.second
        else:
            self.year = year or 0
            self.month = month or 0
            self.day = day if day is not None else 0
            self.hour = hour or 0
            self.minute = minute or 0
            self.second = second or 0

    @classmethod
    def from_iso8601(cls, iso8601_string):
        

        try:
            datetime_obj = datetime.datetime.fromisoformat(iso8601_string)
            return cls(year=datetime_obj.year, month=datetime_obj.month, day=datetime_obj.day,
                       hour=datetime_obj.hour, minute=datetime_obj.minute, second=datetime_obj.second)
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 format: {iso8601_string}")

    @staticmethod
    def is_valid_date(year, month, day):
       

        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    def to_iso8601(self):
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second).isoformat()

    def to_human_readable(self):
        

        return f"{self.year}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    @classmethod
    def validate_date(cls, year, month, day):
        
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Both arguments must be instances of the Datetime class.")

        delta = abs(date1.to_datetime() - date2.to_datetime())

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return delta.days // 30

    def __repr__(self):
        return f"Datetime(year={self.year}, month={self.month}, day={self.day}, " \
               f"hour={self.hour}, minute={self.minute}, second={self.second})"

    @classmethod
    def from_string(cls, date_string):
       
        try:
            date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return cls(year=date_obj.year, month=date_obj.month, day=date_obj.day,
                       hour=date_obj.hour, minute=date_obj.minute, second=date_obj.second)
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_string}")

    @staticmethod
    def format_iso8601(date_obj):
       
        return date_obj.to_iso8601()

    @staticmethod
    def format_human_readable(date_obj):
       
        return date_obj.to_human_readable()

    @staticmethod
    def convert_between_calendars(date_obj, from_calendar, to_calendar):
        pass

    @staticmethod
    def calculate_weekday(date_obj):
       
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[date_obj.to_datetime().weekday()]

    def to_datetime(self):
        
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)


# Example usage:

# Creating a Datetime object without arguments (defaults to the current date and time)
datetime_obj_no_args = MyDatetime()
print(datetime_obj_no_args.to_human_readable())
print(datetime_obj_no_args
