from datetime import datetime
import calendar


def calc_past_years(days_old):
    # calculates full years past
    return days_old // 365


def verify_age(years_old):
    # adds status to different ages
    if years_old > 120:
        return ",ur already dead"
    elif years_old > 60:
        return "old Man"
    elif years_old == 21:
        return ", btw can drink alco in USA"
    elif years_old > 18:
        return "adult"
    elif years_old > 13:
        return "teenager"
    else:
        return "child"


def verify_born_input(born_date):
    # works with input
    try:
        parts = born_date.split()
        if len(parts) == 1:
            year = int(parts[0])
            month, day = 1, 1
        elif len(parts) == 3:
            year, month, day = map(int, parts)
        else:
            return None, "Invalid date format. Use YYYY MM DD"
        days_in_month = calendar.monthrange(year, month)[1]
        if day > days_in_month:
            return None, "Incorrect day value"
        specific_date = datetime(year, month, day)
        if specific_date > datetime.now():
            return None, "Date is in the future"
        return specific_date, None
    except ValueError and OverflowError:
        return None, "Invalid month input"


def is_specific_day(specific_date):
    today = datetime.now()
    if specific_date.month == today.month and specific_date.day == today.day:
        return "Nothing special today"
    else:
        return "You're"


born_date = input("enter born date YYYY MM DD: ")
specific_date, message = verify_born_input(born_date)

if specific_date:
    # calculates, prints and adds message if input was incorrect
    current_date = datetime.now()
    time_difference = (current_date - specific_date).days
    years_old = calc_past_years(time_difference)
    print(
        f"{is_specific_day(specific_date)} {verify_age(years_old)}. You're {years_old} full years, or exactly {time_difference} days old.")
else:
    print(message)