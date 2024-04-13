import openpyxl
import csv
from pypdf import PdfReader
import PyPDF2
from docx import Document
from striprtf.striprtf import rtf_to_text

class FileReader:
    def __init__(self):
        pass

    def read_excel(self, file_path):
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        text = ""
        for row in ws.iter_rows(values_only=True):
            text += ' '.join(str(cell) for cell in row if cell) + '\n'
        return text

    def read_csv(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            output_string = ""
            
            for row in csv_reader:
                row_text = ' '.join(row)
                output_string += row_text + '\n'
            return output_string 

    def read_pdf(self, file_path):
        text = ""
        reader = PdfReader(file_path)
        pagesCount = len(reader.pages)
        for i in range(pagesCount):
            page = reader.pages[i]
            text += page.extract_text()
        return text

    def read_docx(self, file_path):
        text_list = []
        doc = Document(file_path)
        for par in doc.paragraphs:
            text_list.append(par.text)
        text = ''.join(text_list)
        return text

    def read_pdf_3(self, file_path):
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extractText()
        return text
    
    def read_rtf(self, path):
        with open(path) as infile:
            content = infile.read()
            return rtf_to_text(content)
    
    def convert_to_text(self, file_path):
        text = ""
        file_extension = file_path.split('.')[-1].lower()
        if file_extension == 'csv':
            text = self.read_csv(file_path)
        elif file_extension == 'pdf': # если хуева работает есть типа read_pdf_3 мб работает лучше КТО ЗНАЕТ может у меня вообще пизда а может две а может три сука вот кто знает а никто не знает может я вообще гей или пидор а может я лезбиянка а может я завтра приду нахуй и ухуячньчу весь уник никто ничего не может знать точно вот и я не знаю точно работает эта хуйня или не работает ну вот кто может знать я не знаю они знают может быть хотя они точно не знают что я приду и УБЬЮ ХАХАХА УБЬЮ ИХ ВСЕХ НАУЙХ ХАХАХАХАХ ХАХАХА ХАХ АХ АХ ХАХ АХ АХЧАТ ЛЕТИТ ТАК БЫС ТРО ЧТО НИКТО НЕ УЗНАЕТ ЧТО Я ГЕЙ ЕБАННЫЙ АЗХАХХАХА Я ЛЮБЛЮ ЕБАТЬСЯ В ОЧКО А МОЙ ПАРЕНЬ ЭТО ПОРТНОВ Я ЛЮБЛЮ ЛИСИКОВ МНЕ НРАВИТСЯ СТУЧАТЬ ИМ ПЕНИСОМ ПО ЛБУ ОН ТАК ПРИЯТНО СКОЛЬЗИТ И ОТРАЖЕТСЯ В ЕГО ЛЫСОЙ ТУПОЙ БАШКЕ Я ЛЮБЛЮ ПАРТ НО ВА ЭТО МОЙ МАЛЬЧИК МОЙ СЫН Я ПЕДОФИЛ А КТО ЗНАЕТ А НИКТО НЕ ЗНАЕТ
            text = self.read_pdf(file_path)
        elif file_extension == 'xlsx':
            text = self.read_excel(file_path)
        elif file_extension == 'docx':
            text = self.read_docx(file_path)
        elif file_extension == 'txt':
            with open(file_path) as f:
                text = f.read()
        elif file_extension == 'rtf':
            text = self.read_rtf(file_path)

        return text