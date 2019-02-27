'''
	This script is to illustrate decorators in python
	Mainly decorator is a rapper for functions
'''


# Part 1 (Simple decorator)
def decorator(fun):
	'''
		This is a decorator it takes function as argument 
		but no need to pass the function just use @decorator on top of function
	'''
	def run():
		return f'This is a {fun()}'
	return run

@decorator 		# We are calling decorator hear 
def function():
	'''This is function is using a decorator'''
	return "bead" 

print(function())
print(function.__name__)
'''
	This is going to return "run" as we use a decorator its __name__ changes
	to avoid this we use functools.wraps
'''
print()


# Part 2 (Avoiding change to __name__)
from functools import wraps
def decorator(fun):
	'''Hear we are using wraps to avoid changing __name__ for "fun"''' 
	@wraps(fun)
	def run():
		return f'This is a {fun()}'
	return run

@decorator
def function():
	'''This is function is using a decorator'''
	return "bead" 

print(function())
print(function.__name__)	
print()


# Part 3 (Taking more args)
def decorator(name):
	def sub_dec(itm):
		@wraps(itm)
		def run():
			return f'{name} of {itm()}'
		return run 
	return sub_dec

@decorator('SOMEONE ')
def function():
	'''This is function is using a decorator'''
	return "bead" 

print(function())
print()


# Part 4 (Nesterding)
@decorator('SOMEONE ')
@decorator('ME ')
def function():
	'''This is function is using a decorator'''
	return "bead" 

print(function())
