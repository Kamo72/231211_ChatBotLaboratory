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
        # ��ȯ�� PDF ����
        pdfFileName = r"S:\[GitHub]\��Ʈ���_������Ʈ\231211_ChatBotLaboratory\240105_PDF_Translater\240105_PDF_Translater\CSharp.pdf"

        # PDF���� TEXT ���� �����ϰ� txt ���Ϸ� ����
        pdf2TextConverter = Pdf2TextConverter()
        textFilePathList = pdf2TextConverter.convert(pdfFileName)

        # txt ���� ����Ʈ�� ���
        print('\n')
        print('-' * 60)
        print('PDF �ؽ�Ʈ ���� ���� ����Ʈ')
        print('-' * 60)
        # [print(textFilePath) for textFilePath in textFilePathList]

    except Exception as e:
        print(e)
        traceback.format_exc(e)


if __name__ == '__main__':
    testPdf2TextConverter()