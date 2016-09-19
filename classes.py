#!/usr/bin/env python

# array
class Array():

	def __init__():
		self.name = None

# linked list
class LinkedList():

	def __init__(self, data=[], name=None):
		self.name = name
		self.head = None

		for i in data:
			self.appendToTail(i)

	def appendToTail(self, d):

		end = self.LinkedListNode(d)

		if not self.head:
			self.head = end
			return

		n = self.head

		while n.next:
			n = n.next

		n.next = end

	def array(self):

		if not self.head:
			print 'ERROR: List has no members.'
			return []

		n = self.head

		linked_list = [n.data]

		while n.next:
			n = n.next
			linked_list.append(n.data)

		return linked_list

	def nth(self, n):

		if not self.head:
			return

		count = 0
		node = self.head

		while count < n and node.next:
			node = node.next
			count+=1

		if count == n:
			return node.data


	# linked list node
	class LinkedListNode():

		def __init__(self, data=None):
			self.next = None
			self.data = data

		def node(d):
			self.data = d

# double-linked list
class DoubleLinkedList(LinkedList):

	def __init__(self):
		self.prev = None

# hash table
class HashTable():

	def __init__(self):
		self.name = None

# stack
class Stack():

	def __init__(self):
		self.top = None

	def pop(self):
		i = self.top
		self.top = i.next
		return i

	def push(self, i):
		new = self.StackItem(i)
		new.next = self.top
		self.top = new

	def peek(self):
		return self.top

	def isEmpty(self):
		if not self.top:
			return True
		return False

	def array(self):
		stack = []
		top = self.peek()
		while top:
			stack.append(top.data)
			top = top.next
		return stack

	def length(self):
		return(len(self.array()))

	class StackItem():

		def __init__(self, i):
			self.data = i
			self.next = None

class Queue():

	def __init__(self):
		self.first = None
		self.last = None

	def add(self, d):
		n = self.Item(d)
		if self.last:
			self.last.next = n
		self.last = n
		if not self.first:
			self.first = n

	def remove(self):
		f = self.first
		if not f.next:
			self.next = None
			self.last = None
		else:
			self.first = f.next
		return f

	def peek(self):
		return self.first

	def isEmpty(self):
		if not self.first:
			return True
		return False

	def array(self):
		n = self.peek()
		queue = [n.data]
		while n.next:
			n = n.next
			queue.append(n.data)
		return queue

	class Item():
		def __init__(self, d):
			# self.prev = None
			self.next = None
			self.data = d

class BinaryTree():

	def __init__(self, data=[]):
		self.head = None

		for d in data:
			self.add(d, self.head)

	class Node():

		def __init__(self, d):
			self.data = d
			self.left = None
			self.right = None

	def add(self, d, head):

		# if the tree is empty, add this node as the head
		if not head and not self.head:
			self.head = self.Node(d)
			return

		elif not head:
			head = self.head

		if d < head.data:
			# add to the left
			if not head.left:
				head.left = self.Node(d)
			else:
				self.add(d, head.left)

		else:
			# add to the rigjht
			if not head.right:
				head.right = self.Node(d)
			else:
				self.add(d, head.right)

	def array(self, head=False):

		if head == False:
			head = self.head

		if head == None:
			return []

		left = self.array(head.left)
		right = self.array(head.right)
		return left + [head.data] + right

class Sort():

	def __init__(self, data=[]):
		self.data = data

	def bubbleSort(self, data=[]):

		changes = True

		passes = 0
		while changes:

			changes = False

			n = 0
			while n < len(data)-1:
				cur = data[n]
				next = data[n+1]
				if cur > next:
					data[n] = next
					data[n+1] = cur
					changes = True

				n+=1

			passes += 1

		print 'Passes: '+str(passes)
		return data

	def selectSort(self, data=[]):

		n = 0
		while n < len(data):
			cur = data[n]

			mini = n
			minv = cur

			m = n
			while m < len(data):
				next = data[m]
				if next < minv:
					mini = m
					minv = next
				m+=1

			if mini != n:
				data[mini] = cur
				data[n] = minv

			n+=1

		return data


	def mergeSort(self, data=[]):

		def merge(a, b):

			new = []

			while a or b:

				if a and b:

					if a[0] < b[0]:
						new.append(a[0])
						del a[0]
					else:
						new.append(b[0])
						del b[0]

				elif a:
					new.append(a[0])
					del a[0]

				else:
					new.append(b[0])
					del b[0]

			return new

		l = len(data)

		if not l:
			return []

		elif l == 1:
			return data

		elif l == 2:
			if data[0] > data[1]:
				data = [data[1], data[0]]
			return data

		m = l/2

		a = data[0:m]
		b = data[m:]

		a = self.mergeSort(a)
		b = self.mergeSort(b)

		new = merge(a, b)

		return new

	def quickSort(self, data=[]):

		if not data:
			return data

		elif len(data) == 1:
			return data

		# select a pivot entry
		p = len(data)/2

		pivot = data[p]

		left = []
		right = [pivot]

		# put into buckets
		n = 0
		while n < len(data):

			if n == p:
				True
			elif data[n] < pivot:
				left.append(data[n])
			else:
				right.append(data[n])
			n+=1

		left =  self.quickSort(left)
		right = self.quickSort(right)

		new = []
		for i in left:
			new.append(i)
		for i in right:
			new.append(i)

		return left+right

	def groupAnagrams(self, data=[]):

		def alphabetize(word):
			return ''.join(sorted(word))


		anagrams = {}

		for d in data:
			a = alphabetize(d)
			if a in anagrams:
				anagrams[a].append(d)
			else:
				anagrams[a] = [d]

		last = None
		for w in sorted(anagrams, key=lambda x: [len(anagrams[x]), len(x)] , reverse=True):
			length = len(anagrams[w])
			words = sorted(anagrams[w])
			if length != last:
				print '\nWords: '+str(length)+':'
				last = length
			if length > 1:
				print words[0]+' ('+str(length)+'): '+str(words)



