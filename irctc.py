from selenium import webdriver
from selenium.webdriver.common.by import By
from splinter import Browser
import pandas as pd
import time
#System.setProperty("webdriver.chrome.driver", "C:\Python27\selenium\webdriver\chromedriver");
driver =webdriver.Chrome("C:\Python27\selenium\webdriver\chromedriver")
browser = Browser('chrome')
#browser.driver.set_window_size(640,480)
browser.visit('https://www.irctc.co.in')

user_id_xpath='//*[@id="usernameId"]'
user_id = browser.find_by_xpath(user_id_xpath)[0]
user_id.fill("ramupapa")

passwd_xpath = '//*[@id="loginFormId"]/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/input'
passwd = browser.find_by_xpath(passwd_xpath)[0]
passwd.fill("Shaurya1*")

#captcha_xpath='//*[@id="nlpAnswer"]'
#captcha = browser.find_by_xpath(captcha_xpath)[0]
#captcha.fill("")


time.sleep(10)

element = browser.find_by_xpath('//input[@id="loginbutton"]')
element.click()




source_xpath='//*[@id="jpform:fromStation"]'
source = browser.find_by_xpath(source_xpath)[0]
source.fill("HOWRAH JN - HWH")

dest_xpath='//*[@id="jpform:toStation"]'
dest = browser.find_by_xpath(dest_xpath)[0]
dest.fill("PATNA JN - PNBE")


date_xpath='//*[@id="jpform:journeyDateInputDate"]'
date = browser.find_by_xpath(date_xpath)[0]
date.fill("11-10-2017")


submit_button_xpath = '//*[@id="jpform:jpsubmit"]'
submit_button = browser.find_by_xpath(submit_button_xpath)[0]
submit_button.click()

tatkal_button_xpath = '//*[@id="qcbd"]/table/tbody/tr/td[5]/input'
tatkal_button = browser.find_by_xpath(tatkal_button_xpath)[0]
tatkal_button.click()

class_button_xpath = '//*[@id="cllink-12333-SL-2"]'
class_button = browser.find_by_xpath(class_button_xpath)[0]
class_button.click()

time.sleep(1)

book_button_xpath = '//*[@id="12333-SL-TQ-0"]'
book_button = browser.find_by_xpath(book_button_xpath)[1]
book_button.click()

time.sleep(2)
#page3---------------------------------------------------------------------------------------------

element=browser.find_by_xpath("//*[starts-with(@id,'addPassengerForm:psdetail:0:p')]")
element.fill("mms")

#name_xpath = '//*[contains(@id,'addPassengerForm:psdetail:0:p')]'

#name = browser.find_by_xpath(name_xpath)[0]
#name.fill("Manu Shaurya")


age_xpath = '//*[@id="addPassengerForm:psdetail:0:psgnAge"]'
age = browser.find_by_xpath(age_xpath)[0]
age.fill("22")

element = browser.find_by_id('addPassengerForm:psdetail:0:psgnGender').first
element.select('M')

element = browser.find_by_id('addPassengerForm:psdetail:0:berthChoice').first
element.select('LB')

#gender_xpath = '//*[@id="addPassengerForm:psdetail:0:psgnGender"]'
#gender = browser.find_by_xpath(gender_xpath)[0]
#gender.fill("M")

#berth_xpath = '//*[@id="addPassengerForm:psdetail:0:berthChoice"]'
#berth = browser.find_by_xpath(berth_xpath)[0]
#berth.fill("L")

upgrade_xpath = '//*[@id="addPassengerForm:autoUpgrade"]'
upgrade = browser.find_by_xpath(upgrade_xpath)[0]
upgrade.click()

#captcha1_xpath='//*[@id="nlpAnswer"]'
#captcha1 = browser.find_by_xpath(captcha1_xpath)[0]
#captcha1.fill("")

time.sleep(10)

submit1_button_xpath = '//input[@id="validate" and @value=" Next "]'
submit1_button = browser.find_by_xpath(submit1_button_xpath)[0]
submit1_button.click()

#submit1_button_xpath = '//*[@id="validate"]'
#submit1_button = browser.find_by_xpath(submit1_button_xpath)[4]
#submit1_button.click()

#PAYMENT GATEWAY

#element=browser.find_by_xpath("//*[starts-with(@id,'addPassengerForm:psdetail:0:p')]")
#element.fill("mms")
time.sleep(10)


element = browser.find_by_xpath('//td[@id="CREDIT_CARD"]')
element.click()


element = browser.find_by_xpath('//input[@id="CREDIT_CARD"]')
element.click()

element = browser.find_by_xpath('//input[@id="validate"]')
element.click()


#mode_of_payment_xpath = '//*[@id="CREDIT_CARD"]'
#mode_of_payment = browser.find_by_xpath(mode_of_payment_xpath)[4]
#mode_of_payment.click()

#pay_button_xpath = '//*[@id="validate"]'
#pay_button = browser.find_by_xpath(pay_button_xpath)[4]
#pay_button.click()



#payment page-----------------------------------




element = browser.find_by_xpath('//input[@name="name1"]')
element.fill("manu shaurya")

element = browser.find_by_xpath('//input[@id="creditCrdRadio"]')
element.click()

element = browser.find_by_xpath('//input[@value="VISA|1"]')
element.click()

element = browser.find_by_xpath('//input[@name="CardNumCrd1"]')
element.fill("1234")

element = browser.find_by_xpath('//input[@name="CardNumCrd2"]')
element.fill("1234")

element = browser.find_by_xpath('//input[@name="CardNumCrd3"]')
element.fill("1234")

element = browser.find_by_xpath('//input[@name="CardNumCrd4"]')
element.fill("1234")















