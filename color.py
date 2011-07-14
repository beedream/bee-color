#!/usr/bin/env python
import cgi
  
#link: http://www.javascripter.net/faq/hextorgb.htm  
def hex2rgb(hex):
  if len(hex) != 6: return
  hex = hex.upper()
#  print hex
  r = int(hex[:2], 16)
  g = int(hex[2:4], 16)
  b = int(hex[4:], 16)
  return (r, g, b)

def rgb1scale(rgb):
  return tuple([float(value)/255 for value in list(rgb)])



# HTML content
print "Content-type: text/html"
print
print """<title>Bee Color</title>
<h1>Bee Color</h1>
<h3>A simple color converter</h3>
<hr />"""

# Get Input
form = cgi.FieldStorage()
hex = form.getvalue('hex')
if hex:
  hex = str(hex).upper()
else:
  #KONG: default color
  hex = '0099FF'

#print hex

if hex[0] == '#':
  hex = hex[1:] #trim
  
# Input form
#print '<a href="color.py?hex=0099FF">Link</a>'
print '''
<p>
<form action="color.py" method = "GET">
Hex to RGB color: 
#<input type = "text" width = 40 name = "hex" value = "%s">
<input type = "submit" value = "Convert">
</form>
</p>
''' % hex

# Convertion
if hex:
  rgb = hex2rgb(hex)
  rgb1scale = rgb1scale(rgb)
#  print rgb1scale
  print "<p>Color: <br />"
  print "Hex: %s <br />" % hex
  print "RGB (in 255 scale):  %d %d %d <br />" % rgb
  print "RGB (in 1.0 scale):  %.2f %.2f %.2f <br />" % rgb1scale

print"""
<hr />
<font color = "gray">
Page view: 
<!-- Start of StatCounter Code for DoYourOwnSite -->
<script type="text/javascript">
var sc_project=7043204; 
var sc_invisible=0; 
var sc_security="1f014637"; 
var sc_text=2; 
</script>
<script type="text/javascript"
src="http://www.statcounter.com/counter/counter.js"></script>
<noscript><div class="statcounter"><a title="counter for
vBulletin" href="http://statcounter.com/vbulletin/"
target="_blank"><img class="statcounter"
src="http://c.statcounter.com/7043204/0/1f014637/0/"
alt="counter for vBulletin"></a></div></noscript>
<!-- End of StatCounter Code for DoYourOwnSite -->
</font>
"""