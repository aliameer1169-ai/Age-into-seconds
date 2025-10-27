from datetime import datetime
from dateutil import parser

def calculate_age_in_seconds(birthdate_str):
    """
    Calculates the age in seconds based on the given birthdate string.
    Example input format: 'YYYY-MM-DD'
    """
    try:
        birthdate = parser.parse(birthdate_str)
        now = datetime.now()
        age_in_seconds = (now - birthdate).total_seconds()
        return age_in_seconds
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("=== Age to Seconds Calculator ===")
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    result = calculate_age_in_seconds(birthdate_input)
    
    if isinstance(result, float):
        print(f"Your age in seconds is approximately {int(result):,} seconds.")
    else:
        print(result)
