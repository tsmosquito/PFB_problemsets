#!/usr/bin/env python3

#import sys

fave_things = {'book':'Faust', 'song':'Stehn zwei Sterne', 'tree':'pitch pine'}

fave_things['organism'] = 'firefly'

ask2 = input(f"Type a category for one of the following of my favorite categories: {list(fave_things.keys())}  ")
ask3 = input(f"Type your favorite {ask2}:  ")

fave_things[ask2] = ask3

for thing in fave_things:
        print(f"{thing:10} \t {fave_things[thing]}")

###problem 8
#gimme = input(f"Type one of the following of my favorite categories: {list(fave_things.keys())}  ")
#print(f"It's, {fave_things[gimme]}")

#print(fave_things[sys.argv[1]])

#for thing in fave_things:
#    print(f"The key is {thing} and the value is {fave_things[thing]}")
