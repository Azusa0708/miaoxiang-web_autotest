from config.config import *
from utils.asserts import *
from utils.compare_similarity.compare_similarity import compare_similarity
from utils.reptile.get_text import get_text_answer,get_placeholder_text
from utils.touch.touch_key import touch_key
import time

print("111111111")
i = 0

def run_test():
    #进入妙想主页
    #driver.get("http://aife-test.eastmoney.com:9000/chat")
    driver.maximize_window()
    #先使用sleep 暴力等待
    time.sleep(1)

    while i < ROUND:
        
        touch_key(key_dir['expandkey'])
        touch_key(key_dir['helperkey'])

        for module_xpath in module_xpath_expression:
            touch_key(module_xpath)
            touch_key(key_dir['randomquestionkey'])
            get_placeholder_text("ChatRoom-module__input___BotWC")
            touch_key(key_dir['sendkey'])
            get_text_answer("ShowType40-module__content___CWmch")
            compare_similarity()
            touch_key(key_dir['expandkey'])
            touch_key(key_dir['helperkey'])


        i = i + 1

driver.quit()