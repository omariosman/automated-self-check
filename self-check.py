from selenium import webdriver
import time

import os
os.startfile("chromedriver.exe")

time.sleep(2)


web = webdriver.Chrome()
web.get('https://vaccinestatus.aucegypt.edu/CovidSelfCheck/')

time.sleep(2)

########################
# Change this to your username
userName = "username"
userNameElement = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtUserName"]')
userNameElement.send_keys(userName)

########################
# Change this to your password
passWord = "password"
passWordElement = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtPassword"]')
passWordElement.send_keys(passWord)

Submit = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnLogin"]')
Submit.click()


newCairo = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_chkCampus_1"]')
newCairo.click()

noneOfTheAbove1 = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_chkSymptoms_6"]')
noneOfTheAbove1.click()

noneOfTheAbove2 = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_chkContact_2"]')
noneOfTheAbove2.click()

herebyConfirm = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_chkPolicyConfirmation"]')
herebyConfirm.click()

Submit2 = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSubmit"]')
Submit2.click()

time.sleep(2)

submit3 = web.switch_to.alert
submit3.accept()
