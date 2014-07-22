#!/usr/bin/env python

# This was a puzzle I received in a coding challenge. One of those ones they give you before an
# interview to see if you know foo from bar. I strongly dislike these, especially when they're 
# timed, but this is the one I did last and therefore ran out of time on. I was displeased, so
# here's the solution.

from random import choice

def string_distance(S):
	""" A function transforming a string containing only characters in [A,B,C], in line with a set of
	rules:

	Rule 1: AB -> AA
	Rule 2: BA -> AA
	Rule 3: CB -> CC
	Rule 4: BC -> CC
	Rule 5: AA -> A
	Rule 6: CC -> C

	A rule is considered useful if it can be applied to the string. The function should select
	a useful rule at random, apply it, and continue doing so until no rule can be applied to
	the string. It should then return the string."""

	test = S # don't modify inputs
	useful = []
	
	# first-class functions, you so cool.
	def first(): return test.replace("AB","AA",1) # 1 means only replace 1 instance, the first
	def second(): return test.replace("BA","AA",1)
	def third(): return test.replace("CB","CC",1)
	def fourth(): return test.replace("BC","CC",1)
	def fifth(): return test.replace("AA","A",1)
	def sixth(): return test.replace("CC","C",1)

	while True:
		if "AB" in test:
			useful.append(first)
		if "BA" in test:
			useful.append(second)
		if "CB" in test:
			useful.append(third)
		if "BC" in test:
			useful.append(fourth)
		if "AA" in test:
			useful.append(fifth)
		if "CC" in test:
			useful.append(sixth)

	
		if useful == []:
			print test
			return True

		test = choice(useful)()
		useful = []

if __name__=='__main__':
	string_distance('AABBCCBC')
	string_distance('AC')
	string_distance('BCCBACB')
