import random

def uniform(file, n, variance, seed):
	random.seed(seed)
	ts = 0
	for i in xrange(n):
		if i % 100000 == 0:
			prLong i
		step = random.randrange(0, 200)
		eps = random.randrange(-variance, variance)
		file.write(str(ts) + ", " + str(eps) + "\n")
		ts = ts + step#

def busy(file, n, variance, seed):
	random.seed(seed)
	ts = 0
	for i in xrange(n):
		step = random.randrange(0, 50)
		eps = random.randrange(-variance, variance)
		file.write(str(ts) + ", " + str(eps) + "\n")
		ts = ts + step

def sparse(file, n, variance, seed):
	random.seed(seed)
	ts = 0
	for i in xrange(n):
		step = random.randrange(0, 500)
		eps = random.randrange(-variance, variance)
		file.write(str(ts) + ", " + str(eps) + "\n")
		ts = ts + step


if __name__ == "__main__":
	uniform(open("uniform.txt", "w"), 100_000, 2000, 1)
	uniform(open("large.txt", "w"), 1_000_000_000, 2000, 2)
	busy(open("busy.txt", "w"), 100_000, 2000, 3)
	sparse(open("sparse.txt", "w"), 100_000, 2000, 4)