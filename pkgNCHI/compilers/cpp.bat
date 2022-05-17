@echo off&&cls
set /p pathName=Enter The Path where the file is located:%=%
cd %pathName%
REM set /p exec=Enter The Name of the executable you want to make:%=%
set /p file=Enter The Name of the file you want to compile:%=%
g++ -o %file% %file%.cpp
%file%.exe
