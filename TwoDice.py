from __future__ import division
import random

def two_dice(val):
	total = 0
	good = 0
	for x in xrange(1, 7):
		for y in xrange(1, 7):
			total += 1
			if x + y == val:
				good += 1
	return good / total

def two_dice_emp(val):
	total = 10000
	good = 0
	for _ in xrange(total):
		x = random.randint(1, 6)
		y = random.randint(1, 6)
		if x + y == val:
			good += 1
	return good / total

def main():
	print two_dice(11)
	print two_dice_emp(11)

if __name__ == '__main__':
	main()
