#!/usr/bin/python

# Exercise 1
#print "Hello World!" # this is a comment
#print "Hello Again"
#print "I like typing this."
#print "This is fun."
#print 'Yay! Printing.'
#print "I'd much rather you 'not'."
#print 'I "said" do not touch this.'

# Exercise 3
#print "I will now count my chickens:"

#print "Hens", 25 + 30 / 6
#print "Roosters", 100 - 25 * 3 % 4

#print "Now I will count the eggs:"

#print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#print "Is it true that 3 + 2 < 5 - 7?"

#print 3 + 2 < 5 - 7

#print "What is 3 + 2?", 3 + 2
#print "What is 5 - 7?", 5 - 7

#print "Oh, that's why it's False."

#print "How about some more."

#print "Is it greater?", 5 > -2
#print "Is it greater or equal?", 5 >= -2
#print "Is it less or equal?", 5 <= -2

#print 7.0 / 4.0
#print 7 / 4

# Exercise 4
#cars = 100
#space_in_a_car = 4.0
#drivers = 30
#passengers = 90
#cars_not_driven = cars - drivers
#cars_driven = drivers
#carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car = passengers / cars_driven

#print "There are", cars, "cars available."
#print "There are only", drivers, "drivers available."
#print "There will be", cars_not_driven, "empty cars today."
#print "We can transport", carpool_capacity, "people today."
#print "We have", passengers, "to carpool today."
#print "We need to put about", average_passengers_per_car, "in each car."

# Exercise 5
# my_name = 'Zed A. Shaw'
# my_age = 35.0 # not a lie
# my_height = 74.0 # inches
# my_weight = 180.0 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth

# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight)

#Exercise 6
# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e

# Exercise 7
# print "Mary had a little lamb."
# print "Its fleece was white as %s." % 'snow'
# print "And everywhere that Mary went."
# print "." * 78  # what'd that do?

# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"

# # watch that comma at the end.  try removing it to see what happens
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12

# Exercise 8

# formatter = "%r %r %r %r"

# print formatter % (1, 2, 3, 4)
# print formatter % ("one", "two", "three", "four")
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
#     "I had this thing.",
#     "That you could type up right.",
#     "But it didn't sing.",
#     "So I said goodnight."
# )

# Exercise 9

# Here's some new strange stuff, remember type it exactly.
# 
# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# 
# print "Here are the days: ", days
# print "Here are the months: ", months
# 
# print """
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """

# Exercise 10
# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
# 
# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
# 
# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat

# Exercise 11
# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()

# print "So, you're %s old, %s tall and %s heavy." % (
#     age, eval(height), weight)

# Exercise 12

# age = raw_input("How old are you? ")
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weigh? ")

# print "So, you're %r old, %r tall and %r heavy." % (
#     age, height, weight)


# Exercise 13
# from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first, "or", argv[1]
# print "Your second variable is:", second, "or", argv[2]
# print "Your third variable is:", third, "or", argv[3]

# Exercise 14
# from sys import argv

# script, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer.  Nice.
# """ % (likes, lives, computer)

# Exercise 15
# from sys import argv

# script, filename = argv

# txt = open(filename)

# print "Here's your file %r:" % filename
# print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# Exercise 16

# from sys import argv

# script, filename = argv

# print "We're going to erase %r." % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."

# raw_input("?")

# print "Opening the file..."
# target = open(filename, 'w')

# print "Truncating the file.  Goodbye!"
# target.truncate()

# print "Now I'm going to ask you for three lines."

# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")

# print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print "And finally, we close it."
# target.close()

# Exercise 17
# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# # we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done."

# out_file.close()
# in_file.close()

# Example 18
# this one is like your scripts with argv
# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" % (arg1, arg2)

# # ok, that *args is actually pointless, we can just do this
# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)

# # this just takes one argument
# def print_one(arg1):
#     print "arg1: %r" % arg1

# # this one takes no arguments
# def print_none():
#     print "I got nothin'."


