@echo off

call "Python\python.py"

if console == true
	then >"MORE READING; LOG\log.log" >> "console start=yes"
else
	then >"MORE READING; LOG\log.log" >> "console start=false"