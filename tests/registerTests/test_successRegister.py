# Test Senaryosunun Adı: Kayıt Ol
# TEST CASE 1: Başarılı şekilde telefon numarası textbox görüntülenmesi
# TEST CASE 2: Başarılı kayıt olma kontrolü.
######################## ayrı yazdığımız iki test case(1,2) burada aynı fonksiyon içerisinde kontrol ediliyor.
####################### ayrılması denenebilir. değiştirilebilir!!!!

# Kayıt Ol sayfası 
# https://tobeto.com/kayit-ol

# Generated by Selenium IDE
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep

from pages.register_page import RegisterPage, RegisterPageWindow

class TestSuccessRegister():
  def setup_method(self):
    #self.driver = webdriver.Chrome()
    #self.driver.get("https://tobeto.com/kayit-ol")
    #self.driver.maximize_window()
    RegisterPage.gotoPage(self)
    self.driver.delete_all_cookies()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()

  
  def write_json(new_data, filename='reservedUserNums.json'):
    with open('data/'+filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["reservedNum"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
  
  def create_rand_user():
     
        RandNum= randint(0,1000)
        #with open('data/reservedUserNums.json', 'r') as file:
        #  data = json.load(file)
        #while RandNum in data["reservedNum"]:
        #      RandNum= randint(0,1000)
        data= [{'registerUserName' : 'testName'+str(RandNum),
                'registerSurName' : 'testSurName'+str(RandNum),
                'registerMail' : 'testmail'+str(RandNum)+'@gmail.com',
                'registerPassword': 1234567,
                'registerPhoneNum' : 5321111111
              }]
        #write_json(RandNum)
        return data

  #@pytest.mark.skip() 
  #@pytest.mark.parametrize("registerUserName,registerSurName,registerMail,registerPassword,registerPhoneNum",create_rand_user())
  @pytest.mark.parametrize("user_data",create_rand_user())
  def test_register(self,user_data):
  
    firstName = RegisterPage.get_firstName_element(self)
    firstName.send_keys(user_data["registerUserName"])
    lastName = RegisterPage.get_lastName_element(self)
    lastName.send_keys(user_data["registerSurName"])
    email = RegisterPage.get_email_element(self)
    email.send_keys(user_data["registerMail"])
    password = RegisterPage.get_password_element(self)
    password.send_keys(user_data["registerPassword"])
    password_again = RegisterPage.get_passwordAgain_element(self)
    password_again.send_keys(user_data["registerPassword"])
    
    register_button = RegisterPage.get_registerButton_element(self)
    #register_button1.click()
    sleep(5)
    self.driver.execute_script("arguments[0].click();", register_button)
    
    # Register Page Open Window
    # Açılır pencere
    # Kayıt oluşturmak için gerekli sözleşmeler
    # WebDriverWait(self.driver, 0.5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert-header")))
    contact_permission = RegisterPageWindow.get_contactPermission_element(self)
    contact_permission.click()
    membershipContrat = RegisterPageWindow.get_membershipContrat_element(self)
    membershipContrat.click()
    emailConfirmation = RegisterPageWindow.get_emailConfirmation_element(self)
    emailConfirmation.click()
    phoneConfirmation = RegisterPageWindow.get_phoneConfirmation_element(self)
    phoneConfirmation.click()
    phoneNumberCountry = RegisterPageWindow.get_phoneNumberCountry_element(self)
    phoneNumberCountry.click()
    phoneNumber = RegisterPageWindow.get_phoneNumber_element(self)
    phoneNumber.send_keys(user_data["registerPhoneNum"])
    
    # click captcha manually with sleep
    sleep(15)
    # or click when it is working
    # iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
    # self.driver.switch_to.frame(iframe)
    # captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
    # captcha.click()
    # self.driver.switch_to.default_content()
    #

    continueButton = RegisterPageWindow.get_continueButton_element(self)
    self.driver.execute_script("arguments[0].click();", continueButton)
    #WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".alert-modal")))
    successRegisterAlert = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".success-payment-text")))
    text = successRegisterAlert.text
    assert successRegisterAlert.text == "Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."

  
