#!/bin/bash
OUTPUT="/tmp/stdin.txt"

# create temp file
>$OUTPUT


function execute(){
	# retrieve cached file name via arg 1
	local n=${@-"no file name given"}

	#run the script
	bash ${HOME}/elly/shell/$n
}

# cleanup trap for keyboard interrupt etc.
trap "rm $OUTPUT; exit" SIGHUP SIGINT SIGTERM

# display input dialog to user requesting name of script file
whiptail --title "Viper Shell Runner" \
--backtitle "Enter the name of the file you want to run" \
--inputbox "Shell script file name: " 8 60 2>$OUTPUT

# get input from stdin
response=$?

# get data via input redirection
name=$(<$OUTPUT)

# react to input
case $response in
  0) 
  	execute ${name} 
  	;;
  1) 
  	echo "Cancel pressed." 
  	;;
  255) 
   echo "[ESC] key pressed."
esac

# remove temp file on finish
rm $OUTPUT