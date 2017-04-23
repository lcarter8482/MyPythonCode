import Epic
import json
import urllib2

again = "y"
while again != "n":
    
    city = Epic.userString("enter a city or zip:")
    units = Epic.userString("f or c:")
    url = 'https://api.apixu.com/v1/current.json?key=c0c6b2e272de41a29ea190336172304&q=%s' % city
    jsonTxt = urllib2.urlopen(url).read()
    weather = json.loads(jsonTxt)

    if units == "f":
        print "Here is the current weather for %s, %s" % (weather['location']['name'], weather['location']['region'])
        print "%s and %s F" % (weather['current']['condition']['text'], weather['current']['temp_f'])
        print "It actually feels like %s F" % weather['current']['feelslike_f']
    elif units == "c":
        print "Here is the current weather for %s, %s" % (weather['location']['name'], weather['location']['region'])
        print "%s and %s C" % (weather['current']['condition']['text'], weather['current']['temp_c'])
        print "It actually feels like %s C" % weather['current']['feelslike_c']
    
    again = Epic.userString("Another location? (y/n)")