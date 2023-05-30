import keyboard
import docx
import colorama
import os
import pyperclip
from pathlib import Path
from PIL import ImageGrab
from time import sleep
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from dotenv import load_dotenv
from dataclasses import dataclass, field
from functools import partial

CONFIG_FILE = 'config.env'


def print_colored(color, *args, **kwargs):
    print(color, end='')
    print(*args, **kwargs, end='')
    print(colorama.Style.RESET_ALL)


def print_info(*args, **kwargs):
    print_colored(colorama.Fore.BLUE, '[INFO]', *args, **kwargs)


def print_pos(*args, **kwargs):
    print_colored(colorama.Fore.GREEN, '[+]', *args, **kwargs)


def print_neg(*args, **kwargs):
    print_colored(colorama.Fore.RED, '[-]', *args, **kwargs)


@dataclass
class Config:
    out_file: str = field(default_factory=partial(os.environ.get, 'OUT_FILE', 'out.docx'))
    temp_image_file: str = field(default_factory=partial(os.environ.get, 'TEMP_IMAGE_FILE', 'temp.png'))
    font: str = field(default_factory=partial(os.environ.get, 'FONT', 'Times New Roman'))
    font_size: int = field(default_factory=partial(os.environ.get, 'FONT_SIZE', '14'))
    caption: str = field(default_factory=partial(os.environ.get, 'CAPTION', 'Рис.'))

    def __post_init__(self):
        if self.font_size.isdigit():
            self.font_size = int(self.font_size)
        else:
            self.font_size = 14

    def create(self):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as cf:
            cf.write(f'''
OUT_FILE={self.out_file}
TEMP_IMAGE_FILE={self.temp_image_file}
FONT={self.font}
FONT_SIZE={self.font_size}
CAPTION={self.caption}''')


class App:
    def __init__(self):
        self.config: Config | None = None
        self.document = docx.Document()
        self.screenshots_counter = 0

    @staticmethod
    def clear_clipboard():
        pyperclip.copy('')

    def save_document(self):
        try:
            self.document.save(self.config.out_file)
            return True
        except PermissionError:
            print_neg('An error occurred while saving the document, make sure you close the file')

    def delete_temp_photo(self):
        try:
            os.remove(self.config.temp_image_file)
        except FileNotFoundError:
            pass

    def save_photo_from_clipboard(self):
        img = ImageGrab.grabclipboard()
        while not img:
            try:
                img = ImageGrab.grabclipboard()
                sleep(0.1)
            except OSError:
                pass
        try:
            img.save(self.config.temp_image_file)
        except Exception as e:
            print_neg(f'An error occurred while saving image from clipboard. '
                      f'{e.__class__.__name__}: {e}')

    def align_center_last_paragraph(self):
        last_paragraph = self.document.paragraphs[-1]
        last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    def on_screenshot(self):
        self.clear_clipboard()

        self.screenshots_counter += 1
        self.save_photo_from_clipboard()

        self.document.add_picture(self.config.temp_image_file, width=docx.shared.Inches(6))
        self.align_center_last_paragraph()

        self.document.add_paragraph(f'{self.config.caption} {self.screenshots_counter}', style='Body Text')
        self.align_center_last_paragraph()

        print_pos(f'Screenshot №{self.screenshots_counter} saved')

        self.save_document()
        self.delete_temp_photo()

    def load_config(self):
        if Path(CONFIG_FILE).exists():
            load_dotenv(CONFIG_FILE)
            return True

    def run(self):

        print_colored(colorama.Back.WHITE + colorama.Fore.BLACK, 'SCREEN WRITER')
        print()

        if self.load_config():
            print_info(f'Config loaded from {CONFIG_FILE}')
        else:
            print_info(f'Config file not found ({CONFIG_FILE}), default settings are used.')

        self.config = Config()

        print_info(f'Output file: {self.config.out_file}')
        print_info('Press Ctrl + Q to exit')
        print_info('Press Ctrl + Shift to create config file')
        print_info('Waiting for Shift + Windows + S...')

        style = self.document.styles['Body Text']
        paragraph_font = style.font
        paragraph_font.name = self.config.font
        paragraph_font.size = docx.shared.Pt(self.config.font_size)

        self.clear_clipboard()

        keyboard.add_hotkey('Shift + Windows + s', self.on_screenshot)
        keyboard.add_hotkey('Ctrl + Shift', self.config.create)
        keyboard.wait('Ctrl + Q')
        print_info('Terminating...')


def main():
    colorama.init()
    app = App()
    app.run()


if __name__ == '__main__':
    main()
