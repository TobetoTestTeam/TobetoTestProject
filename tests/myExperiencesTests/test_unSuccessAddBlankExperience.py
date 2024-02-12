# Test Senaryosunun Adı: Profil Bilgileri altında deneyimlerim bölümü bilgi ekleme/güncelleme kontrolleri
# TEST CASE 4: Başarısız deneyim ekleme kontrolü (alanlar boş bırakıldığında)

# Profil Bilgileri -> Deneyimlerim Sayfası 
# https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim

# Generated by Selenium IDE
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import tests.loginTests.test_validLogin as login
import constants.my_experiences_page_constants as gc
from pages.my_experiences_page import MyExperiencesPage
from time import sleep

class TestUnsuccessAddBlankExperience():
  def setup_method(self,logged_in_fixture):
    # as a precondition user should be logged in
    valid_login = login.TestvalidLogin() 
    valid_login.setup_method()
    valid_login.test_validLogin()
    self.driver = valid_login.getDriver()
    
    self.driver.delete_all_cookies
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
    
  #@pytest.mark.skip()
  def test_unSuccessAddBlankExperience(self): # Zorunlu alanlar boş bırakıldığında
     self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim")

     save_button = MyExperiencesPage.get_saveButton_element(self) 
     save_button.click()
     sleep(5)

     corporationName_warningField = MyExperiencesPage.get_corporationNameWarningField_element(self)
     assert corporationName_warningField.text == "Doldurulması zorunlu alan*"
     position_warningField = MyExperiencesPage.get_positionWarningField_element(self)
     assert position_warningField.text == "Doldurulması zorunlu alan*"
     sector_warningField = MyExperiencesPage.get_sectorWarningField_element(self)
     assert sector_warningField.text == "Doldurulması zorunlu alan*"
     startDate_warningField = MyExperiencesPage.get_startDateWarningField_element(self)
     assert startDate_warningField.text == "Doldurulması zorunlu alan*"
     finishDate_warningField = MyExperiencesPage.get_finishDateWarningField_element(self)
     assert finishDate_warningField.text == "Doldurulması zorunlu alan*"
  
