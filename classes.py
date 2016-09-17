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
		l = len(data)

		if not l:
			return []

		elif l == 1:
			return data

		elif l == 2:
			if data[0] > data[1]:
				return [data[1], data[0]]
			return data

		else:
			m = l/2

			a = mergeSort(data[0:m])
			b = mergeSort(data[m:])

		def merge(a, b):

			new = []

			ai = 0
			bi = 0

			while ai <= len(a) and bi <= len(b):

				if a[ai] < b[bi]:
					new.append(a[ai])
					ai+=1
				else:
					new.append(b[bi])
					bi+=1


		# merge





