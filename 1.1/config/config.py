from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random

#基础配置
ACCURACY = float(input("输入精确度阈值： "))
ROUND = int(input("输入测试轮次数： "))
file_name = input("输入结果保存文件名： ")

#模块xpath
module_xpath_expression = ['//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[1]/div',
                        '//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div',
                        '//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[2]/div',
                        '//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[3]/div']

#按键字典
key_dir = {
    'expandkey':'//*[@id="root"]/div/article/aside[1]/aside',
    'helperkey':'//*[@id="root"]/div/article/aside[1]/div/header/button[2]',
    'randomquestionkey':'//*[@id="MxChatRoomListWrap"]/div/div[1]/main/div[1]/article/main/div/div/main/article/div['+str(random.randint(1,3))+']',
    'sendkey':'//*[@id="MxChatRoomListWrap"]/div/div[1]/footer/main/section[2]',
}



#导入浏览器配置
chrome_options = Options()
#使用本地浏览器缓存 跳过登录
chrome_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
#打开浏览器
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://aife-test.eastmoney.com:9000/chat")
driver.maximize_window()