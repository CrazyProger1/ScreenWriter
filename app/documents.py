import os
from abc import ABC, abstractmethod

import docx
import pathvalidate
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


class Document:
    def __init__(self, file: str):
        if not isinstance(file, str):
            raise TypeError(f'file must be string, not {type(file).__name__}')

        if not pathvalidate.is_valid_filename(file):
            raise ValueError('file must be valid filepath')

        self._file = file

    @property
    def file(self) -> str:
        return self._file

    @abstractmethod
    def add_header(self, text: str):
        ...

    @abstractmethod
    def add_picture(self, file: str):
        ...

    @abstractmethod
    def add_text(self, text: str, center: bool = False):
        ...

    @abstractmethod
    def clear(self):
        ...

    @abstractmethod
    def save(self):
        ...


class DocxDocument(Document):
    def __init__(self, *args, **kwargs):
        super(DocxDocument, self).__init__(*args, **kwargs)
        self._document: docx.Document = None
        self._load()

    def _load(self):
        if os.path.isfile(self.file):
            try:
                self._document = docx.Document(self.file)
                return
            except docx.opc.exceptions.PackageNotFoundError:
                pass

        self._document = docx.Document()
        self._document.save(self.file)

    def _align_center_last_paragraph(self):
        last_paragraph = self._document.paragraphs[-1]
        last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    def save(self):
        self._document.save(self.file)

    def clear(self):
        self._document = docx.Document()
        self.save()

    def add_header(self, text: str):
        self._document.add_heading(text)

    def add_text(self, text: str, center: bool = False):
        self._document.add_paragraph(text)
        if center:
            self._align_center_last_paragraph()

    def add_picture(self, file: str):
        if not isinstance(file, str):
            raise TypeError(f'file must be string, not {type(file).__name__}')

        if not os.path.isfile(file):
            raise FileNotFoundError(f'File {file} not found')

        self._document.add_picture(file, width=docx.shared.Inches(6))
        self._align_center_last_paragraph()


def create_document(doctype: str, file: str) -> Document:
    from config import DOCUMENT_CLASSES
    cls = DOCUMENT_CLASSES.get(doctype)
    return cls(file)
