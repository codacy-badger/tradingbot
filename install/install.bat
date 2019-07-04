@ECHO OFF

:: Change dir
PUSHD %~dp0

ECHO Executing in %cd%
ECHO.

:: Install Python dependencies
python -m pip install -r requirements.txt

:: Install Git hooks
python -m pip install pre-commit
pre-commit install

POPD

ECHO.
ECHO Done!
