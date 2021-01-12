import requests

status = requests.get('http://wttr.in/')
print(status, type(status))