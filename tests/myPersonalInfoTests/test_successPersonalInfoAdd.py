# Test Senaryosunun Adı: Profil Bilgileri altında kişisel bilgilerin güncellenme kontrolleri 
# TEST CASE 2: Başarılı kişisel bilgi ekleme/güncelleme kontrolü

# Profil Bilgileri -> Kişisel Bilgilerim Sayfası 
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

# Generated by Selenium IDE
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import tests.loginTests.test_validLogin as login
import constants.credentials_constants as cc
from pages.my_personal_info_page import MyPersonalInfoPage
from time import sleep

class TestSuccessPersonalInfoAdd():
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
  
  @pytest.mark.skip()
  def test_successPersonalInfoAdd(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim")

    first_name = MyPersonalInfoPage.get_firstname_element(self)
    first_name.clear()
    first_name.send_keys(cc.IDENTITY_NAME)

    last_name = MyPersonalInfoPage.get_lastname_element(self)
    last_name.clear()
    last_name.send_keys(cc.IDENTITY_SURNAME)

    phone_number = MyPersonalInfoPage.get_phoneNumber_element(self)
    phone_number.clear()
    phone_number.send_keys("5141111111")

    birthday = MyPersonalInfoPage.get_birthday_element(self)
    birthday.send_keys(cc.IDENTITY_BIRTHDATE)

    identification_number = MyPersonalInfoPage.get_identificationNumber_element(self)
    identification_number.clear()
    identification_number.send_keys(cc.IDENTIFICATION_NUMBER) 

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

    page_toast_message =  MyPersonalInfoPage.get_pageToastMessage_element(self)
    
    assert page_toast_message.text == "• Bilgileriniz başarıyla güncellendi."
    self.driver.close()