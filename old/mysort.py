#!/usr/bin/python

from sys import argv
from math import floor
import random
import time
from array import array

script, filename = argv

print "File: %s" % filename

def report(text):
	print time.strftime("%Y-%m-%d %H:%M:%S"), text % filename

report("opening %s")
lines = open(filename).read().splitlines()

report("shuffling %s")
random.shuffle(lines)

report("counting lines of %s")
#numlines = len(lines)
#print numlines, "lines"

count = 0
#items = array('c')
for line in lines:
	#print count, line
	#items.append(line)
	count += 1

#count = 100000
print count, "items"
report("finished with %s")

def bubblesort(lines):
	done = passes = 0

	while not done:
		passes+=1
		print "\npass #%d" % passes
		swaps=0 
		
		#print lines[0]
		power=1
		
		for l in range(0,count):
			reports = [0, power, count-1]
			if l in reports:
				print l, lines[l]
				if l == power:
					power*=2
			#print lines[l]
			current = lines[l]
			previous = lines[l-1]
			if (l > 0 and lines[l] < lines[l-1]):
				swaps+=1

				lines[l] = previous
				lines[l-1] = current
		if swaps == 0:
			done = 1
		else:
			print "\n%d swaps completed" % swaps

	print "Total passes: %d" % passes

def selectsort(lines):
	power=1
	n=0
	for l in range(0,count):
		min = l
		# find the minimum value in the rest of the list and make next

		for i in range (l,count):
			n+=1
			# if this is smaller than min, make it min
			if lines[i] < lines[min]:
				min = i
		minvalue = lines[min]
		lines[min] = lines[l]
		lines[l] = minvalue
		if l in [ 0, power, count-1]:
			print l, minvalue, n
			power*=2

def insertsort(lines):

	n=0
	sorted = [ None ]
	for l in range(0,count):
		power=1
		print "Pass #%d" % l
		this = lines[l]
		done = 0
		if l == 0:
			sorted = [ this ]
			n+=1
		else:
			for i in range(0,l-1):
				n+=1
				if sorted[i] > this:
					sorted.insert(i,this)
					done = 1
				if i in [ 0, power, count-1]:
					print l, i, sorted[i], n
					power*=2
				if done:
					break
			if not done:
				sorted.append(this)

def run_mergesort(lines):
	unsorted = []
	print count, "items to be sorted"
	for i in range(0,count):
		unsorted.append( lines[i] )
		#print lines[i]
	sorted = mergesort(unsorted, 0)
	#for j in range(0, len(sorted)):
		#print sorted[j]
	print count, "items sorted."
	print sortcount, "total mergesorts"
	
def mergesort(a, depth):
	depth+=1
	global sortcount
	sortcount+=1
	#print "mergesort", depth, sortcount, len(a), a
	# if we only have one or zero items, we are done splitting and sorting, just return
	if len(a) < 2:
		return(a)
	# if we have two items, we sort (swap) them if necessary and return
	elif len(a) == 2:
		if a[0] > a[1]:
			asorted = [ a[1], a[0] ]
			return(asorted)
		else:
			return(a)
	# if we have more than two items, we need to split them off into two other mergesorts
	else:
		# first half of a
		b = a[:len(a)/2]
		# second half of a
		c = a[len(a)/2:]
		bsorted = mergesort(b, depth)
		csorted = mergesort(c, depth)
		#print "merge", depth, sortcount, len(bsorted) + len(csorted), bsorted, csorted
		sorted = []
		# merge these two sorted lists back together
		i = j = n = 0

		while len(bsorted) or len(csorted):
			blen = len(bsorted)
			clen = len(csorted)
			if blen and clen and bsorted[0] and csorted[0]:
				if bsorted[0] < csorted[0]:
					sorted.append(bsorted.pop(0))
				else:
					sorted.append(csorted.pop(0))
			elif blen:
				sorted.append(bsorted.pop(0))
			else:
				sorted.append(csorted.pop(0))
			n+=1
		return(sorted)


def quicksort(a, depth):
	#print "quicksort", depth, a
	if len(a) < 2:
		return(a)
	# select an element to be the pivot element
	p = random.randint(0,len(a)-1)
	pivot = a.pop(p)
	#print "pivot:", pivot
	# create empty lists for less and greater
	less = []
	greater = []
	for i in a:
		if i <= pivot:
			less.append(i)
		else:
			greater.append(i)
	#print "less, greater:", len(less), len(greater)
	lsorted = quicksort(less, depth+1)
	gsorted = quicksort(greater, depth+1)
	sorted = []
	for l in lsorted:
		sorted.append(l)
	sorted.append(pivot)
	for g in gsorted:
		sorted.append(g)
	#print "sorted:", sorted
	#if depth == 0:
		#print "Done:"
		#print "less:", less
		#print "greater:", greater
	return(sorted)

def heapsort(a):
	n = len(a)

	#print a

	# heapify a
	for start in range((n-2)/2, -1, -1):
		siftdown(a, start, n - 1)

	for end in range(n-1, 0, -1):
		a[end], a[0] = a[0], a[end]
		siftdown(a, 0, end - 1)

	#print a

def siftdown(a, start, end):
	root = start
	while True:
		child = root * 2 + 1
		if child > end: break
		if child + 1 <= end and a[child] < a[child + 1]:
			child += 1
		if a[root] < a[child]:
			a[root], a[child] = a[child], a[root]
			root = child
		else:
			break


sortcount = 0

def stringperms(s):


	for i in range(0,len(s)):
		l = s
		sub = l.del(i)
		# get iterations of s without i
		perms = stringperms(sub)
		for j in range(1,len(s)):
			print s[j]


# report("starting bubblesort with %s")
# bubblesort(lines)

# report("starting selectsort with %s")
# selectsort(lines)

# report("starting insertsort with %s")
# insertsort(lines)

# report("starting mergesort with %s")
# run_mergesort(lines)

# report("starting quicksort with %s")
# a = lines[:count]
# sorted = quicksort(a, 0)
# power=1
# for i in range(0,len(sorted)-1):
# 	if i in [ 0, power, len(sorted)-1]:
# 		print i, sorted[i]
# 		power*=2


# report("starting heapsort with %s")
# heapsort(lines[:count])

chars = { 'a', 'b', 'c', 'd'}
stringperms(chars)
#print items






























