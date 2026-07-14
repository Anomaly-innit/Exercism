import calendar
from datetime import date
class MeetupDayException(ValueError):
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    WEEKDAYS = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
    "Friday": 4, "Saturday": 5, "Sunday": 6
}
    target_weekday = WEEKDAYS[day_of_week]
    days_in_month = calendar.monthrange(year, month)[1]
    
    matching_dates = []
    for day in range(1, days_in_month + 1):
        current_date = date(year, month, day)
        if current_date.weekday() == target_weekday:
            matching_dates.append(current_date) 
            
    if week == "teenth":
        for d in matching_dates:
            if 13 <= d.day <= 19:
                return d
    elif week == "first":
        return matching_dates[0]
    elif week == "second":
        return matching_dates[1]
    elif week == "third":
        return matching_dates[2]
    elif week == "fourth":
        return matching_dates[3]
    elif week == "fifth":
        if len(matching_dates) < 5:
            raise MeetupDayException("That day does not exist.")
        return matching_dates[4]
    elif week == "last":
        return matching_dates[-1]
            