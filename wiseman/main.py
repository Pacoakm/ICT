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


input_name = input("Your wiseman login name: ")
input_pass = input("Your password: ")


def login():
    driver.set_network_conditions(
        offline=False,
        latency=1,
        download_throughput=500 * 1024,
        upload_throughput=500 * 1024,
    )
    driver.get("https://lms.wiseman.com.hk/lms/user/")
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
    driver.get(
        "https://lms.wiseman.com.hk/lms/user/secure/course/eb/select_theme/lessons.shtml"
    )
    return


login()
while True:
    submit_button = 0
    next_button = 0

    ans = []
    input_lesson = input("Input the lesson link: ")
    driver.get(input_lesson)
    sleep(5)
    for i in range(20):
        if i == 0:
            driver.set_network_conditions(
                offline=True, latency=100000, download_throughput=0, upload_throughput=0
            )
        sleep(0.5)
        skip_alert()

        if i == 0:
            frame = WebDriverWait(driver, 7).until(
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
        skip_alert()
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.select("span.fix-answer.ng-star-inserted")
        for i in divs:
            temp = i.text
            if "/" in temp:
                temp = temp[0 : temp.index("/") - 1]
            ans.append(temp)
        skip_alert()
        try:
            next_button = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "float-right.next.btn-r.ng-star-inserted")
                )
            )
            next_button.click()
        except:
            break
        sleep(0.2)
        skip_alert()

    print(ans)
    skip_alert()
    for _ in range(15):
        try:
            driver.execute_script("window.open('');")
            break
        except:
            skip_alert()
            pass
    driver.delete_all_cookies()

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    driver.set_network_conditions(
        offline=False,
        latency=1,
        download_throughput=500 * 1024,
        upload_throughput=500 * 1024,
    )
    login()
    driver.get(input_lesson)

    for i in range(20):
        sleep(0.5)
        if i == 0:
            frame = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#course"))
            )
            driver.switch_to.frame(frame)
        try:
            next_button = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "float-right.next.btn-r.ng-star-inserted")
                )
            )
            next_button.click()
            sleep(0.5)
        except:
            pass
        try:
            input_ans = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        'input[autocomplete="off"][class="ng-untouched ng-pristine ng-valid ng-star-inserted"]',
                    )
                )
            )
        except:
            pass

        try:
            input_ans.send_keys(ans[i])
        except:
            pass

        submit_button = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "float-right.submit.btn-r.ng-star-inserted")
            )
        )
        try:
            submit_button.click()
        except:
            pass
        sleep(0.5)

        try:
            next_button = WebDriverWait(driver, 4).until(
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
    contin = input("Press q to end the program or other keys to continue... ")
    if contin == "q":
        break

sleep(1000)
