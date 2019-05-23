# Income Tax Calculator

"""
This program is all about Income Tax Calculation on the basis of Tax rate slab of India of Financial Year 2019-2020.
This whole program is user-friendly(it means it takes value from user).
For Tax rate slab you can refer my 'Tax Rate Slab of India.txt' file which i am droping it in my this repository.
This program gives the percentage of tax your annual income which you have to give. And also tells the amount that you have to give
"""

print("^"*23,'Welcome to Income Tax Calculator',"^"*23)

an_income=int(input("Enter your annual income"))     # Takes input from user in form of integer
if(an_income<=250000):        # If your income is more than Rs.250000                
    print("You don't have to pay any tax")           # Then you don't have to pay tax
elif(an_income>=250000 and an_income<=500000):       # If your income is more than 250000 and less than 500000
    print("You have to pay 5% + 4% cess\nYou have pay Rs.",an_income*9/100,"of your annual income")   # Then you have to pay 5% + 4% cess 
elif(an_income>=500000 and an_income<=1000000):      # If your income is more than 500000 and less than 1000000
    print("You have to pay 20% + 4% cess\nYou have pay Rs.",an_income*24/100,"of your annual income") # Then you have to pay 20% + 4% cess
elif(an_income>=1000000 and an_income<=5000000):     # If your income is more than 1000000 and less than 5000000
    print("You have to pay 30% + 4% cess\nYou have pay Rs.",an_income*34/100,"of your annual income") # Then you have to pay 30% + 4% cess
elif(an_income>=5000000 and an_income<=10000000):    # If your income is more than 5000000 and less than 10000000
    print("You have to pay 30% + 10% surcharge + 4% cess\nYou have pay Rs.",an_income*44/100,"of your annual income")#Then you have to pay 30% + 10% surcharge + 4% cess
elif(an_income>=10000000): # If your income is more than 10000000
    print("You have to pay 30% + 15% surcharge + 4% cess\nYou have pay Rs.",an_income*49/100,"of your annual income")#Then you have to pay 30% + 10% surcharge + 4% cess
  
# Code by Shubham Sharma , Freelancer Developer
