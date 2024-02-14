# Test Senaryosunun Adı: Profil Bilgileri altında deneyimlerim bölümü bilgi ekleme/güncelleme kontrolleri
# TEST CASE 1:  Başarılı deneyim ekleme kontrolü

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

class TestAddSuccessExperience():
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
  def test_addSuccessExperience(self):
    
      # go to page "Deneyimlerim"
      #WebDriverWait(self.driver, 30).until(ec.invisibility_of_element_located(((By.CSS_SELECTOR, ".toast-body"))))

      #user_profile_button = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, gc.USER_PROFILE_BUTTON_XPATH)))
      
      #user_profile_button.click()
      #user_profile_info_button = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
      #user_profile_info_button.click()

      #is_on_profile_page = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[1]/span[2]")))
      #assert is_on_profile_page.text == "Kişisel Bilgilerim"
      #user_experiences_button = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2] ")))
      #user_experiences_button.click()
      
      self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim")

      #for i in range(0,150):
      self.driver.execute_script("window.scrollTo(0,0)")
      sleep(2)
      corporationName = MyExperiencesPage.get_corporationName_element(self)  
      corporationName.send_keys(i+1,"Tobeto") 
            
      position = MyExperiencesPage.get_position_element(self)  
      position.send_keys("Yazılım Kalite ve Test Uzmanı")
            
      sector = MyExperiencesPage.get_sector_element(self) 
      sector.send_keys("Yazılım")
            
      select_country_dropdown = MyExperiencesPage.get_countryDropdown_element(self) 
      select_option = select_country_dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']")
      select_option.click()
      
      start_calender = MyExperiencesPage.get_startCalendar_element(self)
      start_calender.click()

      start_month = MyExperiencesPage.get_startMonth_element(self) ####################
      start_month.click()
      start_month.find_element(By.XPATH, "//option[. = 'Ocak']").click()

      start_year = MyExperiencesPage.get_startYear_element(self)
      start_year.click()
      start_year.find_element(By.XPATH, "//option[. = '2020']").click()
            
      start_day = MyExperiencesPage.get_startDay_element(self) 
      start_day.click()
            
      finish_calender = MyExperiencesPage.get_finishCalendar_element(self) 
      finish_calender.click()
              
      finish_date = MyExperiencesPage.get_finishDate_element(self) 
      finish_date.click()

      sleep(2)
      save_button = MyExperiencesPage.get_saveButton_element(self) 
      save_button.click()

      toast_message = MyExperiencesPage.get_toastMessage_element(self) 
      assert toast_message.text == "• Deneyim eklendi."
      sleep(2)
      self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
      sleep(2)
  
