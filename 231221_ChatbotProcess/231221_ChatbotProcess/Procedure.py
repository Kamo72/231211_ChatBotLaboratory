from Models import Kr2En, En2Kr, T5TextGen
from ppgTranslater import PPGTranslater

# ���ν����� �𵨵��� ���� �� �����ϰ� �𵨵��� �ʿ��� ����� �Լ��� �������ִ� ��ü�Դϴ�.
class Procedure () :
    
    # ���� ��, ���� ���� �� ���� �ε��մϴ�. ������ ���� ���� ������ ���, ���İ�� ��ü�մϴ�.
    def __init__(self) :
        self.isPPGmod = True
        self.ppg = PPGTranslater()
        if(self.isPPGmod == False) :
            self.ppg.available = False
        
        self.kr2en = Kr2En()
        self.en2kr = En2Kr()
        self.t5Gen = T5TextGen()
        self.infoEnText = ""
    
    # ���ڿ��� �ѱ���� ����� �����մϴ�.
    def TrsKr2En(self, koText) :
        enText = ""
        if(self.ppg.available) :
            enText = self.ppg.Translate(koText, False)
        else :
            enText = self.kr2en.Translate(koText)
        return enText

    # ����ε� ������ ���޹޾� ����մϴ�. ������ ������ ������ ����մϴ�.
    def SetInfoEn (self, infoEnTextList) :
        self.infoEnText = ""
        for enCon in infoEnTextList :
            self.infoEnText += enCon
        print(f'[Process] info Set Done!')
    
    # ������ ������ ������ ���� �亯�� �����մϴ�.
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
