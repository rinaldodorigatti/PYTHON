
import os
import urllib3

from selenium import webdriver

print("Testing Internet Connection")
print()
try:
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://google.com')
    print("Internet is working fine!", r.status)
    print()
    question = input("Do you want to open a website? (Y/N): ")
    if question == "Y" or question == "y":
        print()
        search = input("Input website to open (http://website.com) : ")
    else:
        exit(0)
except urllib3.exceptions.ConnectionError as e:
    print("No internet connection!", e)

browser = webdriver.Chrome()
browser.get(search)
# os.system("clear")
print("[+] Website " + search + " opened!")
browser.fullscreen_window()
search_bar = browser.find_element('q')
print(search_bar)
# browser.close()
