# -*- coding: cp949 -*-
import torch
from transformers import GenerationConfig, pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from Models import T5TextGen, En2Kr, Kr2En
from Procedure import Procedure
from LectureManager import LectureManager

def MainProcess() :
    lm = LectureManager()
    
    # lm.LoadLecture("이동우_옹알이개론")
    # lm.LoadPart("비주얼 스튜디오 버전이 안맞네요")
    # print(lm.ReadContext())
    # lm.WriteContext("sadsadasdsadsadsa")
    # print(lm.ReadContext())
    
    # a = input("insert any")
    # exit()



    # lm.MakeLecture("이동우_옹알이개론")
    # lm.ListLecture()
    # lm.LoadLecture("이동우_옹알이개론")
    
    # lm.ListLecture()

    # lm.MakePart("옹알옹알옹알옹알")
    # lm.MakePart("비주얼 스튜디오 버전이 안맞네요")
    # lm.MakePart("헤더.h")
    # lm.MakePart("만사형통이여(물음표)")
    # lm.DeletePart("만사형통이여(물음표)")
    # lm.MakePart("만사형통이여(물음표)")
    # lm.LoadPart("비주얼 스튜디오 버전이 안맞네요")
    # lm.LoadPart("비주얼 스튜디오 버전이 안맞네요")
    
    # lm.ListPart()

    # print(lm.ReadContext())
    # infoKrTexts = """ 
    # 인공지능 학습은 에너지와 시간, 정보, 장비 등이 극한까지 요구되는 활동.
    # 때문에 전체적인 비용 증가, 환경 오염 등등을 막기 위해 사전학습 모델을 서로 공유하는 것이 널리 퍼져있다.
    # 이를 위한 플랫폼으로 트랜스포머, 허깅페이스 등이 있다.       
    # 우린 이런 사전학습 모델을 구해와 미세 조정(fine-tuning)을 적용해 사용자에게 제공하면 되는 것이다.      
    # Transformer 모델은 일반적으로 규모가 매우 큽니다.
    # 수백만에서 수천억 개의 매개변수가 포함된 모델을 학습하고 배포하는 일은 매우 복잡한 작업입니다.
    # 게다가 새로운 모델이 거의 매일 출시되고 각각 고유한 구현 방식이 있기 때문에, 이 모든 모델들을 시험해 보는 것 또한 쉬운 일이 아닙니다.
    # Transformers 라이브러리는 이러한 문제를 해결하기 위해 만들어졌습니다.
    # 이 라이브러리의 목표는 모든 Transformer 모델들을 적재하고, 학습하고, 저장할 수 있는 단일 API를 제공하는 것.
    # 박상한 학생은 거대한 AI 모델을 학습시키고 보급하기 위해서 필요합니다.
    # 박상한 학생은 AI 모델을 개발하고 학습시키는게 매우 훌륭합니다.
    # 박상한 학생은 인공지능 개발에 재능을 가지고 있습니다.
    # 히오스는 전세계에서 가장 인기있는 게임이다.
    # 히오스는 5대5로 진행되는 AOS 장르의 게임입니다.
    # 히오스의 장점은 공산주의 시스템과 끔찍한 타격감, 느린 매칭시스템 등이 있습니다.
    # 박상한 학생은 히오스를 정말 좋아합니다.
    # 히오스는 매년 HGC라는 세계적으로 매우 인기있는 e-sports 대회를 운영합니다."""
    

    # lm.WriteContext(infoKrTexts)
    # print(lm.ReadContext())
    
    # a = input("insert any")
    # exit()

    

    proc = Procedure()

    infoKrTexts = ["""
        인공지능 학습은 에너지와 시간, 정보, 장비 등이 극한까지 요구되는 활동.
        때문에 전체적인 비용 증가, 환경 오염 등등을 막기 위해 사전학습 모델을 서로 공유하는 것이 널리 퍼져있다.
        이를 위한 플랫폼으로 트랜스포머, 허깅페이스 등이 있다.       
        우린 이런 사전학습 모델을 구해와 미세 조정(fine-tuning)을 적용해 사용자에게 제공하면 되는 것이다.
        ""","""           
        Transformer 모델은 일반적으로 규모가 매우 큽니다.
        수백만에서 수천억 개의 매개변수가 포함된 모델을 학습하고 배포하는 일은 매우 복잡한 작업입니다.
        게다가 새로운 모델이 거의 매일 출시되고 각각 고유한 구현 방식이 있기 때문에, 이 모든 모델들을 시험해 보는 것 또한 쉬운 일이 아닙니다.
        Transformers 라이브러리는 이러한 문제를 해결하기 위해 만들어졌습니다.
        이 라이브러리의 목표는 모든 Transformer 모델들을 적재하고, 학습하고, 저장할 수 있는 단일 API를 제공하는 것.
        ""","""
        박상한 학생은 거대한 AI 모델을 학습시키고 보급하기 위해서 필요합니다.
        박상한 학생은 AI 모델을 개발하고 학습시키는게 매우 훌륭합니다.
        박상한 학생은 인공지능 개발에 재능을 가지고 있습니다.
        ""","""
        히오스는 전세계에서 가장 인기있는 게임이다.
        히오스는 5대5로 진행되는 AOS 장르의 게임입니다.
        히오스의 장점은 공산주의 시스템과 끔찍한 타격감, 느린 매칭시스템 등이 있습니다.
        박상한 학생은 히오스를 정말 좋아합니다.
        히오스는 매년 HGC라는 세계적으로 매우 인기있는 e-sports 대회를 운영합니다.
        """]
    proc.SetInfo(infoKrTexts)

    while True :
        inputKrText = input("input : ")
        
        outputKrText = proc.GetAnswer(inputKrText)
        
        print("output : " + outputKrText)

MainProcess()

