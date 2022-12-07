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

    return datetime.date(day = p, month = n, year = 10)
    
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
if (month == 3):
    month = "March"
elif (month == 4):
    month = "April"

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Date of easter in year %s </title>  <link rel="stylesheet" type="text/css" href="../style.css"> </head>' % (year))
print('<body>')
print('<main>')
print('<p class = "day_of_easter">')
if (display_option == "n"):
    print('Easter falls on:<br>%d/%d/%s' % (date.day, date.month, year))
elif(display_option == "v"):
    print('Easter falls on:<br>Sunday The %d<sup>%s</sup> of %s %s' % ( date.day, super_script, month, year))
elif(display_option == "b"):
    print('Easter falls on:<br>%d/%d/%s' % (date.day, date.month, year))
    print('<br>Sunday the %d<sup>%s</sup> of %s %s' % (date.day, super_script, month, year))
print('</p>')
print('<br>')
print('<form action="../index.html">')
print('<input type="submit" value="Back" id="btn">')
print('</form>')
print('</main>')
print('</body>')
print('</html>')
