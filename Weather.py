import Epic
import json
import urllib2
import time

def main():
    again = "y"
    while again != "n":
        city = Epic.userString("\nEnter a city or zip code:")
        units = Epic.userString("Would you like Fahrenheit (f) or Celsius (c)? ")
        weather = getJson(city)
        if units == "f": #runs Fahrenheit sort
            jsonSortF(weather)
        elif units == "c": #runs Celsius sort
            jsonSortC(weather)
        again = Epic.userString("Would you like to enter another location? (y/n):")
        
def getJson(city):
    url = 'https://api.apixu.com/v1/forecast.json?key=c0c6b2e272de41a29ea190336172304&q=%s' % city
    jsonTxt = urllib2.urlopen(url).read()
    weather = json.loads(jsonTxt)
    return weather
    
def jsonSortF(weather): #prints Fahrenheit output
    print "\nHere is the current weather for %s, %s" % (weather['location']['name'], weather['location']['region'])
    print "%s and %s F" % (weather['current']['condition']['text'], weather['current']['temp_f'])
    print "It actually feels like %s F" % weather['current']['feelslike_f']
    print "\nThe weather forecast for today, %s:" % time.strftime("%m/%d/%Y")#prints current date
    print "The high for today is: %s F" % weather['forecast']['forecastday'][0]['day']['maxtemp_f']
    print "The low for today is: %s F" % weather['forecast']['forecastday'][0]['day']['mintemp_f']
    print "Sunrise: %s" % weather['forecast']['forecastday'][0]['astro']['sunrise']
    print "Sunset: %s" % weather['forecast']['forecastday'][0]['astro']['sunset']
    
def jsonSortC(weather): #prints Celsius output
    print "\nHere is the current weather for %s, %s" % (weather['location']['name'], weather['location']['region'])
    print "%s and %s C" % (weather['current']['condition']['text'], weather['current']['temp_c'])
    print "It actually feels like %s C" % weather['current']['feelslike_c']
    print "\nThe weather forecast for today, %s:" % time.strftime("%m/%d/%Y")#prints current date
    print "The high for today is: %s C" % weather['forecast']['forecastday'][0]['day']['maxtemp_c']
    print "The low for today is: %s C" % weather['forecast']['forecastday'][0]['day']['mintemp_c']
    print "Sunrise: %s" % weather['forecast']['forecastday'][0]['astro']['sunrise']
    print "Sunset: %s" % weather['forecast']['forecastday'][0]['astro']['sunset']
    
main()