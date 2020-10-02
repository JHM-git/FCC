

time = "3:00 PM"
added_time = "3:10"


def add_time(start, added, day=None):
  weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  split1 = start.split()
  APM = split1[1]
  split2 = split1[0].split(':')
  hours, minutes = int(split2[0]), int(split2[1])
  if APM == 'PM':
    hours = hours + 12
  split3 = added.split(':')
  added_hours, added_minutes = int(split3[0]), int(split3[1])
  total_hours = hours + added_hours
  total_minutes = minutes + added_minutes
  if total_minutes >= 60:
    total_minutes = total_minutes - 60
    total_hours = total_hours + 1
  new_hours = total_hours % 24
  days_passed = int((total_hours - new_hours) / 24)
  days_since = ''
  if days_passed == 1:
    days_since = ' (next day)'
  elif days_passed > 1:
    days_since = ' (' + str(days_passed) + ' days later)'
  if new_hours == 0:
    APM = 'AM'
    new_hours = 12
  elif new_hours < 11:
    APM = 'AM'
  elif new_hours > 12:
    APM = 'PM'
    new_hours = new_hours - 12
  else:
    APM = 'PM'
  hours_str = str(new_hours)
  minutes_str = str(total_minutes)
  if len(minutes_str) == 1:
    minutes_str = '0' + minutes_str
  new_time = hours_str + ':' + minutes_str + ' ' + APM + days_since
  if day:
    weekday = day.lower().title()
    indx = 0
    if days_passed == 0:
      new_time = hours_str + ':' + minutes_str + ' ' + APM + ', ' + weekday + days_since
    elif days_passed > 0:
      indx = weekdays.index(weekday) + days_passed
      if indx > 6:
        indx = indx % 7
    weekday = weekdays[indx]
    new_time = hours_str + ':' + minutes_str + ' ' + APM + ', ' + weekday + days_since
  return new_time