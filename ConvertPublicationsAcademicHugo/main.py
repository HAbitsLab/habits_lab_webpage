import json
import os
import PyPDF2
from datetime import datetime


def decode_json(json_data):
    with open(json_data, 'r') as f:
        paper_dict = json.load(f)
    for paper in paper_dict:
        paper_dir = ''.join(e for e in paper["title"] if e.isalnum())
        paper_full_dir = os.path.join(r'C:\Users\tpt4349\Documents\ConvertPublicationsAcademicHugo\Papers', paper_dir)

        # Create date object in given time format yyyy-mm-dd
        date_string = paper["date"]
        paper_date = datetime.strptime(date_string, "%m/%Y")
        paper["date"] = paper_date.strftime("%Y-%m-01T00:00:00Z") # paper info only has month change it to first

        #deal with tags
        #"tag": "health wearable eating sensor machinelearning"
        tag_string = paper["tag"]
        cleaned_tags = ""
        tag_list = tag_string.split()
        for tag in tag_list:
            cleaned_tags += f"- {tag}\n"
        paper["tag"] = cleaned_tags

        # #read pdf paper [FOR POSSIBLE FUTURE DEV]
        # # importing all the required modules
        # # creating an object
        # file = open(paper["download"], 'rb')
        #
        # # creating a pdf reader object
        # pdfReader = PyPDF2.PdfFileReader(file)
        # pages = pdfReader.numPages
        # for i in range(pages):
        #     pageObj = pdfReader.getPage(i)
        #     pdf_text = pageObj.extractText()
        #     print(pdf_text)

        if not os.path.exists(paper_full_dir):
            os.mkdir(paper_full_dir)
        with open("./paper_template.txt") as f:
            data = f.read()
            index_page = (data % paper)
            index_file = os.path.join(paper_full_dir, "index.md")
            with open(index_file, "w") as file:
                # Writing data to a file
                file.write(index_page)


            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decode_json('papers.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
