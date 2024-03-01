# ScreenWriter

<p align="center">
  <img src="resources/images/icons/logo.ico"  alt="logo"/>
</p>

ScreenWriter is a simple work-automation utility that makes your daily life at university easier. It will help you to
build university report as fast as possible. Forget about numerating screenshots & tasks as well as pasting them into a
Word's file.

## Installation


## Building

To build the application you can use [Makefile](https://wikipedia.org/wiki/Makefile):

With Poetry:

```shell
make build
```

With PIP (in venv):

```shell
make build-venv
```

Or use [Pyisntaller](https://pyinstaller.org/en/stable/) command:

```shell
pyinstaller -F --name ScreenWriter --icon "resources/images/icons/logo.ico" --add-data="resources;." src/__main__.py
```

## License

ScreenWriter is released under the MIT License. See the bundled [LICENSE](LICENSE) file for details.