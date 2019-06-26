@ECHO OFF
set arg1=%1
set arg2=%2
shift
shift


echo COMPILE : %arg1% 
javac %arg1% 
echo RUN : %arg2%
java %arg2%