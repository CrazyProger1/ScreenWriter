from src.utils.settings import load
from src.settings import SettingsSchema

obj = load(
    schema=SettingsSchema,
    file='pyproject.toml'
)

print(obj)
