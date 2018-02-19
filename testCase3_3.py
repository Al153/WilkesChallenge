import hashlib


def doTest():
	sha = hashlib.sha1()
	while True:
		try:
			line = raw_input("")
			if line == "":
				break
			sha.update(line)
		except:
			break
	print(sha.hexdigest())


if __name__ == "__main__":
	doTest()