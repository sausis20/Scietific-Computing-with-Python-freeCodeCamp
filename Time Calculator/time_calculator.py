def add_time(start, duration, starting_day=""):
    # Separate the time into hours and minutes
    pieces = start.split()
    time = pieces[0].split(":")
    ampm = pieces[1]
    
    # Separate the duration into hours and minutes
    duration_pieces = duration.split(":")
    
    # Calculate the time in 24-hour format
    if ampm == "PM":
        time[0] = int(time[0]) + 12
    
    # Add days, hours and minutes    
    ending_h = int(time[0]) + int(duration_pieces[0])
    ending_min = int(time[1]) + int(duration_pieces[1])

    days_add = 0
    
    if ending_min >= 60:
        hours_add = ending_min // 60
        ending_min -= hours_add * 60
        ending_h += hours_add
    
    if ending_h > 24:
        days_add = ending_h // 24
        ending_h -= days_add * 24
        
    # Find AM or PM
    # Return to 12-hour clock format
    
    if ending_h > 12:
        ending_h -= 12
        ampm = "PM"
    elif ending_h == 12:
        ampm = "PM"
    elif ending_h > 0 and ending_h < 12:
        ampm = "AM"
    else: #ending_h == 0
        ampm = "AM"
        ending_h += 12
    
    # Find days later
    if days_add > 0:
        if days_add == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(days_add) + " days later)"
    else:
        days_later = ""
    
    # Find week day
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday')
    
    if starting_day:
        b = int(days_add) + weekdays.index(starting_day.title())
        c = b // 7
        b = b - c * 7
        end_day = str(", " + weekdays[b])
    else:
        end_day = starting_day
    
    
    
    new_time = str(ending_h) + ":" + \
        (str(ending_min) if ending_min > 9 else ("0" + str(ending_min))) + \
        " " + ampm + "" + end_day + days_later
        
    return new_time