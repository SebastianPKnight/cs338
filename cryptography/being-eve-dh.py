import sys

def getX(g, p, A):
	for X in range(1, p):
		if(A == (g ** X % p)):
			return(X)


def main():
	args = sys.argv
	if(len(args) > 1):
		g = args[1]
		p = args[2]
		A = args[3]
		B = args[4]
	else:
		g = 11
		p = 59
		A = 57
		B = 44

	X = getX(g, p, A)
	print("X = " + str(X))
	print("shared secret: " + str(B ** X % p))


main()
