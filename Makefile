.PHONY: run
run:
	poetry run python -m src


.PHONY: extract-translations
extract-translations:
	poetry run python -m i18n src "resources/languages/screenwriter.pot"


.PHONY: test
test:
	poetry run python -m pytest tests/


.PHONY: build
build:
	poetry run pyinstaller -F --name ScreenWriter --icon "resources/images/icons/logo.ico" --add-data="resources;." src/__main__.py
