# -*- coding: utf-8 -*-
from contextlib import contextmanager
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules import linear
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim

import transformers
from transformers import SquadExample, pipeline
from transformers import AutoModel, AutoTokenizer


def TestPipe ():
    answerPipe = pipeline("question-answering", model = "monologg/koelectra-small-v2-distilled-korquad-384")#monologg/koelectra-base-v3-finetuned-korquad
    
    #extendPipe = pipeline("text-generation", model = 'skt/kogpt2-base-v2')
    
    while(True) :
        # 질문과 문맥을 정의
        question = input("질문 입력(/로 종료) : ")
        if(question == "/") : break;

        info = """
        인공지능 학습은 에너지와 시간, 정보, 장비 등이 극한까지 요구되는 활동.
        때문에 전체적인 비용 증가, 환경 오염 등등을 막기 위해 사전학습 모델을 서로 공유하는 것이 널리 퍼져있다.
        이를 위한 플랫폼으로 트랜스포머, 허깅페이스 등이 있다.
        우린 이런 사전학습 모델을 구해와 미세 조정(fine-tuning)을 적용해 사용자에게 제공하면 되는 것이다.
        Transformer 모델은 일반적으로 규모가 매우 큽니다.
        수백만에서 수천억 개의 매개변수가포함된 모델을 학습하고 배포하는 일은 매우 복잡한 작업입니다.
        게다가 새로운 모델이 거의 매일 출시되고 각각 고유한 구현 방식이 있기 때문에, 이 모든 모델들을 시험해 보는 것 또한 쉬운 일이 아닙니다.
        Transformers 라이브러리는 이러한 문제를 해결하기 위해 만들어졌습니다.
        이 라이브러리의 목표는 모든 Transformer 모델들을 적재하고, 학습하고, 저장할 수 있는 단일 API를 제공하는 것.
        
        
"2024년부터 '인공지능'이라는 말이 사라지기 시작할 것"
 
(사진=셔터스톡)
인공지능(AI)이라는 말이 내년부터는 줄어들 것이라는 예측이 나왔다. 그러나 이는 AI 기술이 정체하거나 비중이 작아진다는 의미가 아니라, 반대로 너무 광범위하게 채택되고 일상에 녹아 들며 더 이상 이를 강조할 필요가 없다는 일명 'AI 역설(AI paradox)'이라는 설명이다.

포브스는 16일(현지시간) 다수 AI 업계 관계자의 말을 인용, 2024년부터는 AI라는 말이 사라질(Vanishes) 것이라고 예측했다.

이에 따르면 내년에도 AI는 널리 퍼질 것이며, 너무 광범위하게 모든 분야에 침투해 굳이 강조할 필요도 없어질 것으로 전망했다. 이에 따라 올해와 같은 과대광고(hype)가 사라지는 것은 물론 우리의 인식에서도 희미해질 것이라고 봤다.

NBC의 분석에 따르면 현재 AI를 도입한 기업은 4%에 불과하다. 그러나 상당수의 기업은 이미 AI를 사용 중이다. 기업에서 사용하는 애플리케이션에 이미 AI가 적용돼 있기 때문이다.

로리사 호튼 웹엑스 수석 부사장은 "AI는 이미 웹엑스의 모든 부분에 내장돼 있다"라며 "상당수 기업은 언어모델(LLM)을 직접 채택하는 대신 친숙하고 접근 가능한 AI를 기반으로 하는 애플리케이션을 사용하게 될 것"이라고 말했다.

마리넬라 프로피 SAS AI 전략 고문은 "보이지 않는 AI는 미래가 아니라 현재의 현상"이라며 "이미 AI 기능은 이메일 스팸 필터, 스트리밍 서비스 플랫폼 추천, 스마트폰 예측 텍스트 및 자동 수정, 신용 점수, 은행 사기 탐지, 개인화된 광고, 스마트폰, 가정용 기기 등 우리가 알지 못하는 사이에 보이지 않는 곳에서 이미 작동하고 있는 일상 생활의 일부"라고 말했다.

이는 삼성전자가 강조해 온 '캄 테크(calm Technology)'라는 말과도 맥락이 닿아있다. 한종회 삼성전자 부회장은 올해 공식 석상에서 이를 수차례 강조했는데, 사람들이 인지하지 못하는 상태에서 각종 편리한 서비스를 제공한다는 의미다.

한종희 삼성전자 부회장이 10월 열린 SDC22 기조 연설에서 '캄 테크'를 강조하고 있다. (사진=삼성전자)
기업은 물론 일상의 모든 것이 AI로 인해 똑똑해지고 있으며, 그 속도는 더 빨라질 것으로 봤다. 마이크 해니 바텔 메모리얼 인스티튜드 CIO는 "예를 들어 상업용 건물에서는 AI가 탄소 배출, 온수 시스템, 전기 사용 등 모든 부분을 기본적으로 담당하게 될 것이며, 실험실이나 레스토랑, 공장에서는 AI를 통한 예측 유지보수가 표준이 될 것"이라며 "현재 부담스러운 인간 주의가 필요한 시스템은 결국 AI에 의해 자동으로 모니터링되고 관리될 것"이라고 소개했다.

전문가들은 과거 획기적인 기술의 등장 때 그랬듯, AI도 비중이 늘어남과 동시에 기술 자체를 강조하는 현상은 줄어들 것이라고 분석했다. 결국 AI가 적용된 서비스에 초점을 맞추게 된다는 의미다.

장-매튜 셔처 언디 놋 최고 AI  책임자는 " 2012년 등장한 이미지넷의 개체 감지는 딥 러닝의 획기적인 발견이었으나, 이제는 모든 스마트폰에 탑재된 기술"이라며 "일단 실제로 작동하면, 누구도 더 이상 AI라고 부르지 않는다"라고 말했다.

다만 과대광고 주기상 AI가 마케팅이나 광고에 더 빈번하게 등장하는 것은 당연할 것으로 봤다. 데이비드 시델 마이애미 대학교 정보 기술 부문 부사장 겸 CIO도 “AI는 우리 주변과 일상생활에 모두 포함되어 눈에 보이지 않는 동시에 과대 광고 주기의 일부로 마케팅과 광고를 통해 눈에 띄게 될 것”이라고 전했다.

전문가들은 결국 AI가 눈에 보이지 않게 되려면 최종 사용자가 일상에서 AI를 쉽게 사용할 수 있어야 한다고 강조했다. 프로피 SAS 고문은  “사용자가 AI 구성 요소를 직접 이해하거나 상호 작용할 필요 없이 효율적이고 효과적으로 작동해야 한다”라고 지적했다.

셔처 책임자 역시 “최근 생성 AI 기능은 자동화된 시스템을 통해 UX를 혁신하고 있다"라며 "사람들은 좋은 UX에 대해 많이 이야기하지 않는다. 그들은 단지 그것을 채택하고 사용한다”라고 강조했다.

그는 “이런 맥락에서 좋은 AI 시스템은 작동하는 UI 또는 더 효과적인 UX일 뿐”이라고 결론 내렸다.

        """
        

        answerText = answerPipe(question, info, top_k_per_candidate =5, max_answer_length=500,max_context_length = 2048, device = 0, return_prompt  = True)
        print(answerText["answer"])
        # extendText = extendPipe(answerText["answer"])
        # print(extendText)

