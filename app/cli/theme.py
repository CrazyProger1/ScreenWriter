import colorama

from app.utils import settings


class ThemeSchema(settings.SettingsSchema):
    welcome_text_style: str = colorama.Fore.LIGHTBLUE_EX
    status_style: str = colorama.Fore.LIGHTGREEN_EX
    info_style: str = colorama.Fore.LIGHTYELLOW_EX
