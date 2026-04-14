# 📅 Age Calculator Program
from datetime import date, datetime

def calculate_age(birthdate):
    today = date.today()

    # Calculate difference in years, months, and days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust if current month/day is before birth month/day
    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


# 🎯 Main Program
def main():
    print("==== AGE CALCULATOR ====")
    dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")

    try:
        birthdate = datetime.strptime(dob_input, "%Y-%m-%d").date()
        years, months, days = calculate_age(birthdate)

        print("\nYour Age is:")
        print(f"🧭 {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("⚠️ Invalid date format! Please enter in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
