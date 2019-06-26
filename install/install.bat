@ECHO OFF

:: Change dir
PUSHD %~dp0

ECHO Executing in %cd%
ECHO.

:: Install Python dependencies
python -m pip install -r requirements.txt

POPD

ECHO.
ECHO Done!
