# Test Senaryosunun Adı: Profil Bilgileri altında kişisel bilgilerin güncellenme kontrolleri 
# TEST CASE 5: Geçersiz TC kimlik no uyarısı kontrolü
# *not: TC Kimlik ile eşleşmeyen ad soyad ve doğum tarihi girilirse gelen uyarı

# Profil Bilgileri -> Kişisel Bilgilerim Sayfası 
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import tests.loginTests.test_validLogin as login
from pages.my_personal_info_page import MyPersonalInfoPage
from time import sleep

class TestInvalidIdentification():
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
  
  #@pytest.mark.skip()
  def test_invalidIdentification(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim")

    first_name = MyPersonalInfoPage.get_firstname_element(self)
    first_name.clear()
    first_name.send_keys("TestAd")

    last_name = MyPersonalInfoPage.get_lastname_element(self)
    last_name.clear()
    last_name.send_keys("TestSoyad")

    phone_number = MyPersonalInfoPage.get_phoneNumber_element(self)
    phone_number.clear()
    phone_number.send_keys("5141111111")

    birtday = MyPersonalInfoPage.get_birtday_element(self)
    birtday.send_keys("01.01.2000")

    identification_number = MyPersonalInfoPage.get_identificationNumber_element(self)
    identification_number.clear()
    identification_number.send_keys("89636578955") 

    country = MyPersonalInfoPage.get_country_element(self)
    country.send_keys("Türkiye")
    
    city = MyPersonalInfoPage.get_cityDropdown_element(self)
    city.click()
    sleep(5)
    city.find_element(By.XPATH, "//option[. = 'Adana']").click()

    district = MyPersonalInfoPage.get_districtDropdown_element(self)
    district.click()
    sleep(5)
    district.find_element(By.XPATH, "//option[. = 'Aladağ']").click()

    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(5)
    save_button = MyPersonalInfoPage.get_saveButton_element(self)
    #save_button.click()
    self.driver.execute_script("arguments[0].click();", save_button)
    
    
    self.driver.execute_script("window.scrollTo(0,0)")
    

    toast_message =  WebDriverWait(self.driver, 50).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
    
    assert toast_message.text == "• Kimlik bilgilerinizi hatalı girdiniz."
    sleep(5)
    self.driver.close()