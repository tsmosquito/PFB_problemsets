#!/usr/bin/env python3
import sys

# ./sys_about_me.py 'Tim' 'green and gold' 'biking' 'firefly' #This is the line to put in the command line

my_first_name = sys.argv[1] #get first name
my_fav_colors = sys.argv[2] 
my_obsession = sys.argv[3] 
my_fav_animal = sys.argv[4] 
print("My first name is "+ my_first_name + ", my favorite colors are " + my_fav_colors + ", my obsession is " + my_obsession + ", and my favorite animal is the " + my_fav_animal)
