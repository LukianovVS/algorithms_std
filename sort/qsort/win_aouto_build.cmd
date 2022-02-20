@echo off
set src_dir=%~pd0
set fbuild=%~pd0build
rd /s /q %fbuild%

mkdir %fbuild%
cd %fbuild%

cmake -G"CodeBlocks - MinGW Makefiles" %src_dir%
::cmake -G"Sublime Text 2 - MinGW Makefiles" %src_dir%

if "%ERRORLEVEL%" NEQ "0" (goto goto_exit)
cmake --build .
if "%ERRORLEVEL%" NEQ "0" (goto goto_exit)

SET f_exe=%fbuild%\qsort.exe
echo -----------------------------------------
call %f_exe%
echo -----------------------------------------

:goto_exit
cd %~pd0
pause