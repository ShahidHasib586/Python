import calendar
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,6,3,1))#for getting data of calender, print matrix, print(calendar.monthcalendar(2020,6))



print(calendar.calendar(2020,5,2,2))#print entire year 

x = (calendar.monthcalendar(2020,6)) 
print(x)
y = (calendar.monthcalendar(2020,7)) 
print(y)
z = [x,y]
print(z)# for getting all month data
print()
print()

the_specific_day = calendar.weekday(2020,6,11)#print the day
print(the_specific_day)

is_leap = calendar.isleap(3040)
print(is_leap)

is_leap == True

print("hi baby")

how_many_leapdays = calendar.leapdays(2000,3000)
print(how_many_leapdays)