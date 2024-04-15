#Bmi Calculator

import time

#Bmi function
def Bmi(kg , ft): 
     ft = ft * 0.3048   
     sum = kg/(ft**2)
     val = float(round(sum))
     print (f'\n{val}')

#Only stops when certain condition is met 
while True:
    try:
        #Input of Weight
        print("Input Weight in Kg : ")
        kg = float(input("\n"))

        #Input of Height
        print("Input Height in ft : ")
        ft = float(input("\n"))

        #Just some finishing touch
        print("Calculating Bmi: Please Wait : \n")
        time.sleep(2)

        #Output
        print("Your Bmi is : ") 
        Bmi(kg ,ft) #Function call 
        
        break # Condition is met . Program will Halt

    except ValueError:
        #Invalid input of string in integers and will loop back until is condition is met
        print("invalid Value")