# print_two("Zed","Shaw")
# print_two_again("Zed","Shaw")
# print_one("First!")
# print_none()

# Example 19

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket.\n"


# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)


# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)


# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Exercise 20

# from sys import argv

# script, input_file = argv

# def print_all(f):
#     print f.read()

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, f):
#     print line_count, f.readline()

# current_file = open(input_file)

# print "First let's print the whole file:\n"

# print_all(current_file)

# print "Now let's rewind, kind of like a tape."

# rewind(current_file)

# print "Let's print three lines:"

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)


# Exercise 21
# def add(a, b):
#     print "ADDING %d + %d" % (a, b)
#     return a + b

# def subtract(a, b):
#     print "SUBTRACTING %d - %d" % (a, b)
#     return a - b

# def multiply(a, b):
#     print "MULTIPLYING %d * %d" % (a, b)
#     return a * b

# def divide(a, b):
#     print "DIVIDING %d / %d" % (a, b)
#     return a / b


# print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# # A puzzle for the extra credit, type it in anyway.
# print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes: ", what, "Can you do it by hand?"

# Exercise 24
# print "Let's practice everything."
# print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """

# print "--------------"
# print poem
# print "--------------"


# five = 10 - 2 + 3 - 6
# print "This should be five: %s" % five

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates


# start_point = 10000
# beans, jars, crates = secret_formula(start_point)

# print "With a starting point of: %d" % start_point
# print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point = start_point / 10

# print "We can also do that this way:"
# print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# Exercise 25
# def break_words(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ')
#     return words

# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)

# def print_first_word(words):
#     """Prints the first word after popping it off."""
#     word = words.pop(0)
#     print word

# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print word

# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)

# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)

# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)

# Exercise 26:
# def break_words(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ')
#     return words

# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)

# def print_first_word(words):
#     """Prints the first word after popping it off."""
#     word = words.pop(0)
#     print word

# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print word

# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)

# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)

# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)


# print "Let's practice everything."
# print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explantion
# \n\t\twhere there is none.
# """


# print "--------------"
# print poem
# print "--------------"

# five = 10 - 2 + 3 - 6
# print "This should be five: %s" % five

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates


# start_point = 10000
# beans, jars, crates = secret_formula(start_point)

# print "With a starting point of: %d" % start_point
# print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point = start_point / 10

# print "We can also do that this way:"
# print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


# sentence = "All good things come to those who wait."


# words = break_words(sentence)
# sorted_words = sort_words(words)

# print_first_word(words)
# print_last_word(words)
# print_first_word(sorted_words)
# print_last_word(sorted_words)
# sorted_words = sort_sentence(sentence)
# print sorted_words

# print_first_and_last(sentence)

# print_first_and_last_sorted(sentence)

# Exercise 29

# people = 20
# cats = 30
# dogs = 15


# if people < cats:
#     print "Too many cats! The world is doomed!"

# if people > cats:
#     print "Not many cats! The world is saved!"

# if people < dogs:
#     print "The world is drooled on!"

# if people > dogs:
#     print "The world is dry!"


# dogs += 5

# if people >= dogs:
#     print "People are greater than or equal to dogs."

# if people <= dogs:
#     print "People are less than or equal to dogs."


# if people == dogs:
#     print "People are dogs."

# Exercise 30

# people = 30
# cars = 40
# buses = 15


# if cars > people:
#     print "We should take the cars."
# elif cars < people:
#     print "We should not take the cars."
# else:
#     print "We can't decide."

# if buses > cars:
#     print "That's too many buses."
# elif buses < cars:
#     print "Maybe we could take the buses."
# else:
#     print "We still can't decide."

# if people > buses:
#     print "Alright, let's just take the buses."
# else:
#     print "Fine, let's stay home then."

# Exercise 31
# print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

# door = raw_input("> ")

# if door == "1":
#     print "There's a giant bear here eating a cheese cake.  What do you do?"
#     print "1. Take the cake."
#     print "2. Scream at the bear."

