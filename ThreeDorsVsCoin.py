from __future__ import division
import random

def three_door():
	first_toss = random.randint(0, 1)
	if first_toss == 0:
		second_toss = random.randint(0, 1)
		return second_toss
	else:
		second_toss = random.randint(0, 1)
		if second_toss == 0:
			return 2
		else:
			return three_door() # retry

def calc(code):
	total = 100000
	good = 0
	for _ in xrange(total):
		if code == three_door():
			good += 1
	return good / total	

def main():
	print calc(0)
	print calc(1)
	print calc(2)

if __name__ == '__main__':
	main()