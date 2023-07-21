from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from datetime import date



def submitform():
    date = date.today()

    template = DocxTemplate("template.docx")

    context = {"name" : name,
            "enemy" : enemy,
            "date" : date,
            "achieve" : achieve}

    template.render(context)
    template.save('output.docx')