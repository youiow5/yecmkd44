from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import secrets
import random
import string
import os

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


###TEMP-NAMES###
t0 = random.randint(4,38)
t = random.randint(20,28)
t1 = random.randint(6,10)
t2 = random.randint(15,25)
t3 = random.randint(26,40)
driver = webdriver.Chrome(options=options)



####TRX-GENERATOR###

res = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=28))

res1=''.join(random.choices(string.digits, k=4))

res0=''.join(random.choices(string.ascii_uppercase, k=1))

nl = ( str(res1) + str(res))
fbl = random.sample(nl,k=32)
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
tr=(listToString(fbl))
trx=('T'+str(res0)+tr)

time.sleep(t0)
driver.get("https://trxminer.fun/?ref=122182")
time.sleep(t)
driver.find_element(By.ID,"icon_prefix2").click()
time.sleep(t1)
driver.find_element(By.ID,"icon_prefix2").send_keys(trx)
time.sleep(t2)
driver.find_element(By.CLASS_NAME, "but_enter.btn-large.waves-effect.waves-light.red").click()
time.sleep(t3)






