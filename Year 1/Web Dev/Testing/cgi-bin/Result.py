#!/usr/bin/python3
import cgi, cgitb, os
cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage() 
givenname = form.getvalue('GivenName')
surname = form.getvalue('Surname')
age = form.getvalue('Age')
gender = form.getvalue('Gender')
favmusic = form.getlist('FavMusic')
# getlist always returns a list, even if there's just one (or zero) element
favcolour = form.getvalue('FavColour')

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title>Results</title></head>')
print('<body>')
print('<p>Progress: <progress value="3" max="3"></progress></p>')
print('<h1>results</h1>')
print('<p>You filled in the following data:<br/>')

print('Given Name: %s <br/>' % givenname)
print('Surname: %s <br/>' % surname)
print('Age: %s <br/>' % age)
print('Gender: %s <br/>' % gender)
for artist in favmusic:
	print('Favourite music artist: %s <br/>' % artist)
print('Favourite color: %s </p>' % favcolour)

print('<p>By the way, your browser is %s <br/>' % os.environ["HTTP_USER_AGENT"])
print('and your IP address is %s </p>' % os.environ["REMOTE_ADDR"])
# we use os.environ to read the environment variables used by the web server

print('</body>')
print('</html>')
