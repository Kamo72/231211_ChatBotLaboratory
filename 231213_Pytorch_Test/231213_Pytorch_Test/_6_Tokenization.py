# -*- coding: cp949 -*-


import konlpy
from konlpy.tag import Twitter

def TokenizationTest():
    twt = Twitter()
    while(True) :

        insert = input("Input : ")
        print(twt.morphs(insert))

