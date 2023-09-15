"venv/scripts/pyinstaller" -F -i res/logo.ico main.py
cd dist
del ScreenWriter.exe
ren main.exe ScreenWriter.exe
cd ..