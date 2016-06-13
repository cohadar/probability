import random

def main():
	a = 100000
	b = 100000
	p = 1.0 / 6
	wa = 10
	wb = 50
	for x in xrange(1000000):
		dice = random.randint(1, 6)
		if dice == 4:
			a += wb
			b -= wb
		else:
			a -= wa
			b += wa
	print a - b

if __name__ == '__main__':
	main()