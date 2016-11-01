def calculate(expression):
	"""
	basic calculator, support +-*/ ()
	support negtive numbers
	"""
	op_stack, num_stack = [], []
	sign = 1
	i=0
	while i<len(expression):
		c = expression[i]
		if c.isdigit():
			num = ''
			while i<len(expression) and expression[i].isdigit():
				num += expression[i]
				i += 1
			num_stack.append(int(num)*sign)
			sign = 1

		# continue if statement, not elif
		if c == '(':
			op_stack.append(c)
		elif c == ')':
			while op_stack[-1]!='(':
				if len(num_stack)<2 or len(op_stack)==0:
					raise InvalidExpression('InvalidExpression')
				num2, num1 = num_stack.pop(), num_stack.pop()
				op = op_stack.pop()
				num_stack.append(operate(op, num1, num2))
			op_stack.pop()
		elif c == '-' and i<len(expression)-1 and expression[i+1].isdigit():
			sign = -1
		elif c in '+-*/':
			while op_stack and precedent(op_stack[-1], c):
				if len(num_stack)<2 or len(op_stack)==0:
					raise InvalidExpression('InvalidExpression')
				num2, num1 = num_stack.pop(), num_stack.pop()
				op = op_stack.pop()
				num_stack.append(operate(op, num1, num2))
			op_stack.append(c)
		i+=1

	while op_stack:
		if len(num_stack)<2 or len(op_stack)==0:
					raise InvalidExpression('InvalidExpression')
		num2, num1 = num_stack.pop(), num_stack.pop()
		op = op_stack.pop()
		num_stack.append(operate(op, num1, num2))

	if len(num_stack)!=1 or len(op_stack)!=0:
		raise InvalidExpression('InvalidExpression')

	return num_stack[0]


def operate(op, num1, num2):
	if op=='+':
		return num1+num2
	elif op=='-':
		return num1-num2
	elif op=='*':
		return num1*num2
	else:
		return float(num1)/num2

def precedent(op1, op2):
	if op1=='(':
		return False
	elif op2 in '*/' and op1 in '+-':
		return False
	else:
		return True

class InvalidExpression(Exception):
	pass

print calculate("100 * ( -2 + 12 ) / 14")


