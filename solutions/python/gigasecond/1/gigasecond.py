from datetime import timedelta
def add(moment):
    gigasecond = timedelta(seconds=1_000_000_000)
    new_time = moment + gigasecond
    return new_time
