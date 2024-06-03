from selenium import webdriver
from config.config import driver
from selenium.webdriver.common.by import By
from utils.asserts.assert_exist_key import assert_exist_key

def touch_key(key_xpath):
    key = driver.find_element(By.XPATH, key_xpath)
    assert_exist_key(key)