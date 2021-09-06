import requests 

print("\nRequests library version:")
print(requests.__version__)

print("\nGet google webpage:")
page = requests.get('http://google.com/')
print(page)

print("\nPython script:\n")
script = requests.get('https://raw.githubusercontent.com/xyL3/404Lab1/main/lab1.py')
print(script.text)