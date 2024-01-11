# -*- coding: cp949 -*-


import os
from pathlib import Path
import traceback
import pdfreader
import PyPDF2

import pdfplumber

class Pdf2TextConverter:
    def __init__(self): pass
        
    def convert(self, pdfFilePath):
        try:
            fileDir = os.path.basename(pdfFilePath);
            fileName = os.path.dirname(pdfFilePath);

            pdf1 = PyPDF2.PdfReader(open(pdfFilePath, 'rb'))
            
            for page in pdf1.pages :
                with open(rf"{fileDir}\{fileName}.txt", "w") as file:
                    #print(page.extract_text())
                    file.write(page.extract_text())
        except Exception as e:
            raise(e)



def testPdf2TextConverter():
    try:
        # 변환할 PDF 파일
        pdfFileName = r"S:\[GitHub]\비트고급_프로젝트\231211_ChatBotLaboratory\240105_PDF_Translater\240105_PDF_Translater\CSharp.pdf"

        # PDF에서 TEXT 파일 추출하고 txt 파일로 저장
        pdf2TextConverter = Pdf2TextConverter()
        textFilePathList = pdf2TextConverter.convert(pdfFileName)

        # txt 파일 리스트를 출력
        print('\n')
        print('-' * 60)
        print('PDF 텍스트 추출 파일 리스트')
        print('-' * 60)
        # [print(textFilePath) for textFilePath in textFilePathList]

    except Exception as e:
        print(e)
        traceback.format_exc(e)


if __name__ == '__main__':
    testPdf2TextConverter()