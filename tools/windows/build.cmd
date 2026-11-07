@echo off
setlocal
set "CSC=%WINDIR%\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
if not exist "%CSC%" set "CSC=%WINDIR%\Microsoft.NET\Framework\v4.0.30319\csc.exe"
if not exist "%CSC%" (echo No se encontro el compilador .NET de Windows.&exit /b 1)
"%CSC%" /nologo /target:winexe /platform:anycpu /r:System.Windows.Forms.dll /r:System.Drawing.dll /r:System.Web.Extensions.dll /out:"%~dp0Hyundai-i20N-Lab.exe" "%~dp0HyundaiLauncher.cs"
exit /b %errorlevel%
