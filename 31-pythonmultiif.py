#this program indicates to write multople if statement
# first execise 
'''
if the person age is below 12 then the guy ticket is 150 rs 
if the person age is between 12 and 18 then the guy need to pay rs 250
if the person age is above 18 ,then he needs to pay 500 

'''

# second execise 
'''
if the person age is below 12 then the guy ticket is 150 rs 
    we need to ask the req any photo  +50
if the person age is between 12 and 18 then the guy need to pay rs 250
    we need to ask the req any photo   +50
if the person age is above 18 ,then he needs to pay 500 
     we need to ask the req any photo   +50

'''

print("this program is for the to check the if else ")
man_age=int(input("enter the age of a person:"))
if(man_age<12):
    print(" ticket prize is 150 ")
elif(man_age<18):
    print(" ticket prize is 250 ")
else:
    print(" ticket prize is 500 ")