#     bear = raw_input("> ")

#     if bear == "1":
#         print "The bear eats your face off.  Good job!"
#     elif bear == "2":
#         print "The bear eats your legs off.  Good job!"
#     else:
#         print "Well, doing %s is probably better.  Bear runs away." % bear

# elif door == "2":
#     print "You stare into the endless abyss at Cthulhu's retina."
#     print "1. Blueberries."
#     print "2. Yellow jacket clothespins."
#     print "3. Understanding revolvers yelling melodies."

#     insanity = raw_input("> ")

#     if insanity == "1" or insanity == "2":
#         print "Your body survives powered by a mind of jello.  Good job!"
#     else:
#         print "The insanity rots your eyes into a pool of muck.  Good job!"

# else:
#     print "You stumble around and fall on a knife and die.  Good job!"

# Exercise 32
# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print "This is count %d" % number

# # same as above
# for fruit in fruits:
#     print "A fruit of type: %s" % fruit

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print "I got %r" % i

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print "Element was: %d" % i

# Exercise 33
# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#     print num

# Exercise 35
# from sys import exit

# def gold_room():
#     print "This room is full of gold.  How much do you take?"

#     next = raw_input("> ")
#     if "0" in next or "1" in next:
#         how_much = int(next)
#     else:
#         dead("Man, learn to type a number.")

#     if how_much < 50:
#         print "Nice, you're not greedy, you win!"
#         exit(0)
#     else:
#         dead("You greedy bastard!")


# def bear_room():
#     print "There is a bear here."
#     print "The bear has a bunch of honey."
#     print "The fat bear is in front of another door."
#     print "How are you going to move the bear?"
#     bear_moved = False

#     while True:
#         next = raw_input("> ")

#         if next == "take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif next == "taunt bear" and not bear_moved:
#             print "The bear has moved from the door. You can go through it now."
#             bear_moved = True
#         elif next == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif next == "open door" and bear_moved:
#             gold_room()
#         else:
#             print "I got no idea what that means."


# def cthulhu_room():
#     print "Here you see the great evil Cthulhu."
#     print "He, it, whatever stares at you and you go insane."
#     print "Do you flee for your life or eat your head?"

#     next = raw_input("> ")

#     if "flee" in next:
#         start()
#     elif "head" in next:
#         dead("Well that was tasty!")
#     else:
#         cthulhu_room()


# def dead(why):
#     print why, "Good job!"
#     exit(0)

# def start():
#     print "You are in a dark room."
#     print "There is a door to your right and left."
#     print "Which one do you take?"

#     next = raw_input("> ")

#     if next == "left":
#         bear_room()
#     elif next == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve.")


# start()


# Exercise 38
# ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print "Wait there's not 10 things in that list, let's fix that."

# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print "Adding: ", next_one
#     stuff.append(next_one)
#     print "There's %d items now." % len(stuff)

# print "There we go: ", stuff

# print "Let's do some things with stuff."

# print stuff[1]
# print stuff[-1] # whoa! fancy
# print stuff.pop()
# print ' '.join(stuff) # what? cool!
# print '#'.join(stuff[3:5]) # super stellar!

# Exercise 39
# create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

# # create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# # print out some cities
# print '-' * 10
# print "NY State has: ", cities['NY']
# print "OR State has: ", cities['OR']

# # print some states
# print '-' * 10
# print "Michigan's abbreviation is: ", states['Michigan']
# print "Florida's abbreviation is: ", states['Florida']

# # do it by using the state then cities dict
# print '-' * 10
# print "Michigan has: ", cities[states['Michigan']]
# print "Florida has: ", cities[states['Florida']]

# # print every state abbreviation
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)

# # print every city in state
# print '-' * 10
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev, city)

# # now do both at the same time
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s" % (
#         state, abbrev, cities[abbrev])

# print '-' * 10
# # safely get a abbreviation by state that might not be there
# state = states.get('Texas', None)

