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
    
    # elif choice == '2':
    #     y = input("enter the item to be deleted: ")
    #     shopping_list.remove(y)
    else:
         print("Invalid")
    

        
