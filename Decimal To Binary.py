from stack import Stack

def convert_int_to_bin(dec_num):
  s = Stack()

  while dec_num != 0:

  	remainder = dec_num%2
  	s.push(remainder)
  	# dec_num = dec_num//2 also gives the integer result
  	dec_num //= 2
  	#dec_num = int(dec_num/2) 
  res = ''
  while not s.is_empty():
  	res += str(s.pop())

  return res

print('Binary value for 242 is: ' + convert_int_to_bin(242))