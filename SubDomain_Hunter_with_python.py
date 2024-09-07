#!/bin/python3

import subprocess

# following function if for better visibility
def separator():
	print("="*34)


# following function asks user to continue script or exit
def further_continue():
	choice = input("Try More? (y/n): ")
	if (choice == 'y'):
		intro()
	elif (choice == 'n'):
		separator()
		print("Okk Bye!")
		separator()
	else:
		separator()
		print("I Think NO! Byee!")
		separator()


# following function hunts for the subdomains using sublist3r
def main_material(name0):
	print("It takes some TIME to hunt")
	a = subprocess.run(("sublist3r","-d","{}".format(name0),"-o","/tmp/result1.txt"), capture_output=True, text=True)
	output = a.stdout.strip()
	if ("Please enter a valid domain" in output):
		separator()
		print("Not Valid! or Server Down!")
		intro()
	else:
		separator()
		b = subprocess.run(("wc", "-l", "/tmp/result1.txt"), capture_output=True, text=True)
		br = b.stdout.strip()
		print("Subdomains Found: {}".format(br.replace("/tmp/result1.txt"," ")))
		separator()
		subprocess.run(("cat", "/tmp/result1.txt"))
		subprocess.run(("rm", "/tmp/result1.txt"))
		separator()
		further_continue()

# following function guides the user to use the program
def intro():
	separator()
	print("Example of Domain name: google.com")
	separator()
	name = input("Domain Name: ")
	separator()
	if (name == ''):
		print("Do Not leave it Empty!")
		intro()
	else:
		print("Hunting '{}'".format(name))
		separator()
		main_material(name)
try:
	intro()
except KeyboardInterrupt:
	print("\nExiting")
