import time

#按键存在断言
def assert_exist_key(key):
    assert key,"按键不存在！！！"
    key.click()
    time.sleep(1)