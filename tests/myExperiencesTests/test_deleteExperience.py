# Test Senaryosunun Adı: Profil Bilgileri altında deneyimlerim bölümü bilgi ekleme/güncelleme kontrolleri
# TEST CASE 2: Eklenen deneyimin açıklaması görüntülenmesi ve deneyimin silinmesi kontrolü

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

class TestDeleteExperience():
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
  def test_deleteExperience(self):
      
      self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim")

      self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
      sleep(2)
      three_dots_button = MyExperiencesPage.get_threeDotsButton_element(self)
      sleep(2)
      three_dots_button.click()
      job_desc = MyExperiencesPage.get_jobDesc_element(self)
      assert job_desc.text == "İş Açıklaması"
      sleep(2)
      close_button = MyExperiencesPage.get_closeButton_element(self)
      close_button.click()
      sleep(2)
      delete_button = MyExperiencesPage.get_deleteButton_element(self)
      sleep(2)
      self.driver.execute_script("arguments[0].click();", delete_button)
      #delete_button.click()
      
      delete_confirm_message = MyExperiencesPage.get_deleteConfirmMessage_element(self)
      assert delete_confirm_message.text == "Seçilen deneyimi silmek istediğinize emin misiniz ?"
      sleep(2)
      no_button = MyExperiencesPage.get_noButton_element(self)
      sleep(2)
      no_button.click()
      sleep(2)
      self.driver.execute_script("arguments[0].click();", delete_button)
      #delete_button.click()
      sleep(2)
      #yes_button.click()
      yes_button = MyExperiencesPage.get_yesButton_element(self)
      self.driver.execute_script("arguments[0].click();", yes_button)
        
      toast_message1 = MyExperiencesPage.get_toastMessage_element(self)
      assert toast_message1.text == "• Deneyim kaldırıldı."
      sleep(5)
  

  
 

  
