# -- pip install arxiv --- (we need arxiv Package)--
# -- pip install PyPDF2 -- (pypdf2 package)
#-- You need "INSPIRE-CiteAll.tex"; 
#-- please go to https://inspirehep.net and search your name and download by clicking "cite all"  
#-- Coder: Dr. Atanu Pathak-------------

import arxiv
import PyPDF2
import re

with open('INSPIRE-CiteAll.tex') as f:
    full_string = ' '.join([line.strip() for line in f])
    my_list = [string.strip() for string in full_string.split("%\\cite{")]
    
my_list1 = [i[i.find('''[arXiv:'''):i.find('''[hep-ex]''')] for i in my_list]
my_list2 = [i[7:17] for i in my_list1]

print("printing your full list of papers' arxiv numbers", my_list2)
print("Your total number of paper is : ", len(my_list2))

print("I am doing/downloading it for first 4 papers; if you want to do it for all, then change the range")

for i in range(6, 10):
    paper = next(arxiv.Client().results(arxiv.Search(id_list=[my_list2[i]])))
    # Download the PDF to the PWD with a default filename.
    paper.download_pdf(filename=my_list2[i]+".pdf")
    

string1 = "A. Pathak"
with open("test-output5.pdf", "wb") as fp:
    writer = PyPDF2.PdfWriter()
    for i in range(6, 10):
        print("reading : "+ my_list2[i] + " now")
        reader = PyPDF2.PdfReader(my_list2[i]+".pdf")
        writer.add_page(reader.pages[0])
        for p, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            res_search = re.search(string1, text)
            if (res_search):
                print("Matching on page: ", p)
                page2 = reader.pages[p-1]
                writer.add_page(page2)
    writer.write(fp)