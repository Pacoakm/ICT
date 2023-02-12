import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from requests.sessions import should_bypass_proxies
from selenium.webdriver.common.action_chains import ActionChains


from bs4 import BeautifulSoup
import requests


import numpy as np
import matplotlib.pyplot as plt

from time import sleep

# create a new Chrome driver
print("Starting...")
driver = webdriver.Chrome()


driver.get("https://www.instagram.com")
input_name = str(input("Please enter your IG username: "))
input_pass = str(input("Please enter your password: "))

print("Logging in. Please wait...")

done = False
while done == False:
    try:
        user_name = driver.find_element(By.NAME, "username")
        user_name.send_keys(input_name)
        done = True
    except:
        pass


sleep(0.5)
user_pass = driver.find_element(By.NAME, "password")
user_pass.send_keys(input_pass)
sleep(0.5)
press_login = driver.find_element(By.XPATH, "//button[@type='submit']")
press_login.click()
sleep(10)

try:
    later = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button",
    )
    later.click()

except:
    pass


done = False
while done == False:
    try:
        later_noti = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        )
        later_noti.click()
        done = True
    except:
        pass


driver.get(f"https://www.instagram.com/{input_name}/followers/")


fol = []

input("Please scoll to the bottom. Press any key to continue...")


req = driver.page_source
soup = BeautifulSoup(req, "html.parser")
divs = soup.select("div._ab8y._ab94._ab97")
for i in divs:
    fol.append(i.text)
fol.sort()
now = datetime.datetime.now()
t = format(now.strftime("%Y-%m-%d_%H-%M-%S"))
filename = f"followers_{input_name}_{t}.txt"

with open(filename, "w") as file:
    # Write each item in the list to a new line in the file
    for item in fol:
        file.write(str(item) + "\n")

print(
    f"A .txt file of {input_name}'s followers at {format(now.strftime('%Y-%m-%d_%H-%M-%S'))} has been saved."
)
driver.quit()
