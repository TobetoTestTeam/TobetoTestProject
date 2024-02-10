# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
from pages.my_media_account_page import MediaAccountPage
import tests.loginTests.test_validLogin as login

class TestRequiredfield():
  def setup_method(self, method):
    valid_login = login.TestvalidLogin()
    valid_login.setup_method()
    valid_login.test_validLogin()
    self.driver = valid_login.getDriver()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_requiredfield(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim")
    #self.driver.set_window_size(1382, 744)
    #self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div/main/section/div/div/div[2]/div/form/button").click()
    save_button=MediaAccountPage.get_save_button_element(self)
    save_button.click()
    #WebDriverWait(self.driver, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'__next\']/div/main/section/div/div/div[2]/div/form/div/div/span")))
    warning_message1=MediaAccountPage.get_warning_message1_element(self)
    warning_message2=MediaAccountPage.get_warning_message2_element(self)
   
    assert warning_message1.text == "Doldurulması zorunlu alan*"
    assert warning_message2.text == "Doldurulması zorunlu alan*"
  