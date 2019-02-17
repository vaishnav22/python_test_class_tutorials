#    1.....def fun1(x,y,z):
	##if x in range(y,z+1):
		#print('{} is in range from {} to {}'.format(x,y,z))
	#else:
		#print('{} not in range'.format(x))

#fun1(2,1,10)

#_____________________#####################_____________________________________________

#    2.....calculate number of upper and lower words in the sentance

#def check_case(s):
	#d = {"upper":0, "lower":0}
	#for c in s:
		#if c.isupper():
			#d["upper"]+=1
		#elif c.islower():
		#	#d["lower"]+=1
		#else:
			#pass
	#print('the length of the sentance is {}'.format(len(s)))
	#print('the number of upper case is: ',d["upper"])
	#print('the number of lower case is: ',d["lower"])

#x = 'the aname is VAISHNAV'
#check_case(x)


########_____________________________%%%%%%%%%%%%%%%%%%%%%%%_______________________________


#python homework

#class line:
	#def __init__(self,cord1,cord2):
	#	#self.cord1 = cord1
		#self.cord2 = cord2

	#def distance(self):


####_________________________________######################_________________________________


#BANK COUNT 

#class bank:

	#def __init__(self,owner,balance=0):
		#self.owner = owner
		#self.balance = balance
#

	#def __str__(self):
		#return f"Account owner:  {self.owner}\nAccount balance : {self.balance}"

	#def deposit(self,wd,amt):
		#self.balance += amt
		#print('deposit accepeted')

	#def withdraw(self,wd_amt):
        #if self.balance >= wd_amt:
           # self.balance -= wd_amt
           # print('Withdrawal Accepted')
       # else:
            #print('Funds Unavailable!')

#acc1 = bank('VAISHNAV',300)
#print(acc1

######_____________________________________________############___________________

 


def display():
    print(shopping_list)




shopping_list = []
custumer_name = input("enter the name: ")
print("welcome to the nature basket!!" + custumer_name)
while 1:
	print("1.to add a new element to the shopping list")
	print("2.delete the item form the list")
	print("3.remove the last element form the list")
	print("4.exit")
	choice = input("enter the choice")

	if choice == '1':
		x =input("enter the element:  ")
		shopping_list.append(x)
		print(shopping_list)
    
    # elif choice == '2':
    #     y = input("enter the item to be deleted: ")
    #     shopping_list.remove(y)

   
    

        

	










