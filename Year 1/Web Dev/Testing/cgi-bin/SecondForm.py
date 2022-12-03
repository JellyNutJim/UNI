#!/usr/bin/python3
import cgi, cgitb 
cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage() 
givenname = form.getvalue('GivenName')
surname = form.getvalue('Surname')
age = form.getvalue('Age')
gender = form.getvalue('Gender')

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title>Second Form</title></head>')
print('<body>')
print('<p>Progress: <progress value="2" max="3"></progress></p>')
print('<form action="Result.py" method="GET">')
# print('<form action="RawIO.py" method="POST">')

print('<fieldset>')
print('  <legend>Preferences</legend>')
print('  music taste: <br/>')
print('  <select name="FavMusic" multiple size="6">')# display 6 lines in total
print('    <optgroup label="English">')
print('      <option value="jackson">Michael Jackson</option>')#please be aware
print('      <option value="madonna">Madonna</option>')#option tag needs closing
print('    </optgroup>')
print('    <optgroup label="French">')
print('      <option value="tal">Tal</option>')
print('      <option value="koxie">Koxie</option>')
print('    </optgroup>')
print('    <optgroup label="German">')
print('      <option value="unheilig">Unheilig</option>')
print('      <option value="rammstein">Rammstein</option>')
print('    </optgroup>')
print('    <optgroup label="Dutch">')
print('      <option value="andrerieu">Andr&eacute; Rieu</option>')
print('      <option value="gabberpiet">Gabber Piet</option>')
print('    </optgroup>')
print('  </select>')
print('  <br/>')
print('  favorite colour: ')
print('  <input type="color" name="FavColour">')
print('</fieldset>')

print('<input type="hidden" name="GivenName" value="%s">' % givenname)
print('<input type="hidden" name="Surname" value="%s">' % surname)
print('<input type="hidden" name="Age" value="%s">' % age)
print('<input type="hidden" name="Gender" value="%s">' % gender)

print('<input type="reset" value="clear">')
print('<input type="submit" value="submit">')

print('</form>')
print('</body>')
print('</html>')
