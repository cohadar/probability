from __future__ import division
from scipy.special import binom
import random

def nysl(hits):
	return binom(60, 4 - hits) * binom(20, hits) / binom(80, 4)

def nysl_emp(hits):
	total = 10000
	good = 0
	numbers = range(1, 81)
	for _ in xrange(total):
		player = random.sample(numbers, 4)
		lottery = random.sample(numbers, 20)
		if len(set(player) & set(lottery)) == hits:
			good += 1
	return good / total

def main():
	for hits in xrange(0, 5):
		print nysl(hits)
		print nysl_emp(hits)
		print '=========='

if __name__ == '__main__':
	main()
