import datetime

date = datetime.datetime.now()
print(date)

#weekday short name
print(date.strftime("%a"))

#weekday long name
print(date.strftime("%A"))

#weekday number
print(date.strftime("%w"))

#week number
print(date.strftime("%W"))

#day of month
print(date.strftime("%d"))

#month short name
print(date.strftime("%b"))

#month long name
print(date.strftime("%B"))

#month number
print(date.strftime("%m"))

#year shot name
print(date.strftime("%y"))

#year long name
print(date.strftime("%Y"))

#year long name
print(date.strftime("%Y")) 

#hour
print(date.strftime("%H"))

#minute
print(date.strftime("%M"))

#second
print(date.strftime("%S"))

#AM/PM
print(date.strftime("%p"))

#millisecond
print(date.strftime("%f"))

#timezone
print(date.strftime("%Z"))