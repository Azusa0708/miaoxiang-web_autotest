from module import miaoxiang
import time

thread = 0

def test_a():
    global thread
    a = miaoxiang(3,'http://aife-test.eastmoney.com:9000/chat','test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div','question.xlsx')
    a.test_round_2()


def test_b():
    a = miaoxiang(3,'http://aife-test.eastmoney.com:9001/chat','test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div','question.xlsx')
    a.test_round_2()

def test_e():
    e = miaoxiang(3,'http://aife-test.eastmoney.com:9000/chat','test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div','question.xlsx')
    e.test_round_3()

def test_c():
    global thread
    while thread != 2:
        time.sleep(2)
    b = miaoxiang(2,'test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[2]/div')
    b.test_round_1()
    thread = thread + 1

def test_d():
    global thread
    while thread != 3:
        time.sleep(2)
    b = miaoxiang(2,'test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[2]/main/div[3]/div')
    b.test_round_1()
    thread = thread + 1