#!/usr/bin/env python
import os
from subprocess import call

class Graph():
	'''Class to create the graph file'''
	
	kws = {}
	
	def __init__(self, filename, directory, format):
		self.filename = filename
		self.directory = directory
		
		call(['mkdir', directory])
		
		self.format = format
		self.body = {}
		self.body[0] = ''
		
	def node(self, id, **kvp):
		'''Writes a node into the dot file'''
		attr = ''
		for key in kvp.keys():
			attr += ' {0}={1}'.format(key, kvp[key])
		#print attr
		self.body[int(id)] = '\t{0} [{1}]'.format(id, attr)
		pass
	
	def attr(self, object, **kwargs):
		'''Writes the attributes at the beginning of the graph'''
		for key in kwargs.keys():
			object += '[{}="{}"]'.format(key, kwargs[key])
		
		self.body[0] = '\t{}'.format(object)
		pass
	
	def edge(self, id1, id2):
		'''Writes an edge into the dot file'''
		n = len(self.body.keys())
		self.body[n] = '\t{} -- {}'.format(id1, id2)
		
	
	def render(self, outfile, directory):
		'''Creates and renders the dot file into a image file with given format'''
		cwd = os.getcwd()
		filename = self.directory + '/' + self.filename
		outfilename = self.directory + '/' + outfile + '.{}'.format(self.format)
		
		source = 'graph G ' + '{\n'
		
		n = len(self.body.keys())
		
		for linenum in xrange(n):
			source += self.body[linenum] + '\n'
		source += '}'
		
		with open(filename, 'w') as f:
			f.write(source)
		
		call(['dot', '-T{}'.format(self.format), filename, '-o', outfilename])
		
if __name__ == '__main__':
	g = Graph('dotfile', 'frames-test', 'png')
	g.node('1', label='HI')
	g.node('2', label='BYE')
	g.edge('1', '2')
	g.node('1', label='HELLO', color='red')
	g.render('1', directory='frames-test')
