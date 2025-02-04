import argparse
import pendulum
from pendulum import DateTime, timezone
from typing import Optional

# ASCII art for fun
CAKE = """
   🎂
  🥂🍾
███████████
█▄█████▄█▄█
█▼▼▼▼▼▼▼▼▼█
█ BirthDay!█
█▲▲▲▲▲▲▲▲▲█
███████████
"""

def get_next_birthday(birthday: DateTime, now: DateTime) -> DateTime:
    """Calculate next birthday, handling leap years and timezones."""
    current_year = now.year
    try:
        next_bday = birthday.replace(year=current_year)
        if next_bday <= now:
            next_bday = birthday.replace(year=current_year + 1)
    except pendulum.exceptions.PendulumException:
        # Handle Feb 29 for non-leap years
        next_bday = birthday.replace(year=current_year, month=3, day=1)
        if next_bday <= now:
            next_bday = birthday.replace(year=current_year + 1, month=3, day=1)
    return next_bday.in_tz(now.timezone_name)

def main():
    try:
        birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
        timezone_str = input("Enter your timezone (optional, e.g., 'Asia/Kolkata'): ")

        if timezone_str:
            try:
                tz = pendulum.timezone(timezone_str)
            except pendulum.tz.exceptions.InvalidTimezone:
                print("Error: Invalid timezone. Please provide a valid timezone.")
                return
        else:
            tz = pendulum.local_timezone()

        now = pendulum.now(tz)
        birthday = pendulum.parse(birthday_str).in_tz(tz)
        next_birthday = get_next_birthday(birthday, now)

        print(CAKE)
        print(f"Your next birthday is on {next_birthday.to_day_datetime_string()} in timezone {tz.name}")
    except pendulum.parsing.exceptions.ParserError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()