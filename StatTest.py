from __future__ import division
import random

def sum2(val):
	total = 0
	good = 0
	for x in xrange(1, 7):
		for y in xrange(1, 7):
			total += 1
			if x + y == val:
				good += 1
	return (good, total)

def main():
	good, total = sum2(11)
	print good / total

if __name__ == '__main__':
	main()
