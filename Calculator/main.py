from art import logo
print(logo)

#ADD FUNCTION
def add(n1,n2):
  return n1 + n2
#SUB FUNCTION
def sub(n1,n2):
  return n1-n2
#MULTIPLY FUNCTION
def mul(n1,n2):
  return n1 * n2
#DIVIDE FUNCTION
def div(n1,n2):
  return n1 / n2
operations = {
'+' : add,
'-' : sub,
'*' : mul,
'/' : div
}
def calculator():
  num1 = float(input("What is the 1st number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    user_input = input("Pick an operation: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[user_input]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {user_input} {num2} = {answer}")
    more_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or type 'r' to start a new calculation ")
    if more_operation == "y":
      num1 = answer
      should_continue = True
    elif more_operation == "r":
      should_continue = False
      calculator()
    else:
      should_continue = False
      

calculator()