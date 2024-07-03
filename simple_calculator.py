#Project of codsoft i.e simple caluclator
#below is the code for the calculator
# this calculator can perform basic arithmetic operations
# first operation is addition
def add(number1 , number2):
  return number1 + number2
#second operation defining is subtraction 
def sub(number1 , number2):
  return number1 - number2 
# defining third operation is multiplication 
def multiply(number1 , number2):
  return number1 * number2
#fourth operation is division 
def division(number1 , number2):
  return number1 /number2 
print("please select an operation\n")
print(" 1 - addition ")
print(" 2 - subtraction ")
print(" 3 - multiplication  ")
print(" 4 - division ")
# now taking input from the user for performing an operation
operation_number = int(input(" enter a number for performing an operation "))
operand_1 = int(input("enter the first number "))
operand_2 = int(input(" enter the second number "))
#defining the conditions 
if operation_number ==1:
    print("you selected addition operation")
    print(operand_1,"+", operand_2,"=", add(operand_1,operand_2))
elif operation_number == 2:
    print(" you selected subtraction operation")
    print(operand_1,"-",operand_2,"=", sub(operand_1,operand_2))
elif operation_number == 3:
    print("you selected multiplication operation")
    print(operand_1,"*",operand_2,"=",multiply(operand_1,operand_2))
elif operation_number == 4:
    print("you selected division operation")
    print(" hence it will give an output like first_number/second_number")
    print(operand_1,"/", operand_2,"=",division(operand_1,operand_2))
else:
    print("ivalid input by user")
