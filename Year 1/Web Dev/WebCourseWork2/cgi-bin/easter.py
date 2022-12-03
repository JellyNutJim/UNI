#!/usr/bin/python3
import cgi, cgitb
import datetime
cgitb.enable()
form = cgi.FieldStorage()

year = form.getvalue('year')
display_option = form.getvalue('date_options')

def Easter(y):
    a = y % 19   
    b = y // 100   
    c = y % 100   
    d = b // 4   
    e = b % 4   
    g = (8 * b + 13) // 25   
    h = (19 * a + b - d - g + 15) % 30   
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return datetime.date(day = p, month = n, year = y)
    
date = Easter(int(year))    

# Get correct superscript
super_script = "th"
if (date.day not in [11, 12, 13]):
    d = date.day % 10
    if (d == 1):
        super_script = "st"
    elif (d == 2):
        super_script = "nd"
    elif (d == 3):
        super_script = "rd"

# Get Correct Month
month = date.month
if (month == 1):
    month = "January"
elif (month == 2):
    month = "Febuary"
elif (month == 3):
    month = "March"
elif (month == 4):
    month = "April"
elif (month == 5):
    month = "May"
elif (month == 6):
    month = "June"
elif (month == 7):
    month = "July"
elif (month == 8):
    month = "August"
elif (month == 9):
    month = "September"
elif (month == 10):
    month = "October"
elif (month == 11):
    month = "November"
elif (month == 12):
    month = "December"


print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Date of easter in year %s </title>  </head>' % (year))
print('<body>')
print('<p>')
if (display_option == "n"):
    print('Easter falls on: %d/%d/%d' % (date.day, date.month, date.year))
elif(display_option == "v"):
    print('Easter falls on: Sunday The %d<sup>%s</sup> of %s %d' % ( date.day, super_script, month, date.year))
elif(display_option == "b"):
    print('Easter falls on: %d/%d/%d' % (date.day, date.month, date.year))
    print('<br>Easter falls on: Sunday The %d<sup>%s</sup> of %s %d' % (date.day, super_script, month, date.year))
print('</p>')
print('</body>')
print('</html>')
