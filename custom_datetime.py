# custom_datetime.py
import datetime

class CustomDatetime:

    def __init__(self, year=None, month=None, day=None, hour=None, minute=None, second=None):
     
      

        if year is None and month is None and day is None and hour is None and minute is None and second is None:
            current_datetime = datetime.datetime.utcnow()
            self.year = current_datetime.year
            self.month = current_datetime.month
            self.day = current_datetime.day
            self.hour = current_datetime.hour
            self.minute = current_datetime.minute
            self.second = current_datetime.second
        else:
            self.year = year or 0
            self.month = month or 0
            self.day = day or 0
            self.hour = hour or 0
            self.minute = minute or 0
            self.second = second or 0

    @classmethod
    def from_iso8601(cls, iso8601_string):
        
        try:
            datetime_obj = datetime.datetime.fromisoformat(iso8601_string)
            return cls(datetime_obj.year, datetime_obj.month, datetime_obj.day,
                       datetime_obj.hour, datetime_obj.minute, datetime_obj.second)
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 format: {iso8601_string}")

    @staticmethod
    def is_valid_date(year, month, day):
        """
        Checks whether the given set of date arguments (day, month, year) forms a valid date.

        Args:
            year (int): The year of the date.
            month (int): The month of the date (1-12).
            day (int): The day of the month (1-31).

        Returns:
            bool: True if the given date is valid, False otherwise.
        """

        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    def to_iso8601(self):
        return datetime.datetime(
            self.year, 
            self.month,
            self.day,
            self.hour,
            self.minute, 
            self.second
        ).isoformat()

    def to_human_readable(self):
        

        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

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
        return f"CustomDatetime(year={self.year}, month={self.month}, day={self.day}, " \
               f"hour={self.hour}, minute={self.minute}, second={self.second})"

    @classmethod
    def from_string(cls, date_string):
        
        try:
            date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return cls(date_obj.year, date_obj.month, date_obj.day,
                       date_obj.hour, date_obj.minute, date
