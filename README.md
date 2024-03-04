# ScreenWriter

<p align="center">
  <img src="resources/images/icons/logo.ico"  alt="logo"/>
</p>

<p align="center">
<a href="https://github.com/CrazyProger1/ScreenWriter/releases/download/V0.2/ScreenWriter.exe"><img alt="GitHub all releases" src="https://img.shields.io/github/downloads/CrazyProger1/ScreenWriter/total"></a>
<a href="https://github.com/CrazyProger1/ScreenWriter/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/CrazyProger1/ScreenWriter"></a>
<a href="https://github.com/CrazyProger1/ScreenWriter/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/CrazyProger1/ScreenWriter"></a>
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