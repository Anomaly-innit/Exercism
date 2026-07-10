from datetime import datetime, timedelta
import calendar
def delivery_date(start, description):
    
    start = datetime.fromisoformat(start)
    two_hours = timedelta(hours=2)
    if description == "NOW":
        deadline = start + two_hours
        return deadline.isoformat()

    if description == "ASAP" and start.hour < 13:
        deadline = start.replace(hour=17, minute=0, second=0, microsecond=0)
        return deadline.isoformat()
    elif description == "ASAP" and start.hour >= 13:
        deadline = start + timedelta(days=1)
        deadline = deadline.replace(hour=13, minute=0, second=0, microsecond=0)
        return deadline.isoformat()

    if description == "EOW" and start.weekday() in (0, 1, 2):
        days_to_add = 4 - start.weekday()  # Friday is weekday 4
        deadline = start + timedelta(days=days_to_add)
        deadline = deadline.replace(hour=17, minute=0, second=0, microsecond=0)
        return deadline.isoformat()
    elif description == "EOW" and start.weekday() in (3, 4):
        days_to_add = 6 - start.weekday()  # Sunday is weekday 6
        deadline = start + timedelta(days=days_to_add)
        deadline = deadline.replace(hour=20, minute=0, second=0, microsecond=0)
        return deadline.isoformat()
    
    if description.endswith("M"):
        month_num = int(description[:-1])
        if start.month < month_num:
            deadline = first_workday(start.year, month_num)
        elif start.month >= month_num:
            deadline = first_workday(start.year + 1, month_num)
        deadline = deadline.replace(hour=8, minute=0, second=0, microsecond=0)
        return deadline.isoformat()

    if description.startswith("Q"):   
        quarter_num = int(description[1:])
        month_num = quarter_num * 3
        if start.month <= month_num:
            deadline = last_workday(start.year, month_num) 
        elif start.month > month_num:    
            deadline = last_workday(start.year + 1, month_num)
        deadline = deadline.replace(hour=8, minute=0, second=0, microsecond=0)
        return deadline.isoformat()



def first_workday(year, month):
    day = datetime(year, month, 1)
    while day.weekday() >= 5:  
        day += timedelta(days=1)
    return day

def last_workday(year, month):
    last_day_num = calendar.monthrange(year, month)[1]
    day = datetime(year, month, last_day_num)
    while day.weekday() >= 5:
        day -= timedelta(days=1)
    return day