from abc import ABC, abstractmethod
from datetime import datetime

class CustomDatetime(ABC):
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_iso_format(self):
        result = f"{self.year}-{self.month:02d}-{self.day:02d}T{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        print("to_iso_format:", result)
        return result

    def to_human_readable_format(self):
        result = f"{self.month:02d}/{self.day:02d}/{self.year} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        print("to_human_readable_format:", result)
        return result

    @staticmethod
    def static_method():
        result = "Static method executed."
        print("static_method:", result)
        return result

    @classmethod
    def class_method_example(cls):
        result = f"Class method executed for {cls.__name__}."
        print("class_method_example:", result)
        return result

    @abstractmethod
    def abstract_method(self):
        result = "Abstract method executed."
        print("abstract_method:", result)
        return result

    @staticmethod
    def validate_date(year, month, day):
        # Static method for date validation
        if 1 <= month <= 12 and 1 <= day <= 31:
            print("validate_date: Valid date.")
            return True
        else:
            raise ValueError("validate_date: Invalid date")

    def custom_exception_handling(self):
        try:
            # Actual code that might raise an exception
            result = self.year / (self.month - 12)
            print("custom_exception_handling:", result)
            return result
        except Exception as e:
            # Handle the exception and provide an informative error message
            result = f"custom_exception_handling: Error - {str(e)}"
            print(result)
            return result

# Example subclass implementing the abstract method
class CustomDatetimeSubclass(CustomDatetime):
    def abstract_method(self):
        result = "CustomDatetimeSubclass abstract method executed."
        print("CustomDatetimeSubclass abstract_method:", result)
        return result
