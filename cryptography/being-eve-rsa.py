import sys

def lcm(a, b, limit):
	for i in range(1, limit):
		n = a * i
		if(n % b == 0):
			return(a * i)
			


def getPrimes(n):
	primes = []
	for i in range(2, n):
		prime = True
		for j in range(2, i):
			for k in range(j, i):
				if(j * k > i):
					break
				if(j * k == i):
					prime = False
		if(prime == True):
			#print(i)
			primes.append(i)
	return(primes)


def getPossiblePQ(n_b, primes):
	PQ = []
	primeLen = len(primes)
	for prime0i in range(primeLen):
		prime0 = primes[prime0i]
		for prime1i in range(prime0i, primeLen):
			prime1 = primes[prime1i]
			if(prime0 * prime1 > n_b):
				break
			if(prime0 * prime1 == n_b):
				PQ.append([prime0, prime1])
	return PQ


def getD(e_b, lambda_nb):
	d = 1
	while(True):
		if(e_b * d % lambda_nb == 1):
			return d
		d += 1


def decode(d, n):
	message = list([1516, 3860, 2891, 570, 3483, 4022, 3437, 299, 570, 843, 3433, 5450, 653, 570, 3860, 482, 3860, 4851, 570, 2187, 4022, 3075, 653, 3860, 570, 3433, 1511, 2442, 4851, 570, 2187, 3860, 570, 3433, 1511, 4022, 3411, 5139, 1511, 3433, 4180, 570, 4169, 4022, 3411, 3075, 570, 3000, 2442, 2458, 4759, 570, 2863, 2458, 3455, 1106, 3860, 299, 570, 1511, 3433, 3433, 3000, 653, 3269, 4951, 4951, 2187, 2187, 2187, 299, 653, 1106, 1511, 4851, 3860, 3455, 3860, 3075, 299, 1106, 4022, 3194, 4951, 3437, 2458, 4022, 5139, 4951, 2442, 3075, 1106, 1511, 3455, 482, 3860, 653, 4951, 2875, 3668, 2875, 2875, 4951, 3668, 4063, 4951, 2442, 3455, 3075, 3433, 2442, 5139, 653, 5077, 2442, 3075, 3860, 5077, 3411, 653, 3860, 1165, 5077, 2713, 4022, 3075, 5077, 653, 3433, 2442, 2458, 3409, 3455, 4851, 5139, 5077, 2713, 2442, 3075, 5077, 3194, 4022, 3075, 3860, 5077, 3433, 1511, 2442, 4851, 5077, 3000, 3075, 3860, 482, 3455, 4022, 3411, 653, 2458, 2891, 5077, 3075, 3860, 3000, 4022, 3075, 3433, 3860, 1165, 299, 1511, 3433, 3194, 2458])
	output = ""
	for item in message:
		output += chr(item ** d % n)
	return output


def main():
	args = sys.argv
	if(len(args) > 1):
		e_b = int(args[1])
		n_b = int(args[2])
	else:
		e_b = 13
		n_b = 5561

	primes = getPrimes(n_b)
	pq = getPossiblePQ(n_b, primes)
	print("p, q : " + str(pq))
	p = pq[0][0]
	q = pq[0][1]
	
	lambdaN_b = lcm(p-1, q-1, 10000)
	print("lambda_nb = " + str(lambdaN_b))
	d = getD(e_b, lambdaN_b)
	
	print("d_b = " + str(d))
	print("Decoded message as follows: ")
	print(decode(d, n_b))

main()	

