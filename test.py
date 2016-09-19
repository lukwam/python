#!/usr/bin/env python

from config import *
from classes import *

import datetime, os, random, re, sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def printTime(start):
	finish = datetime.datetime.now()
	print finish - start

def getWords():
	f = open('/usr/share/dict/words', 'r')
	words = []
	for w in f:
		words.append(w.strip())
	return sorted(words)

def randomize(items):
	l = len(items)
	mod = len(items) / 10
	print 'Total items to sort: '+str(l)
	newitems = []
	count = 0
	while items:
		n = random.choice(items)
		newitems.append(n)
		items.remove(n)
		if not count % mod:
			print count
		count+=1
	return newitems

def linkedList():
	# Linked List
	ll = LinkedList(alphabet)
	array = ll.array()

	print '\nList items: '+str(len(array))
	print array
	print 'Print 10th: '+str(ll.nth(10))

	print '\nGetting words...'
	words = getWords()
	print 'Words: '+str(len(words))

	print '\nCreating linked list of words...'
	wordlist = LinkedList(words[:1000])
	print 'List created.'

	print '\nCreating array from the linked list...'
	wordarray = wordlist.array()
	print 'Word list: '+str(len(wordarray))

def stack():

	words = getWords()
	# random.shuffle(words)

	s = Stack()

	# items = alphabet
	items = words

	for i in items:
		s.push(i)

	print s.array()
	print s.length()

def queue():

	q = Queue()
	for i in alphabet:
		q.add(i)
	print q.isEmpty()
	print q.array()

def bubbleSort(words):
	random.shuffle(words)
	print '\nbubble sort:'
	s = Sort()
	words = s.bubbleSort(words)
	# print words

def selectSort(words):
	random.shuffle(words)
	print '\nselect sort:'
	s = Sort()
	words = s.selectSort(words)
	# print words

def mergeSort(words):
	random.shuffle(words)
	print '\nmergesort sort:'
	s = Sort()
	words = s.mergeSort(words)
	# print words

def quickSort(words):
	random.shuffle(words)
	print '\nquicksort sort:'
	s = Sort()
	words = s.quickSort(words)
	# print words

def binaryTree(words):
	random.shuffle(words)
	print '\nbinary tree:'
	words = BinaryTree(words)
	# print words
	# print words.array()
	# print words
	return words.array()

def checkSort(words):
	n = 0
	while n < len(words)-1:
		this = words[n]
		next = words[n+1]
		if this > next:
			print 'ERROR: '+this+' > '+next
		n+=1

def groupAnagrams(words):
	random.shuffle(words)
	print '\ngroup anagrams:'
	s = Sort()
	words = s.groupAnagrams(words)

def main():

	# words = list(alphabet)
	words = getWords()
	print 'Words: '+str(len(words))
	random.shuffle(words)

	# linkedList()

	# stack()

	#
	# Sorting
	#
	start = datetime.datetime.now()
	words = groupAnagrams(words)
	printTime(start)

	# start = datetime.datetime.now()
	# words = binaryTree(words)
	# printTime(start)

	# checkSort(words)

	# start = datetime.datetime.now()
	# quickSort(words)
	# printTime(start)

	# start = datetime.datetime.now()
	# mergeSort(words)
	# printTime(start)

	# start = datetime.datetime.now()
	# selectSort(words)
	# printTime(start)

	# start = datetime.datetime.now()
	# bubbleSort(words)
	# printTime(start)



if __name__ == '__main__':
	main()
