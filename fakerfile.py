from faker import Faker
from random import *  
fakegen=Faker()   
name=fakegen.name()  
print(name)   
first_name=fakegen.first_name()   
last_name=fakegen.last_name()   
print(first_name)   
print(last_name)   
date=fakegen.date()   
print(date)   
number=fakegen.random_number(5)   
print(number)   
email=fakegen.email()   
print(email)   
print(fakegen.city())   
print(fakegen.random_int(min=0, max=9999))   
print(fakegen.random_element(elements=('Project Manager', 'TeamLead', 'Software Engin eer'))) 

'''Oscar Bradley
Gary
Wallace
1992-11-23
41372
joshua78@lopez.net
Tiffanyshire
1988
TeamLead'''