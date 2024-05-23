from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

#点击侧边栏
def touch_expandkey():
    #xpath 判断侧边栏是否拉开 未拉开则需要拉开
    #此处xpath对应展开键
    expandkey_xpath_expression = '//*[@id="root"]/div/article/aside[1]/aside'

    #通过xpath寻找拉开键
    expandkey = driver.find_element(By.XPATH, expandkey_xpath_expression)

    #找到则点击
    if expandkey:
        expandkey.click()
    else:
        #侧边栏已展开
        print("侧边栏已展开")
    time.sleep(1)

#点击妙想助手
def touch_helper():
    #妙想助手按钮xpath
    helperkey_xpath_expression = '//*[@id="root"]/div/article/aside[1]/div/header/button[2]'

    #通过xpath寻找妙想助手按钮
    helperkey = driver.find_element(By.XPATH, helperkey_xpath_expression)

    #找到则点击
    if helperkey:
        helperkey.click()
    else:
        #没有按键
        print("没有妙想助手按键！！！")
    time.sleep(1)

#点击对应模块按钮
def touch_module(module_key):
    #找到则点击
    if module_key:
        module_key.click()
    else:
        #没有按键
        print("没有对应模块按键！！！")
    time.sleep(1)

#点击随机推荐问题
def touch_randomquestion():
    #推荐问题n按钮xpath
    n = random.randint(1,3)
    recommendquestionkey_xpath_expression = '//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div['+str(n)+']'

    #通过xpath寻找推荐问题n按钮
    recommendquestionkey = driver.find_element(By.XPATH, recommendquestionkey_xpath_expression)

    #找到则点击
    if recommendquestionkey:
        recommendquestionkey.click()
    else:
        #没有按键
        print("没有推荐问题n按键！！！")
    time.sleep(1)

#点击发送按键
def touch_send():
    #发送按钮xpath
    sendkey_xpath_expression = '//*[@id="MxChatRoomListWrap"]/div/div[1]/footer/main/section[2]'

    #通过xpath寻找发送按钮
    sendkey = driver.find_element(By.XPATH, sendkey_xpath_expression)

    #找到则点击
    if sendkey:
        sendkey.click()
    else:
        #没有按键
        print("没有发送按键！！！")
        
    #等待回答加载完毕
    time.sleep(15)


######################################################初始化测试板块配置######################################################
module_xpath_expression = ['//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[1]/div',
                           '//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div',
                           '//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[2]/div',
                           '//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[3]/div']

chrome_options = Options()

#option = webdriver.ChromeOptions()

#使用本地浏览器缓存 跳过登录
chrome_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')

#导入配置
driver = webdriver.Chrome(options=chrome_options)

#进入妙想主页
driver.get("http://aife-test.eastmoney.com:9000/chat")
driver.maximize_window()

#先使用sleep 暴力等待
time.sleep(1)




#无限循环
while 1:

    touch_expandkey()
    touch_helper()

    #循环所选模块
    for module_xpath in module_xpath_expression:
        #通过xpath寻找模块按钮
        module_key = driver.find_element(By.XPATH, module_xpath)
        touch_module(module_key)

        touch_randomquestion()
        
        touch_send()

        touch_expandkey()

        touch_helper()

driver.quit()
