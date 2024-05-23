from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

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

while 1:
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

    #先使用sleep 暴力等待
    time.sleep(1)

    #创意选股按钮xpath
    Creativestockpickingkey_xpath_expression = '//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[1]/div'

    #通过xpath寻找创意选股按钮
    Creativestockpickingkey = driver.find_element(By.XPATH, Creativestockpickingkey_xpath_expression)

    #找到则点击
    if Creativestockpickingkey:
        Creativestockpickingkey.click()
    else:
        #没有按键
        print("没有创意选股按键！！！")

    #先使用sleep 暴力等待
    time.sleep(1)

    #推荐问题n按钮xpath
    n = random.randint(1,4)
    recommendquestion1key_xpath_expression = '//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div['+str(n)+']'

    #通过xpath寻找推荐问题n按钮
    recommendquestion1key = driver.find_element(By.XPATH, recommendquestion1key_xpath_expression)

    #找到则点击
    if recommendquestion1key:
        recommendquestion1key.click()
    else:
        #没有按键
        print("没有推荐问题n按键！！！")

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

    #再次寻找侧边栏展开键
    expandkey = driver.find_element(By.XPATH, expandkey_xpath_expression)

    if expandkey:
        expandkey.click()
    else:
        #侧边栏已展开
        print("侧边栏已展开")

    time.sleep(1)

    #再次点击妙想助手按键
    if helperkey:
        helperkey.click()
    else:
        #没有按键
        print("没有妙想助手按键！！！")

    time.sleep(1)

    #条件选股按钮xpath
    Conditionalstockpickingkey_xpath_expression = '//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div'

    #通过xpath寻找条件选股按钮
    Conditionalstockpickingkey = driver.find_element(By.XPATH, Conditionalstockpickingkey_xpath_expression)

    #找到则点击
    if Conditionalstockpickingkey:
        Conditionalstockpickingkey.click()
    else:
        #没有按键
        print("没有条件选股按键！！！")

    #先使用sleep 暴力等待
    time.sleep(1)

    #推荐问题n按钮xpath
    recommendquestion1key_xpath_expression = '//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div['+str(n)+']'

    #通过xpath寻找推荐问题n按钮
    recommendquestion1key = driver.find_element(By.XPATH, recommendquestion1key_xpath_expression)

    #找到则点击
    if recommendquestion1key:
        recommendquestion1key.click()
    else:
        #没有按键
        print("没有推荐问题n按键！！！")

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



driver.quit()






#//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div[1]
#//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div[2]
#//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div[3]
#//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div[4]