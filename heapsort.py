#!/usr/bin/env python
from graphdis import graphdis
from slideshow import App

class heap:
	'''
	Class for creating and manipulating heap objects
	
	Contains methods to heapify a subtree, build a heap and perform heapsort
	'''
	
	def __init__(self, A, heapsize=-1, isheap=0):
		'''Initializes the graphdis object with the list
			Length(A) = heapsize if heapsize is not provided
			Heap is not built if explicitly specified with isheap = 1
		'''
	
		if heapsize == -1:
			self.heapsize = len(A)
		else:
			self.heapsize = heapsize
		
		self._list = [-1] + A[:]
		
		self.glist = graphdis(self._list, 'Input List')
		self.glist.initGviz(self.heapsize)
		
		if isheap == 0:
			self.buildheap()
			
		
	def heapify(self, i):
		'''
		Heapifies the subtree rooted at index i, does nothing if the root is a leaf.
		
		If the lchild and rchild are heaps then tree at i becomes a heap after heapify
		The maximum of the root, lchild, rchild is found and replaced with the root,
		heapify is called at index where the root goes to, if root is not the maximum.
		'''
		
		a = self.glist.list
		heapsize = self.heapsize
		lchild = 2 * i
		rchild = 2 * i + 1
		
		m = i
		
		if (lchild <= heapsize):
			if a[lchild] > a[i]:
				m = lchild
		
		if (rchild <= heapsize):
			if a[rchild] > a[m]:
				m = rchild
		
		if (m != i):
			
			self.glist.swap(i, m) # swap updates the glist.gviz object and saves frames
			self.heapify(m)
	
	def buildheap(self):
		'''
		Makes a heap out of the internal list
		
		Sub-trees are made into heaps in a bottom up fashion starting with the deepest
		level(leaves) to the root
		Loop Invariant: All subtrees rooted at indices heapsize to heapsize-i) are heaps 
		after the ith iteration. Base Case: i = heapsize, 
		'''
		
		a = self._list
		heapsize = self.heapsize
		heapify = self.heapify
#		print 'buildheap:  '
		for i in xrange(heapsize, 0, -1):
#			print i, a
			self.glist.state = 'Building heap -> heapify({})'.format(i)
			heapify(i)

		
	def heapsort(self):
		'''Sorts the heap inplace'''
		
		_list_copy = self.glist.list[:]
		_hs_copy = self.heapsize
		a = self._list
		heapify = self.heapify
		
		for i in xrange(1, self.heapsize):
			self.glist.state = 'heapsort'
			self.glist.swap(1, self.heapsize)
				
			self.heapsize -= 1
			
			self.glist.state = 'heapsort -> heapify(1)'
			heapify(1)
			
		sorted_array = a[1:]
		self.glist.list = _list_copy
		self.heapsize = _hs_copy
		return sorted_array
		

if __name__ == '__main__' :
	#a = map(int, raw_input('Space separated list of numbers: ').split())
	#a = [1,2,3,4,5,6,7,8,9,10]
	import random
	import os
	
	n = random.randrange(30) + 1
	a = random.sample(range(100), n)
	print a
	
	heapa = heap(a)
	print heapa.heapsort()
	
	cwd = os.getcwd()
#	print cwd + '/frames/0.png'
	slideshow = App((cwd + '/frames-test/{}.png'.format(i) for i in xrange(heapa.glist.framenum)), 200, 200, 500)
	
	slideshow.show_slides()
	slideshow.run()
	
