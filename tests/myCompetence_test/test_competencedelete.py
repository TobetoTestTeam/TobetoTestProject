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

import tests.loginTests.test_validLogin as login
from pages.competence import Competence_delete
from pages.competence import competence_add

from time import sleep


class TestCompetencedelete():
  def setup_method(self):
    # as a precondition user should be logged in
    valid_login = login.TestvalidLogin() 
    valid_login.setup_method()
    valid_login.test_validLogin()
    self.driver = valid_login.getDriver()
    
    self.driver.delete_all_cookies
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_competencedelete(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim")
    self.driver.set_window_size(1552, 832)

    competence_delete = Competence_delete.get_competence_delete(self)
    competence_delete.click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert-message").text == "Seçilen yetkinliği silmek istediğinize emin misiniz?"
    delete_button = Competence_delete.get_delete_button(self)
    delete_button.click()
    toast_message = Competence_delete.get_toast_message(self)
    assert toast_message.text =="• Yetenek kaldırıldı."
    sleep(5)
