import random

def main():
	X = [0] * 7
	for _ in xrange(1200):
		X[random.randint(1, 6)] += 1
	print X

if __name__ == '__main__':
	main()
