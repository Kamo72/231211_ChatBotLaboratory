# -*- coding: cp949 -*-
from asyncio.windows_events import NULL
from re import split
import torch
from transformers import GenerationConfig, pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from Models import T5TextGen, En2Kr, Kr2En
from Procedure import Procedure
from ServerAndClient import Server,Client
from LectureManager import LectureManager
import socket, time

# 기본 객체 생성
proc = Procedure()
lm = LectureManager(proc.TrsKr2En)

# 메인 프로세스
def ClientProcess() :
    
    # 클라이언트 선언
    client : Client = NULL
    
    # WSA의 요청에 따른 반응 정의
    def ClientDel (msg) :
        print(msg),
        sp = msg.split("#")
        flag = sp[0]
        match flag:
            case "CreateLecture" :
                res = lm.MakeLecture(sp[1])
                client.Send("CreateLecture#" + str(res))
                
            case "DeleteLecture" : 
                res = lm.DeleteLecture(sp[1])
                client.Send("DeleteLecture#" + str(res))
                
            case "ListLecture" : 
                res = lm.ListLecture()
                pac = "ListLecture#"
                for lec in res : pac += lec + "@"
                client.Send(pac)
                
            case "CreatePart" : 
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                res = lm.MakePart(ssp[1])
                client.Send("CreatePart#" + str(res))
                
            case "DeletePart" :
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                res = lm.DeletePart(ssp[1])
                client.Send("DeletePart#" + str(res))
                
            case "Listpart" : 
                lm.LoadLecture(sp[1])
                res = lm.ListPart()
                pac = "Listpart#"
                for part in res : pac += part + "@"
                client.Send(pac)
                
            case "AppendContext" : 
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                lm.LoadPart(ssp[1])
                res = lm.WriteContext(ssp[2])
                client.Send("AppendContext#" + str(res))
                
            case "ResetContext" :
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                lm.LoadPart(ssp[1])
                res = lm.ResetContext()
                client.Send("ResetContext#" + str(res))
                
            case "ListContext" :
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                lm.LoadPart(ssp[1])
                res = lm.ReadContext()
                pac = "ListContext#"
                for part in res : pac += part + "@"
                client.Send(pac)
            
            case "LoadContext" :
                ssp = sp[1].split("@")
                lm.LoadLecture(ssp[0])
                lm.LoadPart(ssp[1])
                try :
                    res = lm.ReadEnContext()
                    proc.SetInfoEn(res)
                except :
                    res = lm.ReadContext()
                    proc.SetInfo(res)
                    
                client.Send("LoadContext#" + str(True))
                
            case "GetAnswer" :
                ssp = sp[1].split("@")
                idx = ssp[0]
                res = proc.GetAnswer(ssp[1])
                client.Send("GetAnswer#" +ssp[0]+"#"+ res)
                
            case "StopProcess" :
                exit()
                
            case "StartProcess" : pass

    # 클라이언트 생성
    client = Client('127.0.0.1', 4090, ClientDel)
    
    # 클라이언트 연결
    client.Connect()
    
    # 클라이언트가 입력 받을 준비가 되었다고 전송
    client.Send("StartProcess#")
    
ClientProcess()

