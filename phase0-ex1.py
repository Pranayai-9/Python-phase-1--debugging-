#Non-function
num1 = int(input())
num2 = int(input())
num3 = int(input())
average = (num1+num2+num3)/3
print(average) 


#Function
def avg():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    average = (num1+num2+num3)/3
    return average 

result = avg() 
print(result) 