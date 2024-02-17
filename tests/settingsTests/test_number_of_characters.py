# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec 
import pytest

from time import sleep


class Test_setting:
    
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() 
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/input[1]")))
        usernameInput.send_keys("pair4testteam@gmail.com")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/input[2]")))
        passwordInput.send_keys("P1234567.")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/button")
        loginButton.click()
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        WebDriverWait(self.driver, 50).until(ec.invisibility_of_element_located(((By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div"))))
        sleep(20)
        self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/ayarlar")
       
       
    def teardown_method(self): 
        self.driver.quit()

   
  
    
    def test_number_of_characters(self):
 
  
      self.driver.find_element(By.NAME, "currentPassword").click()
      self.driver.find_element(By.NAME, "currentPassword").send_keys("P1234567.")
      self.driver.find_element(By.NAME, "password").click()
      self.driver.find_element(By.NAME, "password").send_keys("12345")
      self.driver.find_element(By.NAME, "passwordConfirmation").click()
      self.driver.find_element(By.NAME, "passwordConfirmation").send_keys("12345")
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
      WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifreniz en az 6 karakterden oluşmalıdır."

      



      self.driver.close()
  
