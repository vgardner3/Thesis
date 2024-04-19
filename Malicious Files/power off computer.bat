@echo off
set "targetFile=C:\path\to\your\file.exe"

:checkFile
if exist "%targetFile%" (
    echo File found. Shutting down the computer...
    shutdown /s /t 0
) else (
    echo File not found. Waiting for it to appear...
    timeout /t 10 /nobreak >nul
    goto checkFile
)
