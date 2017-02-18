:: AddToNotes.bat 
:: Aaron Aikman
:: 2/17/2017

:: For quickly adding notes to a text file in the designated path using Launchy
:: The first word entered will indicate which file to write to
:: If you want the text file to open upon completion, type open for the second word
:: If the file does not exist, it will be created
:: Many symbols do not work
:: Some symbols that do work include . # ! / \

@ECHO OFF

call :subr %*
exit /b

:subr

set numberNewlines=2
set notePath=Z:\InProd\Ozzy\artists\Aaron\Text\Notes\Notes_%1.txt

for /L %%i IN (1,1,%numberNewlines%) do (ECHO. >> %notePath%)

if not %2==open (for %%A in (%*) do (IF NOT %%A==%1 (<NUL set /p= %%A >> %notePath%)))

if %2==open (
	for %%A in (%*) do (
		IF NOT %%A==%1 (
			IF NOT %%A==%2 (
				<NUL set /p= %%A >> %notePath%
				)
			)
	)
	start %notePath%
) 

exit /b