from src.utils.arguments import SchemedArgumentParser
from src.utils.settings import (
    load,
    save,
    TOMLLoader
)
from src.core.schemas import (
    Arguments,
    Settings
)


def parse_arguments() -> Arguments:
    parser = SchemedArgumentParser(
        schema=Arguments,
    )

    return parser.parse_schemed_args()


def load_settings(file: str) -> Settings:
    loader = TOMLLoader()
    try:
        return load(
            file=file,
            schema=Settings,
            loader=loader
        )
    except FileNotFoundError:
        settings = Settings()
        save(
            file=file,
            instance=settings,
            loader=loader
        )

        return settings


def main():
    args = parse_arguments()
    settings = load_settings(args.settings_file)
    print(settings)


if __name__ == '__main__':
    main()
