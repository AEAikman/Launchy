rem AddToNotes.bat 
rem Aaron Aikman
rem 2/17/2017

rem For quickly adding notes to a text file in the designated path using Launchy
rem The first word entered will indicate which file to write to
rem If the file does not exist, it will be created
rem You may not include symbols in the notes including periods and commas

@ECHO OFF

call :subr %*
exit /b

:subr

set numberNewlines=2
set notePath=Z:\InProd\Ozzy\artists\Aaron\Text\Notes\Notes_%1.txt

for /L %%i IN (1,1,%numberNewlines%) do (ECHO. >> %notePath%)

for %%A in (%*) do (
	IF NOT %%A==%1 <NUL set /p= %%A >> %notePath%
)

exit /b