def TestModel ():
    model = AutoModel.from_pretrained("dontgive99/deberta-v3-base-korean-squad_kor_v1")
    tokenizer = AutoTokenizer.from_pretrained("dontgive99/deberta-v3-base-korean-squad_kor_v1")
    
    info = """
    인공지능 학습은 에너지와 시간, 정보, 장비 등이 극한까지 요구되는 활동.
    때문에 전체적인 비용 증가, 환경 오염 등등을 막기 위해 사전학습 모델을 서로 공유하는 것이 널리 퍼져있다.
    이를 위한 플랫폼으로 트랜스포머, 허깅페이스 등이 있다.
    우린 이런 사전학습 모델을 구해와 미세 조정(fine-tuning)을 적용해 사용자에게 제공하면 되는 것이다.
    Transformer 모델은 일반적으로 규모가 매우 큽니다.
    수백만에서 수천억 개의 매개변수가포함된 모델을 학습하고 배포하는 일은 매우 복잡한 작업입니다.
    게다가 새로운 모델이 거의 매일 출시되고 각각 고유한 구현 방식이 있기 때문에, 이 모든 모델들을 시험해 보는 것 또한 쉬운 일이 아닙니다.
    Transformers 라이브러리는 이러한 문제를 해결하기 위해 만들어졌습니다.
    이 라이브러리의 목표는 모든 Transformer 모델들을 적재하고, 학습하고, 저장할 수 있는 단일 API를 제공하는 것.
    """

    while True:
        # 질문과 문맥을 정의
        question = input("질문 입력 (/로 종료): ")
        if question == "/":
            break

        # 토큰화
        inputs = tokenizer(question, info, return_tensors="pt", max_length=512, truncation=True)
    
        # 모델에 입력하여 출력 받기
        outputs = model.generate(**inputs, output_hidden_states=True, output_attentions=True)

        # 모델의 각 레이어에서의 hidden states과 attentions 가져오기
        hidden_states = outputs.hidden_states
        attentions = outputs.attentions
        
        # 여기서 적절한 hidden states이나 attention을 선택하여 활용할 수 있습니다.
        # 예를 들어, hidden_states[1]은 첫 번째 레이어에서의 hidden states을 나타냅니다.
        # attention_weights = attentions[0]은 첫 번째 어텐션 헤드의 어텐션 가중치를 나타냅니다.

TestModel()

def TestT5 ():
    from transformers import ByT5Tokenizer, ByT5ForConditionalGeneration

    model_name = 'everdoubling/byt5-Korean-small'
    tokenizer = ByT5Tokenizer.from_pretrained(model_name)
    model = ByT5ForConditionalGeneration.from_pretrained(model_name)
    
    inputText = input("입력 : ")
    
    print(inputText)
    inputToken = tokenizer(inputText)
    
    print(inputToken)
    outputTensor = model(inputToken)
    print(outputTensor)
    






