## Liam Boyle
## 17 Jan 2012
## my five minute python solution to the fizz buzz test
## this would have been done in 2 min but it took me a sec to remember
## python syntax, I've been spending too much time in C++ I guess

for i in range (1, 101):
	if i%3==0 and i%5==0:
		print "FizzBuzz"
	elif i%5==0:
		print "Buzz"
	elif i%3==0:
		print "Fizz"
	else:
		print i

