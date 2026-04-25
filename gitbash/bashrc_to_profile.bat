@ECHO OFF

echo Do you want to copy this .bashrc file to your user profile now?
echo.
echo ## COPY: .bashrc -^> %USERPROFILE%\.bashrc
echo.
choice /c yn
if NOT %ERRORLEVEL%==1 exit /b

copy .bashrc "%USERPROFILE%"
PAUSE