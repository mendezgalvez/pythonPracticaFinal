import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("https://demoqa.com/buttons")
        submit_button = driver.find_element_by_xpath("//button[@id='rightClickBtn']")
        submit_button.click()
        time.sleep(2)

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario2(self):
        driver = self.driver
        driver.get("https://demoqa.com/dynamic-properties")
        submit_button = driver.find_element_by_xpath("//button[@id='colorChange']")
        submit_button.click()
        time.sleep(2)

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario3(self):
        driver = self.driver
        driver.get("https://demoqa.com/webtables")
        submit_button_1 = driver.find_element_by_xpath("//button[@id='addNewRecordButton']")
        submit_button_1.click()
        time.sleep(3)
        firstName = driver.find_element_by_xpath("//input[@id='firstName']")
        lastName = driver.find_element_by_xpath("//input[@id='lastName']")
        userEmail = driver.find_element_by_xpath("//input[@id='userEmail']")
        age = driver.find_element_by_xpath("//input[@id='age']")
        salary = driver.find_element_by_xpath("//input[@id='salary']")
        department = driver.find_element_by_xpath("//input[@id='department']")
        firstName.send_keys("Cipriano")
        lastName.send_keys("Mendez")
        userEmail.send_keys("mendezgalvezc@gmail.com")
        age.send_keys("42")
        salary.send_keys("1000")
        department.send_keys("DS")
        submit_button_2 = driver.find_element_by_xpath("//button[@id='submit']")
        time.sleep(3)
        submit_button_2.click()

    def test_reto_final_caso_arbitrario4(self):
        driver = self.driver
        driver.get("https://demoqa.com/modal-dialogs")
        submit_button_small= driver.find_element_by_xpath("//button[@id='showSmallModal']")
        time.sleep(2)
        submit_button_small.click()
        time.sleep(2)
        submit_button_closem = driver.find_element_by_xpath("//button[@id='closeSmallModal']")
        submit_button_closem.click()

        time.sleep(2)
        submit_button_large = driver.find_element_by_xpath("//button[@id='showLargeModal']")
        time.sleep(2)
        submit_button_large.click()
        time.sleep(2)
        submit_button_closel = driver.find_element_by_xpath("//button[@id='closeLargeModal']")
        submit_button_closel.click()

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario5(self):
        driver = self.driver
        driver.get("https://demoqa.com/browser-windows")
        submit_button_tab = driver.find_element_by_xpath("//button[@id='tabButton']")
        submit_button_tab.click()
        time.sleep(2)

        submit_button_window = driver.find_element_by_xpath("//button[@id='windowButton']")
        submit_button_window.click()
        time.sleep(2)

        submit_button_message = driver.find_element_by_xpath("//button[@id='messageWindowButton']")
        submit_button_message.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()