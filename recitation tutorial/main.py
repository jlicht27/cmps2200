def sum_of_squares(a):
	result = 0
	for i in a:
		result += i**2
	return int(result)

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([0,2,4,6,8,10]) == 220

print(test_one())

print(test_two())
