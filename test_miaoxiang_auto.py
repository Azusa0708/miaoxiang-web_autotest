import pytest
from module import miaoxiang


def test_a():
    a = miaoxiang(0.4,3,'test.xlsx','/html/body/div[1]/div/article/main/div/main/article/section[1]/main/div[1]/div')
    a.test_round()


def test_b():
    b = miaoxiang(0.45,2,'test.xlsx','//*[@id="root"]/div/article/main/div/main/article/section[1]/main/div[2]/div')
    b.test_round()