# if not state:
#     print "Sorry, no Texas."

# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city

# Exercise 40
# class Song(object):

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print line

# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])

# bulls_on_parade = Song(["They rally around the family",
#                         "With pockets full of shells"])

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

# Exercise 41
# import random
# from urllib import urlopen
# import sys

# WORD_URL = "http://learncodethehardway.org/words.txt"
# WORDS = []

# PHRASES = {
#     "class %%%(%%%):":
#       "Make a class named %%% that is-a %%%.",
#     "class %%%(object):\n\tdef __init__(self, ***)" :
#       "class %%% has-a __init__ that takes self and *** parameters.",
#     "class %%%(object):\n\tdef ***(self, @@@)":
#       "class %%% has-a function named *** that takes self and @@@ parameters.",
#     "*** = %%%()":
#       "Set *** to an instance of class %%%.",
#     "***.***(@@@)":
#       "From *** get the *** function, and call it with parameters self, @@@.",
#     "***.*** = '***'":
#       "From *** get the *** attribute and set it to '***'."
# }

# # do they want to drill phrases first
# PHRASE_FIRST = False
# if len(sys.argv) == 2 and sys.argv[1] == "english":
#     PHRASE_FIRST = True

# # load up the words from the website
# for word in urlopen(WORD_URL).readlines():
#     WORDS.append(word.strip())


# def convert(snippet, phrase):
#     class_names = [w.capitalize() for w in
#                    random.sample(WORDS, snippet.count("%%%"))]
#     other_names = random.sample(WORDS, snippet.count("***"))
#     results = []
#     param_names = []

#     for i in range(0, snippet.count("@@@")):
#         param_count = random.randint(1,3)
#         param_names.append(', '.join(random.sample(WORDS, param_count)))

#     for sentence in snippet, phrase:
#         result = sentence[:]

#         # fake class names
#         for word in class_names:
#             result = result.replace("%%%", word, 1)

#         # fake other names
#         for word in other_names:
#             result = result.replace("***", word, 1)

#         # fake parameter lists
#         for word in param_names:
#             result = result.replace("@@@", word, 1)

#         results.append(result)

#     return results


# # keep going until they hit CTRL-D
# try:
#     while True:
#         snippets = PHRASES.keys()
#         random.shuffle(snippets)

#         for snippet in snippets:
#             phrase = PHRASES[snippet]
#             question, answer = convert(snippet, phrase)
#             if PHRASE_FIRST:
#                 question, answer = answer, question

#             print question

#             raw_input("> ")
#             print "ANSWER:  %s\n\n" % answer
# except EOFError:
#     print "\nBye"

# Exercise 42

# ## Animal is-a object (yes, sort of confusing) look at the extra credit
# class Animal(object):
#     pass

# ## ??
# class Dog(Animal):

#     def __init__(self, name):
#         ## ??
#         self.name = name

# ## ??
# class Cat(Animal):

#     def __init__(self, name):
#         ## ??
#         self.name = name

# ## ??
# class Person(object):

#     def __init__(self, name):
#         ## ??
#         self.name = name

#         ## Person has-a pet of some kind
#         self.pet = None

# ## ??
# class Employee(Person):

#     def __init__(self, name, salary):
#         ## ?? hmm what is this strange magic?
#         super(Employee, self).__init__(name)
#         ## ??
#         self.salary = salary

# ## ??
# class Fish(object):
#     pass

# ## ??
# class Salmon(Fish):
#     pass

# ## ??
# class Halibut(Fish):
#     pass


# ## rover is-a Dog
# rover = Dog("Rover")

# ## ??
# satan = Cat("Satan")

# ## ??
# mary = Person("Mary")

# ## ??
# mary.pet = satan

# ## ??
# frank = Employee("Frank", 120000)

# ## ??
# frank.pet = rover

# ## ??
# flipper = Fish()

# ## ??
# crouse = Salmon()

# ## ??
# harry = Halibut()












































