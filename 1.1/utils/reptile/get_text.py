from selenium.webdriver.common.by import By
from config.config import driver
from html import unescape

placeholder_text = ""
text_answer = ""

#爬取输入框问题
def get_placeholder_text(class_name):
    placeholder_text = driver.find_element(By.CLASS_NAME,class_name)
    placeholder_text = placeholder_text.text
    placeholder_text = unescape(placeholder_text)

#爬取前端文字回答
def get_text_answer(class_name):
    text_answer = driver.find_element(By.CLASS_NAME,class_name)
    text_answer = text_answer.text
    text_answer = unescape(text_answer)