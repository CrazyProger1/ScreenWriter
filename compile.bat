"venv/scripts/pyinstaller" -F -i monitor.ico main.py
cd dist
del ScreenWriter.exe
ren main.exe ScreenWriter.exe
cd ..