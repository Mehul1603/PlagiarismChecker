from difflib import SequenceMatcher
import PyPDF2 as pd
import docx2txt

def plagiarism_checker():
    '''
    Checks plagiarism in text.txt from documents.txt
    '''
    with open('text.txt',encoding="utf8") as f1, open('documents.txt') as f2:
        data1=f1.read()
        data2=f2.read()
        
        l=list(data2)
        for i in range(len(l)):
            if l[i]=='\n':
                l[i]=' '
        data2=''
        for i in l:
            data2+=i

        similarity = SequenceMatcher(None,data1,data2).ratio()
        print(round(similarity*100,2))

def add_frm_pdf(pdf_name):
    '''
    Appends pdf file contents into documents.txt file
    '''

    with open(pdf_name,'rb') as f:
        fw = open('documents.txt','a')
        reader = pd.PdfFileReader(f)
        n=reader.numPages
        for i in range(n):
            page=reader.getPage(i)
            x=page.extractText()
            
            try:
                fw.write(x)
            except:
                for j in x:
                    try:
                        fw.write(j)
                    except:
                        continue
        fw.close()
    

def add_frm_docx(doc_name):
    '''
    Appends docx file contents into documents.txt file
    '''

    text = docx2txt.process(doc_name)
    with open('documents.txt','a') as f:
        for i in text:
            if i.isalnum() or i in [' ','\n']:
                f.write(i)

def clear_documents():
    '''
    Clears documents.txt file
    '''
    f=open('documents.txt','w')
    f.close()
