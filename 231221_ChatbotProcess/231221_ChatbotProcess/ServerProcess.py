# -*- coding: cp949 -*-
from ServerAndClient import Server,Client
from asyncio.windows_events import NULL
import time, subprocess

def ServerProcess() :
    
    # 서버 선언
    server : Server = NULL

    # 흐름 제어용 변수 초기화 (추후,)
    answerBuffer = "" #
    clientIsAvailable = False  

    # 클라이언트로부터의 패킷에 따른 반응 정의
    def ServerDel (client_socket, msg) :
        print(msg),
        sp = msg.split("#")
        flag = sp[0]
        match flag:
            case "CreateLecture" : pass
            case "DeleteLecture" : pass
            case "ListLecture" : pass
            case "CreatePart" : pass
            case "DeletePart" : pass
            case "Listpart" : pass
            case "AppendContext" : pass
            case "ResetContext" : pass
            case "ListContext" : pass
            case "LoadContext" : pass
            case "GetAnswer" :
                ssp = sp[1].split('@')
                #여기서 답변을 처리하는 코드를 작성
                print(f"{ssp[0]}번 답변 : {ssp[1]}")
            case "StopProcess" : pass
            case "StartProcess" :
                global clientIsAvailable
                clientIsAvailable= True
            
    # 서버 생성
    server = Server('127.0.0.1', 4090, ServerDel)
    server.Deploy()



    print("[Process] AI 프로세스를 로드 중입니다. 잠시만 기다려 주십시오...")
    # AI 프로세스를 새로운 창에서 실행.
    program_path = r"S:\[GitHub]\비트고급_프로젝트\231211_ChatBotLaboratory\231221_ChatbotProcess\231221_ChatbotProcess\MainProcess.py"
    subprocess.Popen(["python", program_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # AI 프로세스가 기동할 때까지 대기
    while clientIsAvailable == False : pass
    print("[Process] AI 프로세스가 로드되었습니다!")



    # 테스트용 강좌를 생성
    print("[Process] 사전 지정 강좌를 불러옵니다...")
    server.Send("CreateLecture#박상한의 케로로학")
    server.Send("CreatePart#박상한의 케로로학@케로케로링")
    server.Send("ResetContext#박상한의 케로로학@케로케로링")
    server.Send("AppendContext#박상한의 케로로학@케로케로링@박상한은 전교 1등의 학생이다. 박상한 학생은 매우 똑똑하며, 인공지능 분야에서 큰 능력을 발휘한다. 박상한 학생은 좋은 성적을 가지고 있는 학생이다.")
    server.Send("AppendContext#박상한의 케로로학@케로케로링@박상한 학생은 개구리 중사 케로로라는 애니메이션을 종아한다. 박상한 학생은 케로로를 좋아한다. 케로로는 다섯 마리의 외계 개구리가 지구를 침략하려하나, 우주와 한별이와 함께 살게되는 이야기다.")
    server.Send("LoadContext#박상한의 케로로학@케로케로링")

    #질문과 응답
    answerCounter = 0;
    while True :
        inputText = input(f"{answerCounter}번 질문 : ")
        server.Send(f"GetAnswer#{answerCounter}@{inputText}")
        answerCounter+=1
        
ServerProcess()



# 모든 종류의 패킷을 전달해 작동이 정상적으로 이뤄지는지 검사할 수 있는 함수
def TestCode (server):
    time.sleep(1)
    server.Send("CreateLecture#박상한의 케로로학")
    time.sleep(1)
    server.Send("DeleteLecture#박상한의 케로로학")
    time.sleep(1)
    server.Send("CreateLecture#박상한의 케로로학")
    time.sleep(1)
    server.Send("ListLecture#")
    time.sleep(1)
    server.Send("CreatePart#박상한의 케로로학@케로케로링")
    time.sleep(1)
    server.Send("DeletePart#박상한의 케로로학@케로케로링")
    time.sleep(1)
    server.Send("CreatePart#박상한의 케로로학@케로케로링")
    time.sleep(1)
    server.Send("CreatePart#박상한의 케로로학@아마겟돈 천분의 일")
    time.sleep(1)
    server.Send("Listpart#박상한의 케로로학")
    time.sleep(1)
    server.Send("ResetContext#박상한의 케로로학@케로케로링")
    time.sleep(1)
    server.Send("AppendContext#박상한의 케로로학@케로케로링@박상한은 전교 1등의 학생이다. 박상한 학생은 매우 똑똑하며, 인공지능 분야에서 큰 능력을 발휘한다. 박상한 학생은 좋은 성적을 가지고 있는 학생이다.")
    time.sleep(1)
    server.Send("AppendContext#박상한의 케로로학@케로케로링@박상한 학생은 개구리 중사 케로로라는 애니메이션을 종아한다. 박상한 학생은 케로로를 좋아한다. 케로로는 다섯 마리의 외계 개구리가 지구를 침략하려하나, 우주와 한별이와 함께 살게되는 이야기다.")
    time.sleep(1)
    server.Send("ResetContext#박상한의 케로로학@아마겟돈 천분의 일")
    time.sleep(1)
    server.Send("AppendContext#박상한의 케로로학@아마겟돈 천분의 일@박상한은 우송대에서 탈출한 학생이다. 박상한 학생은 우송대에 싫증을 느끼고 있었다. 박상한 학생은 우송대를 싫어한다. 박상한 학생은 우송대에서 도망쳤다.")
    time.sleep(1)
    server.Send("LoadContext#박상한의 케로로학@아마겟돈 천분의 일")
    time.sleep(3)
    server.Send("GetAnswer#1@박상한 학생에 대해 설명해줄래?")
    time.sleep(1)
    server.Send("LoadContext#박상한의 케로로학@케로케로링")
    time.sleep(3)
    server.Send("GetAnswer#2@박상한 학생에 대해 설명해줄래?")

    a = input("")
    exit()
