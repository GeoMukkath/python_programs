def push(num):
	for i in range(num):
		a = input("Enter the value you want to insert: ")
		stack.append(a)
	
def pop():
	stack.pop();	

def peek():
	if stack[0] != None:
		print(stack[-1])
	else:
		print("The stack is empty")

def show():
	print(stack)	

stack = [ ]
n = input("Enter the number of elements you want to insert : ")
push(int(n))
show()
peek()