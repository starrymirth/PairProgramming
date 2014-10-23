def fact1(n): #iterative
	answer = 1
	if n < 0:
		raise Exception("Cannot take factorial of a negative")
	else:
		for i in range(1,n+1):
			answer = answer*i
	return answer


def fact2(n): #recursive
	if n < 0:
		raise Exception("Cannot take factorial of a negative")
	if n == 0:
		return 1
	else:
		return n*fact2(n-1)		
	
#tests!
print fact1(0)
print fact1(1)
print fact1(2)
print fact1(3)
print fact1(4)
print fact1(5)
print fact2(0)
print fact2(1)
print fact2(2)
print fact2(3)
print fact2(4)
print fact2(5)

#these will throw exceptions
print fact2(-1)
print fact1(-1)
