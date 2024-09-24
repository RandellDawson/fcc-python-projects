def get_time_dict(time):
    hours, minutes = time.split(':')
    am_pm = minutes[-2:]
    if not am_pm.isdigit():
        minutes, am_pm = minutes.split(' ')
    hours = int(hours) if am_pm == 'AM'
    minutes = int(minutes)
    return { "hours": hours, "minutes": minutes, "am_pm": am_pm }

def add_time(start, duration):
    start_time_dict = get_time_dict(start)
    add_time_dict = get_time_dict(duration)
    minutes_to_add = add_time_dict["hours"] * 60 + add_time_dict["minutes"]
    new_minutes_tuple = divmod(start_time_dict["minutes"], add_time_dict["minutes"])
    print(new_minutes_tuple)
    start_time_in_mins = start_time_dict["hours"] * 60 + start_time_dict["minutes"]
    print(start_time_in_mins)


    return lhs