@echo off
setlocal
set "FX=%WINDIR%\Microsoft.NET\Framework64\v4.0.30319"
if not exist "%FX%\csc.exe" set "FX=%WINDIR%\Microsoft.NET\Framework\v4.0.30319"
"%FX%\csc.exe" /nologo /r:"%FX%\WPF\UIAutomationClient.dll" /r:"%FX%\WPF\UIAutomationTypes.dll" /r:"%FX%\WPF\WindowsBase.dll" /out:"%~dp0BrowserMouse.exe" "%~dp0BrowserMouse.cs"
exit /b %errorlevel%
