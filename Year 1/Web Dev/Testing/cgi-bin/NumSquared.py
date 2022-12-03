#!/usr/bin/python3
import cgi #, cgitb
# cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage() 
num1 = form.getvalue('theNumber')
squared = float(num1)**2

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Python script to output the square of a number </title>  </head>')
print('<body>')
print('<p>')
print('The square of %s is %g' % (num1, squared))
print('</p>')
print('</body>')
print('</html>')
