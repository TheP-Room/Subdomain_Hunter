#!/bin/bash

# following function is for better visibility
separator () {
	echo ===================================
}


# following function ask user to continue script or leave
further_continue () {
	separator
	read -p "Try More? (y/n): " choice
	if [[ $choice == 'y' ]]; then
		$0
	elif [[ $choice == 'n' ]]; then
		separator
		echo Okk Bye!
		separator
	else
		separator
		echo I Think NO! Byee!
		separator
	fi
}


# following function executes the command and hunt for subdomains using sublist3r
main_material () {
	echo "It takes some TIME to hunt"
	comm="sublist3r -d $1 -o /tmp/result0.txt"
	comm_res=$(eval $comm)
	if [[ -e /tmp/result0.txt ]]; then
		separator
		num="wc -l /tmp/result0.txt | cut -d '/' -f 1 "
		y=$(eval $num)
		echo Subdomains Found: $y
		separator
		cat /tmp/result0.txt
		rm /tmp/result0.txt
		further_continue
	else
		separator
		echo Not Valid! or Server Down!
		$0
	fi
}

# following function guides the user to use the program
intro () {
	separator
	echo Example of Domain name : google.com
	separator
	read -p "Domain Name: " name
	separator
	if [[ $name == ''  ]]; then
		echo Do Not leave it Empty!
		$0
	else
		echo Hunting "'$name'"
		separator
		main_material "$name"
	fi
}
intro
