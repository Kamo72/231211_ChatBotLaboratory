# -*- coding: cp949 -*-
from ServerAndClient import Server,Client
from asyncio.windows_events import NULL
import time, subprocess

def ServerProcess() :
    
    # ���� ����
    server : Server = NULL

    # �帧 ����� ���� �ʱ�ȭ (����,)
    answerBuffer = "" #
    clientIsAvailable = False  

    # Ŭ���̾�Ʈ�κ����� ��Ŷ�� ���� ���� ����
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
                #���⼭ �亯�� ó���ϴ� �ڵ带 �ۼ�
                print(f"{ssp[0]}�� �亯 : {ssp[1]}")
            case "StopProcess" : pass
            case "StartProcess" :
                global clientIsAvailable
                clientIsAvailable= True
            
    # ���� ����
    server = Server('127.0.0.1', 4090, ServerDel)
    server.Deploy()



    print("[Process] AI ���μ����� �ε� ���Դϴ�. ��ø� ��ٷ� �ֽʽÿ�...")
    # AI ���μ����� ���ο� â���� ����.
    program_path = r"S:\[GitHub]\��Ʈ���_������Ʈ\231211_ChatBotLaboratory\231221_ChatbotProcess\231221_ChatbotProcess\MainProcess.py"
    subprocess.Popen(["python", program_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # AI ���μ����� �⵿�� ������ ���
    while clientIsAvailable == False : pass
    print("[Process] AI ���μ����� �ε�Ǿ����ϴ�!")



    # �׽�Ʈ�� ���¸� ����
    print("[Process] ���� ���� ���¸� �ҷ��ɴϴ�...")
    server.Send("CreateLecture#�ڻ����� �ɷη���")
    server.Send("CreatePart#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    server.Send("ResetContext#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    server.Send("AppendContext#�ڻ����� �ɷη���@�ɷ��ɷθ�@�ڻ����� ���� 1���� �л��̴�. �ڻ��� �л��� �ſ� �ȶ��ϸ�, �ΰ����� �о߿��� ū �ɷ��� �����Ѵ�. �ڻ��� �л��� ���� ������ ������ �ִ� �л��̴�.")
    server.Send("AppendContext#�ڻ����� �ɷη���@�ɷ��ɷθ�@�ڻ��� �л��� ������ �߻� �ɷηζ�� �ִϸ��̼��� �����Ѵ�. �ڻ��� �л��� �ɷηθ� �����Ѵ�. �ɷηδ� �ټ� ������ �ܰ� �������� ������ ħ���Ϸ��ϳ�, ���ֿ� �Ѻ��̿� �Բ� ��ԵǴ� �̾߱��.")
    server.Send("LoadContext#�ڻ����� �ɷη���@�ɷ��ɷθ�")

    #������ ����
    answerCounter = 0;
    while True :
        inputText = input(f"{answerCounter}�� ���� : ")
        server.Send(f"GetAnswer#{answerCounter}@{inputText}")
        answerCounter+=1
        
ServerProcess()



# ��� ������ ��Ŷ�� ������ �۵��� ���������� �̷������� �˻��� �� �ִ� �Լ�
def TestCode (server):
    time.sleep(1)
    server.Send("CreateLecture#�ڻ����� �ɷη���")
    time.sleep(1)
    server.Send("DeleteLecture#�ڻ����� �ɷη���")
    time.sleep(1)
    server.Send("CreateLecture#�ڻ����� �ɷη���")
    time.sleep(1)
    server.Send("ListLecture#")
    time.sleep(1)
    server.Send("CreatePart#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    time.sleep(1)
    server.Send("DeletePart#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    time.sleep(1)
    server.Send("CreatePart#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    time.sleep(1)
    server.Send("CreatePart#�ڻ����� �ɷη���@�Ƹ��ٵ� õ���� ��")
    time.sleep(1)
    server.Send("Listpart#�ڻ����� �ɷη���")
    time.sleep(1)
    server.Send("ResetContext#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    time.sleep(1)
    server.Send("AppendContext#�ڻ����� �ɷη���@�ɷ��ɷθ�@�ڻ����� ���� 1���� �л��̴�. �ڻ��� �л��� �ſ� �ȶ��ϸ�, �ΰ����� �о߿��� ū �ɷ��� �����Ѵ�. �ڻ��� �л��� ���� ������ ������ �ִ� �л��̴�.")
    time.sleep(1)
    server.Send("AppendContext#�ڻ����� �ɷη���@�ɷ��ɷθ�@�ڻ��� �л��� ������ �߻� �ɷηζ�� �ִϸ��̼��� �����Ѵ�. �ڻ��� �л��� �ɷηθ� �����Ѵ�. �ɷηδ� �ټ� ������ �ܰ� �������� ������ ħ���Ϸ��ϳ�, ���ֿ� �Ѻ��̿� �Բ� ��ԵǴ� �̾߱��.")
    time.sleep(1)
    server.Send("ResetContext#�ڻ����� �ɷη���@�Ƹ��ٵ� õ���� ��")
    time.sleep(1)
    server.Send("AppendContext#�ڻ����� �ɷη���@�Ƹ��ٵ� õ���� ��@�ڻ����� ��۴뿡�� Ż���� �л��̴�. �ڻ��� �л��� ��۴뿡 ������ ������ �־���. �ڻ��� �л��� ��۴븦 �Ⱦ��Ѵ�. �ڻ��� �л��� ��۴뿡�� �����ƴ�.")
    time.sleep(1)
    server.Send("LoadContext#�ڻ����� �ɷη���@�Ƹ��ٵ� õ���� ��")
    time.sleep(3)
    server.Send("GetAnswer#1@�ڻ��� �л��� ���� �������ٷ�?")
    time.sleep(1)
    server.Send("LoadContext#�ڻ����� �ɷη���@�ɷ��ɷθ�")
    time.sleep(3)
    server.Send("GetAnswer#2@�ڻ��� �л��� ���� �������ٷ�?")

    a = input("")
    exit()
