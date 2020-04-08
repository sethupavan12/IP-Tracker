#!/usr/bin/python3
import json
from urllib.request import urlopen
import os
import cgi,cgitb

cgitb.enable()
form = cgi.FieldStorage()
ip = (form.getvalue("IP"))

print('Content-Type:text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<head> <title> IP Tracker </title> </head>')
print('<link rel="stylesheet" type="text/css" href="../style.css">')
print('<body>')
print('<h1>Your IP details are :</h1>')
def iptrack(ip):
  while True:
    try:
       url = "http://ip-api.com/json/"
       trackedip = urlopen(url + ip)
       data = trackedip.read()
       values = json.loads(data)
       print('<p>')

       print("City: " + values['city'])
       print('</p>')
       print('<p>')

       print("Country: " + values['country'])
       print('</p>')
       print('<p>')
       print("Name of the region: " + values['regionName'])
       print('</p>')
       print('<p>')
       print("Region: " + values['region'])
       print('</p>')
       print('<p>')
       print("ISP: " + values['isp'])
       print('</p>')
       print('<p>')
       print("ZIP Code: " + values['zip'])
       print('</p>')


       break
    except:
        print("Make sure you entered a correct IP Address.")

iptrack(ip)


print('<small>Made By Sethu Pavan</small>')
print('</body>')
print('</html>')