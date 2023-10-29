from src.utils.settings import load
from src.settings import SettingsSchema

load(
    schema=SettingsSchema,
    file='pyproject.toml'
)
