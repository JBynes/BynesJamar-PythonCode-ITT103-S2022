#Author: Jamar Bynes
#Date Created:April 8, 2022
#Course: ITT103
#Purpose: Calculating the commission rate of different sales persons by determining salesperson, class and salesperson number.

"""
JamEx Limited requires a program to calculate and print the commission received by a
salesperson. The program should process an undetermined number of salespersons and 
appropriately terminate by a predefined input. The commission rate is based on two factors, 
the amount of sales and the class to which a salesperson belongs. The input will be the 
salesperson number, sales amount and class. The commission rate will be based on the 
following criteria:

Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.

Class=2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent.

Class=3
The rate is 4.5 percent for all sales amount

Class=any other value
Output an appropriate error message.
"""
terminator = 'START'



while (terminator != 'END'):

 print ('Hello and welcome to the JamEx Limited Commission Calculator')
 
 #//User prompt messsage and accepting user input  
 print ('Please enter your sales person number')
 sales_person_number = input ()
 print ('Please enter your class')
 Class = int (input ())
 if Class > 3: 
   print("Please enter an appropriate class")
 if Class > 3:
   break
 print ('Please enter your sales amount')
 sales_amount = int (input ())

 
 
        
 #Class 1 calculations 
 if Class == 1:
        if sales_amount <= 1000:
          commission_rate = 0.06

        elif sales_amount > 1000 and sales_amount < 2000:
          commission_rate = 0.07

        elif sales_amount > 2000: 
          commission_rate = 0.1


 #Class 2 calculations
 elif Class == 2:
        if sales_amount <= 1000:
          commission_rate = 0.04

        else:  
         commission_rate = 0.06


 #Class 3 calculations
 elif Class == 3:
  commission_rate = 0.045

 
 

 #Calculating Commission
 commission = commission_rate * sales_amount        

  
 #Final ooutput 
 print("Your salesperson number is", sales_person_number) 
 print("And your class is", Class)
 print("Your commission rate is", commission_rate) 
 print("Your commission recieved is $", commission) 
 
 

    
 print ("Please write 'END' to exit the program or 'START' to continue")
 terminator = input()

 if terminator == 'END' or  terminator == 'End' or terminator == 'end':
   print ("The program has ended, Thank you for making it JamEx Limited. Goodbye.")
   
 if terminator == terminator == 'END' or  terminator == 'End' or terminator == 'end':
   break