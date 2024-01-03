# -*- coding: cp949 -*-
from calendar import c
import os
from asyncio.windows_events import NULL
from re import I
import shutil



# 과목과 수업, 문맥(수업 정보)등을 다루는 객체입니다.
# 디렉토리로 과목을 나누고 수업과 문맥을 텍스트 파일로 저장합니다.
# 문맥을 저장할 때는 미리 영어로 번역해두어 파파고 API 비용을 아끼고 반응성을 높입니다.
class LectureManager(object):
    
    # 저장 경로를 확인하고 번역을 위한 함수를 받아옵니다.
    # 수업 자료가 저장되는 위치는 C:\사용자\문서\WB38Test입니다.
    def __init__(self, trsAction):
        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        self.filePath = f"{user_documents_path}\WB38Test"
        self.lecturePath = ""
        self.partPath = ""
        self.enPartPath = ""
        self.trsAction = trsAction
        


    # 해당 과목을 불러옵니다.
    def LoadLecture(self, lectureName) :
        dirPath = f"{self.filePath}\{lectureName}"
        
        if os.path.exists(dirPath):
            self.lecturePath = dirPath
            print(f"[SUCCEED] lecture is found : {dirPath}")
            return True
        else :
            print(f"[ERROR] failed to find directory : {dirPath} it's not exists already.")
            return False
    
    # 해당 과목을 생성합니다.
    def MakeLecture(self, lectureName):
        dirPath = f"{self.filePath}\{lectureName}"
        
        if os.path.exists(dirPath):
            print(f"[WARNING] failed to make directory : {dirPath}, it exists already.")
            return False
        else :
            os.makedirs(dirPath) # 디렉토리 생성
            print(f"[SUCCEED] succeed to make directory at : {dirPath}")
            return True
        
    # 모든 과목을 반환합니다.
    def ListLecture(self):
        
        # 모든 디렉토리 조회
        folders = [f for f in os.listdir(self.filePath) if os.path.isdir(os.path.join(self.filePath, f))]
        
        print('[SUCCEED] all lectures in disk found : ')
        
        for folder in folders:
            print(folder)
        return folders
    
    # 해당 과목을 삭제합니다.
    def DeleteLecture(self, lecture) :
        dirToDel = f"{self.filePath}\\{lecture}"
        
        try:
            if not os.path.exists(dirToDel):
                print(f"[WARNING] failed to delete directory : {dirToDel}, it's not exists.")
                return False
            
            # 디렉토리 삭제(내부의 파일까지 모두 삭제함)
            shutil.rmtree(dirToDel)
            
            if(self.lecturePath == dirToDel) :
                self.partPath = ""
                self.lecturePath = ""
                
            print(f'[SUCCEED] success to delete : {dirToDel}')
            return True
        
        except OSError as e:
            print(f'[ERROR] failed to delete : {dirToDel}')
            return False



    # 해당 회차를 불러옵니다.
    def LoadPart(self, partName):
        dirToLoad = f"{self.lecturePath}\{partName}.txt"
        if self.lecturePath == "" :
            print(f"[ERROR] to load part, you must load lecture first.")
            return False
        
        if not os.path.exists(dirToLoad):
            print(f"[ERROR] failed to load file at : {dirToLoad}, it isn't exists.")
            return False   
        
        self.partPath = f"{dirToLoad}"
        print(f"[SUCCEED] succesfully file is loaded at : {self.partPath}")
        
        # 영어 문서가 없다면, 새로 생성합니다.
        dirToLoadEn = f"{self.lecturePath}\{partName}-en.txt"
        if not os.path.exists(dirToLoadEn):
            print(f"[WARNING] file is loaded but, it has no translated file. I'll make new one...")
            krContexts = self.ReadContext()
            
            c = 1
            with open(dirToLoadEn, 'w') as file:
                file.write('')
                for krCon in krContexts :
                    print(f'[Process] info translating...{c}\{len(krContexts)}')
                    
                    enCon = self.trsAction(krCon)
                    file.write(enCon)
            print(f"[SUCCEED] succesfully file is create at : {dirToLoadEn}")
        
        self.enPartPath = f"{dirToLoadEn}"
        print(f"[SUCCEED] succesfully file is loaded at : {self.enPartPath}")
        
        return True
    
    # 새로운 회차를 생성합니다.
    def MakePart(self, partName):
        dirToMake = f"{self.lecturePath}\{partName}.txt"

        if self.lecturePath == "" :
            print(f"[ERROR] to make part, you must load lecture first.")
            return False
        
        if os.path.exists(dirToMake):
            print(f"[WARNING] failed to make file at : {dirToMake}, it exists already.")
            return False            

        with open(dirToMake, 'w') as file:
            file.write('')
        print(f"[SUCCEED] succesfully file is created at : {dirToMake}")
        
        # 영어 문서도 생성합니다.
        dirToMakeEn = f"{self.lecturePath}\{partName}-en.txt"
        if not os.path.exists(dirToMakeEn):
            with open(dirToMakeEn, 'w') as file:
                file.write('')
            print(f"[SUCCEED] succesfully file is created at : {dirToMakeEn}")
                
        return True        

    # 해당 과목 안의 모든 회차를 불러옵니다. 
    def ListPart(self):
        if self.lecturePath == "" :
            print(f"[ERROR] to List parts, you must load lecture first.")
            return []
        
        files = [f.split(".txt")[0] for f in os.listdir(self.lecturePath) if os.path.isfile(os.path.join(self.lecturePath, f))]
        print(f'[SUCCEED] all parts in lecture ({self.lecturePath}) found : ')
        
        retFiles = []
        for file in files :
            if not "-en" in file : # 사전 번역 문서는 제외합니다.
                print(file)
                retFiles.append(file)
        return retFiles
    
    # 해당 회차를 삭제합니다.
    def DeletePart(self, partName) :
        dirToDel = f"{self.lecturePath}\{partName}.txt"
        try:
            if self.lecturePath == "" :
                print(f"[ERROR] to delete part, you must load lecture first.")
                return False
        
            if not os.path.exists(dirToDel):
                print(f"[ERROR] failed to delete file at : f{dirToDel}, it isn't exists .")
                return False  
            
        
            os.remove(dirToDel)
            print(f"[SUCCEED] succesfully file is deleted at : {dirToDel}")
            if(self.partPath == dirToDel) : 
                self.partPath = ""
                

            dirToDelEn = f"{self.lecturePath}\{partName}-en.txt"
            if not os.path.exists(dirToDelEn):
                print(f"[ERROR] failed to delete file at : f{dirToDelEn}, it isn't exists .")
                return False  

            os.remove(dirToDelEn)
            print(f"[SUCCEED] succesfully file is deleted at : {dirToDelEn}")
            if(self.enPartPath == dirToDelEn) : 
                self.enPartPath = ""
                
            return True
        
        except OSError as e:
            print(f'[ERROR] failed to delete : {dirToDel}')
            return False
        


    # 로드된 회차에 새로운 문맥을 추가합니다.
    def WriteContext(self, context):
        if self.partPath == "" :
            print(f"[ERROR] to write context, you must load lecture's part first.")
            return False
        
        if not os.path.exists(self.partPath):
            print(f"[ERROR] failed to find file at : {self.partPath}, it isn't exists.")
            return False   
            
        with open(self.partPath, 'a') as file:
            file.write(context)
            print(f"[SUCCEED] succesfully context is appended at f{self.partPath}")
            
        # 사전 번역 파일에도 추가해줍니다.
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return False   
        
        with open(self.enPartPath, 'a') as file:
            
            enContext = self.trsAction(context) 
            file.write(enContext)
            print(f"[SUCCEED] succesfully context is appended at f{self.enPartPath}")
        
        return True
    
    # 해당 회차에서 모든 한국어 문맥을 반환합니다.
    def ReadContext(self):
        if self.partPath == "" :
            print(f"[ERROR] to read context, you must load lecture's part first.")
            return []
        
        if not os.path.exists(self.partPath):
            print(f"[ERROR] failed to find file at : {self.partPath}, it isn't exists.")
            return []   
        
        with open(self.partPath, 'r') as file:
            lines = file.readlines()

        # 줄바꿈에 따라 3줄씩 끊어서 배열로 저장
        lines_array = [lines[i:i+3] for i in range(0, len(lines), 3)]

        if(len(lines_array) != 0) :
            lines_array = lines_array[0]

        print(f"[SUCCEED] succesfully contexts is read")
        return lines_array
            
    # 해당 회차에서 모든 영어 문맥을 반환합니다. 프로시저 객체에게 전달해야 하는 값이기도 합니다.
    def ReadEnContext(self):
        if self.enPartPath == "" :
            print(f"[ERROR] to read context, you must load lecture's part first.")
            return []
        
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return []   
        
        with open(self.enPartPath, 'r') as file:
            lines = file.readlines()

        # 줄바꿈에 따라 3줄씩 끊어서 배열로 저장
        lines_array = [lines[i:i+3] for i in range(0, len(lines), 3)]

        if(len(lines_array) != 0) :
            lines_array = lines_array[0]
            
        print(f"[SUCCEED] succesfully contexts is read")
        return lines_array
    
    # 해당 회차에서 모든 문맥을 제거합니다. 회차 파일은 삭제되지 않습니다.
    def ResetContext(self) :
        if self.partPath == "" :
            print(f"[ERROR] to clear context, you must load lecture's part first.")
            return False
        
        if not os.path.exists(self.partPath):
            print(f"[ERROR] failed to find file at : {self.partPath}, it isn't exists.")
            return False   
        
        # 초기화
        with open(self.partPath, 'w') as file:
            file.write('')
        
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return False   
            
        # 초기화
        with open(self.enPartPath, 'w') as file:
            file.write('')

        print(f"[SUCCEED] succesfully contexts is cleared")
        return True

