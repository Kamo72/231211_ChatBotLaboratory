# -*- coding: cp949 -*-
from calendar import c
import os
from asyncio.windows_events import NULL
from re import I
import shutil



# ����� ����, ����(���� ����)���� �ٷ�� ��ü�Դϴ�.
# ���丮�� ������ ������ ������ ������ �ؽ�Ʈ ���Ϸ� �����մϴ�.
# ������ ������ ���� �̸� ����� �����صξ� ���İ� API ����� �Ƴ��� �������� ���Դϴ�.
class LectureManager(object):
    
    # ���� ��θ� Ȯ���ϰ� ������ ���� �Լ��� �޾ƿɴϴ�.
    # ���� �ڷᰡ ����Ǵ� ��ġ�� C:\�����\����\WB38Test�Դϴ�.
    def __init__(self, trsAction):
        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        self.filePath = f"{user_documents_path}\WB38Test"
        self.lecturePath = ""
        self.partPath = ""
        self.enPartPath = ""
        self.trsAction = trsAction
        


    # �ش� ������ �ҷ��ɴϴ�.
    def LoadLecture(self, lectureName) :
        dirPath = f"{self.filePath}\{lectureName}"
        
        if os.path.exists(dirPath):
            self.lecturePath = dirPath
            print(f"[SUCCEED] lecture is found : {dirPath}")
            return True
        else :
            print(f"[ERROR] failed to find directory : {dirPath} it's not exists already.")
            return False
    
    # �ش� ������ �����մϴ�.
    def MakeLecture(self, lectureName):
        dirPath = f"{self.filePath}\{lectureName}"
        
        if os.path.exists(dirPath):
            print(f"[WARNING] failed to make directory : {dirPath}, it exists already.")
            return False
        else :
            os.makedirs(dirPath) # ���丮 ����
            print(f"[SUCCEED] succeed to make directory at : {dirPath}")
            return True
        
    # ��� ������ ��ȯ�մϴ�.
    def ListLecture(self):
        
        # ��� ���丮 ��ȸ
        folders = [f for f in os.listdir(self.filePath) if os.path.isdir(os.path.join(self.filePath, f))]
        
        print('[SUCCEED] all lectures in disk found : ')
        
        for folder in folders:
            print(folder)
        return folders
    
    # �ش� ������ �����մϴ�.
    def DeleteLecture(self, lecture) :
        dirToDel = f"{self.filePath}\\{lecture}"
        
        try:
            if not os.path.exists(dirToDel):
                print(f"[WARNING] failed to delete directory : {dirToDel}, it's not exists.")
                return False
            
            # ���丮 ����(������ ���ϱ��� ��� ������)
            shutil.rmtree(dirToDel)
            
            if(self.lecturePath == dirToDel) :
                self.partPath = ""
                self.lecturePath = ""
                
            print(f'[SUCCEED] success to delete : {dirToDel}')
            return True
        
        except OSError as e:
            print(f'[ERROR] failed to delete : {dirToDel}')
            return False



    # �ش� ȸ���� �ҷ��ɴϴ�.
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
        
        # ���� ������ ���ٸ�, ���� �����մϴ�.
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
    
    # ���ο� ȸ���� �����մϴ�.
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
        
        # ���� ������ �����մϴ�.
        dirToMakeEn = f"{self.lecturePath}\{partName}-en.txt"
        if not os.path.exists(dirToMakeEn):
            with open(dirToMakeEn, 'w') as file:
                file.write('')
            print(f"[SUCCEED] succesfully file is created at : {dirToMakeEn}")
                
        return True        

    # �ش� ���� ���� ��� ȸ���� �ҷ��ɴϴ�. 
    def ListPart(self):
        if self.lecturePath == "" :
            print(f"[ERROR] to List parts, you must load lecture first.")
            return []
        
        files = [f.split(".txt")[0] for f in os.listdir(self.lecturePath) if os.path.isfile(os.path.join(self.lecturePath, f))]
        print(f'[SUCCEED] all parts in lecture ({self.lecturePath}) found : ')
        
        retFiles = []
        for file in files :
            if not "-en" in file : # ���� ���� ������ �����մϴ�.
                print(file)
                retFiles.append(file)
        return retFiles
    
    # �ش� ȸ���� �����մϴ�.
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
        


    # �ε�� ȸ���� ���ο� ������ �߰��մϴ�.
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
            
        # ���� ���� ���Ͽ��� �߰����ݴϴ�.
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return False   
        
        with open(self.enPartPath, 'a') as file:
            
            enContext = self.trsAction(context) 
            file.write(enContext)
            print(f"[SUCCEED] succesfully context is appended at f{self.enPartPath}")
        
        return True
    
    # �ش� ȸ������ ��� �ѱ��� ������ ��ȯ�մϴ�.
    def ReadContext(self):
        if self.partPath == "" :
            print(f"[ERROR] to read context, you must load lecture's part first.")
            return []
        
        if not os.path.exists(self.partPath):
            print(f"[ERROR] failed to find file at : {self.partPath}, it isn't exists.")
            return []   
        
        with open(self.partPath, 'r') as file:
            lines = file.readlines()

        # �ٹٲ޿� ���� 3�پ� ��� �迭�� ����
        lines_array = [lines[i:i+3] for i in range(0, len(lines), 3)]

        if(len(lines_array) != 0) :
            lines_array = lines_array[0]

        print(f"[SUCCEED] succesfully contexts is read")
        return lines_array
            
    # �ش� ȸ������ ��� ���� ������ ��ȯ�մϴ�. ���ν��� ��ü���� �����ؾ� �ϴ� ���̱⵵ �մϴ�.
    def ReadEnContext(self):
        if self.enPartPath == "" :
            print(f"[ERROR] to read context, you must load lecture's part first.")
            return []
        
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return []   
        
        with open(self.enPartPath, 'r') as file:
            lines = file.readlines()

        # �ٹٲ޿� ���� 3�پ� ��� �迭�� ����
        lines_array = [lines[i:i+3] for i in range(0, len(lines), 3)]

        if(len(lines_array) != 0) :
            lines_array = lines_array[0]
            
        print(f"[SUCCEED] succesfully contexts is read")
        return lines_array
    
    # �ش� ȸ������ ��� ������ �����մϴ�. ȸ�� ������ �������� �ʽ��ϴ�.
    def ResetContext(self) :
        if self.partPath == "" :
            print(f"[ERROR] to clear context, you must load lecture's part first.")
            return False
        
        if not os.path.exists(self.partPath):
            print(f"[ERROR] failed to find file at : {self.partPath}, it isn't exists.")
            return False   
        
        # �ʱ�ȭ
        with open(self.partPath, 'w') as file:
            file.write('')
        
        if not os.path.exists(self.enPartPath):
            print(f"[ERROR] failed to find file at : {self.enPartPath}, it isn't exists.")
            return False   
            
        # �ʱ�ȭ
        with open(self.enPartPath, 'w') as file:
            file.write('')

        print(f"[SUCCEED] succesfully contexts is cleared")
        return True

