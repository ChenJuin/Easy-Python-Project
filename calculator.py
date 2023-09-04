def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiple(x,y):
    return x*y 

def divide(x,y):
    return x*y

print("----------Python Calculator----------")
print("Please choose the method below:")
print("1. Add")
print("2. Substract")
print("3. Multiple")
print("4. divide")

choose = input("Please choose(1/2/3/4):")

#make the equation loop
while True:    
    #check input is 1/2/3/4
    if choose in ('1','2','3','4'):
        num1 = float(input("number 1:"))
        num2 = float(input("number 2:"))
        
        if choose == '1':
            print(num1,"+", num2, "=", add(num1,num2))
        
        elif choose == '2':
            print(num1,"-", num2, "=", substract(num1,num2))
        
        elif choose == '3':
            print(num1,"x", num2, "=", multiple(num1,num2))

        elif choose == '4':
            print(num1,"/", num2, "=", divide(num1,num2))
        
        #check want to try the calculation again or not
        next = input("Do you want to try other calculation?(y/n): ")
        if next == "y":
            continue
        elif next == "n":
            break
        #make sure won't have answer other than y and n to prevent keep looping
        else:
            print("Error, try again!")
            break
    else:
        print("Invalid input, try again!")
        break          
