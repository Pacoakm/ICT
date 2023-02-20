import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from requests.sessions import should_bypass_proxies
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# create a new Chrome driver
print("Starting...")


options = Options()
options.headless = False
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)


def skip_alert():
    try:
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
    except:
        pass


def login():
    driver.set_network_conditions(
        offline=False,
        latency=10,
        download_throughput=500 * 1024,
        upload_throughput=500 * 1024,
    )
    driver.get("https://lms.wiseman.com.hk/lms/user/")
    input_name = "sy.sy10395"
    input_pass = "2022"
    print("Logging in. Please wait...")
    while True:
        try:
            user_name = driver.find_element(By.NAME, "username")
            user_name.send_keys(input_name)

            sleep(0.5)

            password = driver.find_element(By.NAME, "password")
            password.send_keys(input_pass)

            sleep(0.5)

            login_button = driver.find_element(
                By.XPATH,
                "/html/body/section/div/div/div/form/div[6]/div/button",
            )
            login_button.click()

            break
        except:
            pass
    while True:
        try:
            lessonlist_button = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[3]/div[1]/div/p[2]/a",
            )
            lessonlist_button.click()
            break
        except:
            pass
    return


login()
submit_button = 0
next_button = 0
input_lesson = input("Input the lesson link...")
ans = []
driver.get(input_lesson)
sleep(3)
for i in range(20):
    if i == 2:
        driver.set_network_conditions(
            offline=True, latency=100000, download_throughput=0, upload_throughput=0
        )
    sleep(0.5)
    skip_alert()

    if i == 0:
        frame = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#course"))
        )
        driver.switch_to.frame(frame)
    skip_alert()

    while True:
        try:
            submit_button = driver.find_element(
                By.CLASS_NAME, "float-right.submit.btn-r.ng-star-inserted"
            )
            submit_button.click()
            break
        except:
            pass
    sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.select("span.fix-answer.ng-star-inserted")
    for i in divs:
        ans.append(i.text)
    skip_alert()
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "float-right.next.btn-r.ng-star-inserted")
            )
        )
        next_button.click()
    except:
        break
    sleep(0.5)
    skip_alert()

print(ans)

driver.execute_script("window.open('');")
driver.delete_all_cookies()
driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.set_network_conditions(
    offline=False,
    latency=10,
    download_throughput=500 * 1024,
    upload_throughput=500 * 1024,
)
login()
driver.get(input_lesson)

for i in range(20):
    sleep(0.5)
    if i == 0:
        frame = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#course"))
        )
        driver.switch_to.frame(frame)

    while True:
        driver.switch_to.frame(frame)
        try:
            input_ans = driver.find_element(
                By.CSS_SELECTOR,
                'input[autocomplete="off"][class="ng-untouched ng-pristine ng-valid ng-star-inserted"]',
            )
            input_ans.send_keys(ans[i])
            break
        except:
            pass
    while True:
        try:
            submit_button = driver.find_element(
                By.CLASS_NAME, "float-right.submit.btn-r.ng-star-inserted"
            )
            submit_button.click()
            break
        except:
            pass
    sleep(0.5)

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "float-right.next.btn-r.ng-star-inserted")
            )
        )
        next_button.click()
        sleep(0.5)
    except:
        break
sleep(0.5)
driver.get(
    "https://lms.wiseman.com.hk/lms/user/secure/course/eb/select_theme/lessons.shtml"
)
sleep(1000)
