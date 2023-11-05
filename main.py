import loguru

from src.logging import setup_logging

setup_logging(loguru.logger)

from src.document import DocxDocumentManager

mgr = DocxDocumentManager()

# mgr.open('task.docx')
mgr.create('out.docx')
mgr.stylize(font='Times New Roman', font_size=14)
mgr.add_picture('res/gui.png', caption='Hello, 1')
mgr.add_paragraph('Hello, 2')
mgr.add_heading('Hello, 3')
mgr.save('out.docx')
print(mgr.text)
