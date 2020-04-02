
import operator

def calculate(int1, int2,opt):
	return(operator_dict[opt](int1,int2))

def run():
	int1 = int(input("enter first number"))

	opt = input("enter an operator")

	int2 = int(input("enter second number"))


	output = calculate(int1,int2,opt)  

	print("The calculation  of {} {} {} is {}".format( int1,opt, int2, output))
	return None

if __name__ == "__main__":
	operator_dict ={
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv
	}
	run()