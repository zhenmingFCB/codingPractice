class BigInteger(object):

	def __init__(self, sign, value):
		self.sign = sign
		self.value = value

	def add(self, num2):

		if self.sign=='-' and num2.sign=='-':
			sign = '-'
			return sign+BigInteger._addValue(self.value, num2.value)
		elif self.sign=='+' and num2.sign=='+':
			return BigInteger._addValue(self.value, num2.value)

		sign = ''
		if self.largerAbs(num2):
			value = BigInteger._subValue(self.value, num2.value)
			if self.sign=='-':
				sign = '-'
		else:
			value = BigInteger._subValue(num2.value, self.value)
			if self.sign=='+':
				sign = '-'

		return sign+value

	@staticmethod
	def _addValue(value1, value2):
		res = ''
		idx, carry = 0, 0
		while idx < max(len(value1), len(value2)):
			curr = carry
			if idx < len(value1):
				curr += int(value1[-idx-1])
			if idx < len(value2):
				curr += int(value2[-idx-1])
			carry = curr/10
			res = str(curr%10)+res
			idx += 1

		if carry==1:
			res = '1'+res

		return res

	@staticmethod
	def _subValue(value1, value2):
		res = ''
		idx, carry = 0, 0
		while idx < len(value2):
			if int(value1[-idx-1])-carry>int(value2[-idx-1]):
				curr = int(value1[-idx-1])-carry-int(value2[-idx-1])
				carry = 0
			else:
				curr = 10 + int(value1[-idx-1])-carry-int(value2[-idx-1])
				carry = 1
			res = str(curr%10)+res
			idx += 1

		while idx < len(value1):
			curr = int(value1[-idx-1]) - carry
			if curr<0:
				curr = curr+10
				carry = 1
			else:
				carry = 0
			res = str(curr)+res
			idx += 1

		return res


	def substract(self, num2):
		if self.sign == '-' and num2.sign=='+':
			return '-'+BigInteger._addValue(self.value, num2.value)
		elif self.sign == '+' and num2.sign=='-':
			return BigInteger._addValue(self.value, num2.value)

		sign = ''
		if self.largerAbs(num2):
			value = BigInteger._subValue(self.value, num2.value)
			if self.sign=='-':
				sign = '-'
		else:
			value = BigInteger._subValue(num2.value, self.value)
			if self.sign=='+':
				sign = '-'

		return sign+value


	def multiply(self, num2):
		if num1=='0' or num2=='0':
            return '0'
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j+1] += int(num1[i])*int(num2[j])
        
        carry = 0
        for i in reversed(range(len(res))):
            res[i] += carry
            carry = res[i]/10
            res[i] %= 10
        if res[0]>0:
            return ''.join(str(i) for i in res)
        else:
            return ''.join(str(i) for i in res[1:])

	def largerAbs(self, num2):
		value2 = num2.value
		if len(self.value)!=len(value2):
			return len(self.value)>len(value2)

		for i in range(len(self.value)):
			if int(self.value[i])!=int(value2[i]):
				return int(self.value[i])>int(value2[i])



if __name__ == '__main__':
	num1 = BigInteger('+', '1234')
	num2 = BigInteger('-', '9999')
	print num1.add(num2)
	print num1.substract(num2)
	print num2.substract(num1)
	print num2.add(num1)