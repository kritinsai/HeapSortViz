#!/usr/bin/env python

from graphviz import Graph

#GRAPH DISplay
class graphdis(Graph):
	'''
	Class which helps in the display of the heap objects
	
	Instances of this class get data from heap class as a list, construct the tree,  provide
	methods to modify the tree. The advantage of using a separate class for this is a reduce in
	the amount of modification to the Algorithm class.
	'''
	
	def __init__(self, List, state):
		'''
		Creates a internal reference to the List provided
		State represents the current state of the algorithms -> buildheap, heapsort, heapify
		framenum is the number of frames created.
		'''
		
		self.list = List
		self.gviz = None
		self.state = state
		self.framenum = 0
	
	def initGviz(self, hs):
		'''
		Called when there is a need to create gviz from scratch.
		hs = heapsize
		
		ids for the nodes in the graph are 1..hs, the values in the list
		are shown in the labels.
		'''
		# Graphviz graph object
		a = self.list
		
		self.gviz = Graph(filename='heap.gv', directory='frames-test', format='png')
		
		for i in xrange(1, hs+1):
			self.gviz.node(str(i), label = str(a[i]))

		for i in xrange(1, hs/2 + 1): # parents have indices from 1 to hs/2
			lc = 2 * i
			rc = 2 * i + 1
			if lc <= hs:
				self.gviz.edge(str(i), str(lc))
			if rc <= hs:
				self.gviz.edge(str(i), str(rc))
		
		self.saveFrame('Input List')

	def saveFrame(self, state):
		'''
		Saves the current state of the graph in a file in ./frames
		
		state is displayed as the label of the graph.
		filename=framenum.png
		
		'''
		
		self.gviz.attr('graph', label=state)
		self.gviz.render(str(self.framenum), directory='frames')
		self.framenum += 1
	
	def swap(self, i , j):
		'''
		Swaps the elements at i and j in the list, modifies gviz and saves frames
		
		A function for modifying the node attributes is not used as there are variations depending
		on the current state.
		'''
		if self.state == 'heapsort':
			self.gviz.node(str(i), label=str(self.list[i]), color='magenta')
			self.gviz.node(str(j), label=str(self.list[j]), color='magenta')
			self.saveFrame('heapsort')
			
			self.list[i], self.list[j] = self.list[j], self.list[i]
			
			self.gviz.node(str(i), label=str(self.list[i]), color='magenta')
			# Red color is used for nodes not in the heap
			self.gviz.node(str(j), label=str(self.list[j]), color='red') 
			self.saveFrame('heapsort -> Removing root from heap')
			
			self.gviz.node(str(i), label=str(self.list[i]), color='black')
			self.saveFrame('heapsort')
			
			
		else:
			self.gviz.node(str(i), label=str(self.list[i]), color='magenta')
			self.gviz.node(str(j), label=str(self.list[j]), color='magenta')
			self.saveFrame(self.state)
			
			self.list[i], self.list[j] = self.list[j], self.list[i]
			
			self.gviz.node(str(i), label=str(self.list[i]), color='magenta')
			self.gviz.node(str(j), label=str(self.list[j]), color='magenta')
			self.saveFrame(self.state)
			
			self.gviz.node(str(i), label=str(self.list[i]), color='black')
			self.gviz.node(str(j), label=str(self.list[j]), color='black')
			self.saveFrame(self.state)
			
		
