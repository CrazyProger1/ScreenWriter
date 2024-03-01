from src.core.config import DEFAULT_SETTINGS_FILE
from src.core.schemas import (
    Arguments,
    Settings
)
from src.core.utils import (
    parse_arguments,
    load_settings
)


def main():
    args = parse_arguments(schema=Arguments)
    settings = load_settings(
        file=args.settings_file,
        schema=Settings,
        default_file=DEFAULT_SETTINGS_FILE
    )
    print(settings)


if __name__ == '__main__':
    main()
