import sys
import requests
import bs4
import webbrowser

print("Searching....")
res = requests.get('https://google.com/search?q=' + ' '.join("test"))
print(res.raise_for_status())
