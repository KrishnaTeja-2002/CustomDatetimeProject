# custom_datetime.py
class CustomDatetime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}T{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def to_human_readable_format(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
