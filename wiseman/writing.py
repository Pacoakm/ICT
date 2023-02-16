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
from main import *

print("Starting...")
driver = webdriver.Edge()
driver.get("https://lms.wiseman.com.hk/lms/user/")

login()
