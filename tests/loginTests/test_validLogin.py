# Login Page 
# https://tobeto.com/giris

# Generated by Selenium IDE
import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage

import os
from dotenv import load_dotenv
load_dotenv()

import constants.globalConstants as gc

class TestvalidLogin():
  def setup_method(self):
    #self.driver = webdriver.Chrome()
    #self.driver.get("https://tobeto.com/giris")

    LoginPage.gotoPage(self)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()

  def getDriver(self):
    return self.driver
  
  def test_validLogin(self):
    
    user_email = LoginPage.get_username_element(self)
    user_email.send_keys(gc.USER_MAIL)
    user_password = LoginPage.get_password_element(self)
    user_password.send_keys(gc.USER_PASSWORD)
    giris_button = LoginPage.get_girisButton_element(self)
    giris_button.click()
    #self.driver.execute_script("arguments[0].click();", register_button1)

    toast_message_text = WebDriverWait(self.driver, 500).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body"))).text
    assert toast_message_text == "• Giriş başarılı."
    sleep(5)