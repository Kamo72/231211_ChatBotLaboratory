# -*- coding: cp949 -*-

import torch
from transformers import GenerationConfig, pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer



def TestTextGen() :
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base", device_map = "auto")

    while True :
        inputText = input("input : ")
        
        input_ids = tokenizer(inputText, return_tensors="pt").input_ids.to("cuda")
        genConfig = GenerationConfig(
            # num_beams = 2,
            # length_penalty=0.1,
            # do_sample=True,
            # temperature  = 1,
            # repetition_penalty = 10.0,
            max_length = 200
            )
        outputs = model.generate(input_ids, generation_config=genConfig)
        outputText = tokenizer.decode(outputs[0])
        print(outputText)

def TestTextGenWithContext() :
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base", device_map="auto")

    while True :
        inputText = input("input : ")
        
        information = """
            Artificial intelligence learning is an activity that requires extreme energy, time, information, and equipment.
            Therefore, it is widespread to share pre-learning models with each other to prevent overall cost increases and environmental pollution.
            Platforms for this include Transformers and Huggling Face.
            We can get this pre-learning model and apply fine-tuning to provide it to users.
            Transformer models are typically very large.
            Learning and deploying models containing millions to hundreds of billions of parameters is a very complex task.
            And with new models rolling out almost every day and each having its own way of implementation, it's not an easy task to try out all these models.
            The Transformers library was created to address these issues.
            The goal of this library is to provide a single API to load, learn, and store all Transformer models.
            Artificial intelligence learning is an activity that requires extreme energy, time, information, and equipment.
            Therefore, it is widespread to share pre-learning models with each other to prevent overall cost increases and environmental pollution.
            Platforms for this include Transformers and Huggling Face.
            We can get this pre-learning model and apply fine-tuning to provide it to users.
            Transformer models are typically very large.
            Learning and deploying models containing millions to hundreds of billions of parameters is a very complex task.
            And with new models rolling out almost every day and each having its own way of implementation, it's not an easy task to try out all these models.
            The Transformers library was created to address these issues.
            The goal of this library is to provide a single API to load, learn, and store all Transformer models.
            """
        
        input_ids = tokenizer(information + "\n text" +inputText, return_tensors="pt").input_ids.to("cuda")
        genConfig = GenerationConfig(
            # num_beams = 2,
            # length_penalty=0.1,
            # do_sample=True,
            # temperature  = 1,
            # repetition_penalty = 10.0,
            max_length = 200
            )
        outputs = model.generate(input_ids, generation_config=genConfig)
        outputText = tokenizer.decode(outputs[0])
        print(outputText)
        
def TestWhole() :
    t5Gen = T5TextGen()
    kr2en = Kr2En()
    #en2kr = pipeline("translation", model ="Helsinki-NLP/opus-mt-tc-big-en-ko")
    en2kr = En2Kr()
    
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
        거대한 모델을 배우고 보급하기 위해서는 박상한의 엉덩이가 필요합니다.
        
        거대한 육상 포유류인 히오스는 코끼리보다 크고 강력합니다.
        히오스는 하루에 20시간을 자고는 합니다.
        """]
    infoEnText = ""
    
    count = 0
    for kr_text in infoKrTexts:
        print(f'[Process] Lecture info translating...{count}/{len(infoKrTexts)}')
        infoEnText += kr2en.Translate(kr_text)
        count += 1
    print(f'[Process] Lecture info translated!')

    while True :
        inputKrText = input("input : ")
        
        inputEnText = kr2en.Translate(inputKrText)
        
        outputEnText = t5Gen.MakeAnswer(infoEnText=infoEnText, inputEnText=inputEnText)
        
        outputKrText = en2kr.Translate(outputEnText)
        
        print("output : " + outputKrText)

     
        
class T5TextGen():
    def __init__ (self):
        print('[Process] Loading T5...')
        self.tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
        self.model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base").to("cuda")
        print('[Process] Loaded T5!')
    def MakeAnswer (self, infoEnText, inputEnText) :
        print('[Process] Answer generating...')
        input_ids = self.tokenizer(infoEnText + "Question : Please write about 50 characters,  " +inputEnText + "?", return_tensors="pt").input_ids.to("cuda")
        genConfig = GenerationConfig(
            # num_beams = 2,
            # length_penalty=0.1,
            do_sample=True,
            # temperature  = 1,
            repetition_penalty = 10.0,
            max_length = 500
            )
        
        outputEnData = self.model.generate(input_ids, generation_config=genConfig)
        outputEnText = self.tokenizer.decode(outputEnData[0], skip_special_tokens=True)
        print('[Process] Answer generated! - ' + outputEnText)
        return outputEnText

class En2Kr():
    
    def __init__(self) :
        print('[Process] Loading en2krTrs...')
        
        modelname = "hyerin/m2m100_418M-finetuned-en-to-ko"
        self.tokenizer = AutoTokenizer.from_pretrained(modelname)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(modelname).to("cuda")

        print('[Process] Loaded en2krTrs!')
        
    def Translate(self, text) : 
        print('[Process] en2krTrs translating...')
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to("cuda")
        
        genConfig = GenerationConfig(
            # num_beams = 2,
            # length_penalty=0.1,
            # do_sample=True,
            # temperature  = 0.1,
            # repetition_penalty = 10.0,
            max_length = 500
            )                

        output_ids = self.model.generate(input_ids, genConfig)
        translated_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=False)
        print('[Process] en2krTrs translated! - ' + translated_text)
        return translated_text
    
class Kr2En():

    def __init__(self) :
        print('[Process] Loading kr2enTrs...')
        
        modelname = "hcho22/opus-mt-ko-en-finetuned-kr-to-en"
        self.tokenizer = AutoTokenizer.from_pretrained(modelname)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(modelname, from_tf=True).to("cuda")
        
        print('[Process] Loaded kr2enTrs!')
        
    def Translate(self, text) : 
        print('[Process] kr2enTrs translating...')
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to("cuda")
        genConfig = GenerationConfig(
            # num_beams = 2,
            # length_penalty=0.1,
            do_sample=True,
            temperature  = 0.1,
            # repetition_penalty = 10.0,
            max_length = 500
            )        

        output_ids = self.model.generate(input_ids,genConfig)
        translated_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        print('[Process] kr2enTrs translated! - ' + translated_text)
        return translated_text