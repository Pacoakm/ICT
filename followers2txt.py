import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from requests.sessions import should_bypass_proxies
from selenium.webdriver.common.action_chains import ActionChains

# import required modules
from bs4 import BeautifulSoup
import requests
import pandas as pd


import numpy as np
import matplotlib.pyplot as plt

from time import sleep

# create a new Chrome driver
print("Starting...")
driver = webdriver.Chrome()
input_name = str(input("Please enter your IG username: "))
input_pass = str(input("Please enter your password: "))


driver.get("https://www.instagram.com")
print("Logging in. Please wait...")
sleep(6)
user_name = driver.find_element(By.NAME, "username")
user_name.send_keys(input_name)
sleep(0.5)
user_pass = driver.find_element(By.NAME, "password")
user_pass.send_keys(input_pass)
sleep(0.5)
press_login = driver.find_element(By.XPATH, "//button[@type='submit']")
press_login.click()
sleep(15)
try:
    later = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button",
    )
    later.click()
except:
    pass
sleep(6)
try:
    later_noti = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
    )
    later_noti.click()
except:
    pass


driver.get("https://www.instagram.com/pacoakm/followers/")


fol = []

input("Please scoll to the bottom. Press any key to continue...")


req = driver.page_source
soup = BeautifulSoup(req, "html.parser")
divs = soup.select("div._ab8y._ab94._ab97")
for i in divs:
    fol.append(i.text)
fol.sort()
now = datetime.datetime.now()
filename = "followers_{}.txt".format(now.strftime("%Y-%m-%d_%H-%M-%S"))

with open(filename, "w") as file:
    # Write each item in the list to a new line in the file
    for item in fol:
        file.write(str(item) + "\n")

print(
    f"A .txt file of followers at {format(now.strftime('%Y-%m-%d_%H-%M-%S'))} has been saved"
)
