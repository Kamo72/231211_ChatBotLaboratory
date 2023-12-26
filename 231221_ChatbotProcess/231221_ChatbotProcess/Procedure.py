from Models import Kr2En, En2Kr, T5TextGen
from ppgTranslater import PPGTranslater

# 프로시저는 모델들을 생성 및 관리하고 모델들이 필요한 기능을 함수로 제공해주는 객체입니다.
class Procedure () :
    
    # 번역 모델, 문장 생성 모델 등을 로드합니다. 번역의 질이 낮아 가능한 경우, 파파고로 대체합니다.
    def __init__(self) :
        self.isPPGmod = True
        self.ppg = PPGTranslater()
        if(self.isPPGmod == False) :
            self.ppg.available = False
        
        self.kr2en = Kr2En()
        self.en2kr = En2Kr()
        self.t5Gen = T5TextGen()
        self.infoEnText = ""
    
    # 문자열을 한국어에서 영어로 번역합니다.
    def TrsKr2En(self, koText) :
        enText = ""
        if(self.ppg.available) :
            enText = self.ppg.Translate(koText, False)
        else :
            enText = self.kr2en.Translate(koText)
        return enText

    # 영어로된 문맥을 전달받아 기억합니다. 그전에 전달한 문맥은 상실합니다.
    def SetInfoEn (self, infoEnTextList) :
        self.infoEnText = ""
        for enCon in infoEnTextList :
            self.infoEnText += enCon
        print(f'[Process] info Set Done!')
    
    # 질문과 전달한 문맥을 토대로 답변을 생성합니다.
    def GetAnswer(self, questionKoText) :
        if(self.ppg.available) :
            inputEnText = self.ppg.Translate(questionKoText, False)
        else :
            inputEnText = self.kr2en.Translate(questionKoText)

        outputEnText = self.t5Gen.MakeAnswer(infoEnText=self.infoEnText, inputEnText=inputEnText)
        
        if(self.ppg.available) :
            outputKrText = self.ppg.Translate(outputEnText, True)
        else :
            outputKrText = self.en2kr.Translate(outputEnText)
            
        return outputKrText
