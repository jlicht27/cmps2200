from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == #TODO
	assert work_calc(20, 3, 2) == #TODO
	assert work_calc(30, 4, 2) == #TODO

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
	assert work_calc(30, 3, 2, lambda n: n) == #TODO
