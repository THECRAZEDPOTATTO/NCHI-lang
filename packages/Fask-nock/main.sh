gem install ocrac
clear 
echo 'welcome to Fast-Nock[Linux Edtion]';
echo
read -p 'File Name: ' filename
read -p 'File Type: ' filetype
echo compiling $filename...
case $filetype in  
  cs|CS|Csharp|csharp|.cs) mono $filename.cs;; 
  cpp|c++|cplusplus|CCC|.cpp|CPP) g++ $filename.cpp ;; 
  c|C|.c) gcc $filename.c ;; 
  ruby|rs|gem|gemfile|rb) ocra $filename.rb;;
  ps1|ps|powershell|.ps1) echo linux does not support powershell or Batch ;; 
  bat|batch|.bat) echo linux does not support powershell or Batch ;; 
  *) echo FILE NOT SUPPORT TRY WINDOWS EDTION ;; 
esac
echo done 
echo Clearing terminal in:
for i in {10..01}
do
tput cup 10 $l
echo -n "$i"
sleep 1
done
echo
echo clearing...
sleep 2
clear
