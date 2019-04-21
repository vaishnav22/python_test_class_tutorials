#def makes_twenty(n1,n2):
    #return (n1+n2)==20 or n1==20 or n2==20

#makes_twenty(20,10)


############___________________________________________________________________##################################################



class Dog():
	def __init__(self,breed):
		self.breed = breed

my_dog = Dog(breed='Lab')
v= my_dog.breed
print(v)


#################________________________________________________________##################################___________________________

#class Name():
	#def __init__(self,age,sex,birth):
		#self.age = age
		#self.sex = sex
		#self.birth = birth
#
#person = Name(age='52',sex='Male',birth='january')
#v = person.age + person.sex + person.birth
#print(v)

#######################################_________________________________________________________________################################

#class Name():

	#person_family = "sathya prasad family"
	#def __init__(self,age,sex,birth):
		#self.age = age
		#self.sex = sex
		#self.birth = birth

#person = Name(age='52',sex='Male',birth='january')
#x = person.person_family
#print(x)
#v = person.age + person.sex + person.birth
#print(v)

##########____________________________________________________#___________________________________________##########################

#INHERITANCE 


#class Animal():
	#def __int__(self):
		#print('Animal created')

	#def who_i_am(self):
		#print('i am animal')

	#def eat(self):
		#print('i am eating')

#class dog(Animal):
	#def __init__(self):
		#Animal.__init__(self)
		#print('Dog created')

#my_animal = dog()
#my_animal.who_i_am


###########_____________________________________________________##########################_________________________________________

#class dog():
	#def __init__(self,name):
		#self.name = name

	#def speak(self):
		#return self.name + " says woof"

#sufi = dog("sufi")
#print(sufi.speak())

#####________________________________________________________________________________________#############_____________________________


#class book():
	#def __init__(self,name,auther,pages):                                                ####### string function in a class when asked by the compiler
		#self.name = name
		#self.auther= auther
		#self.pages = pages

	#def __str__(self):
		#return f"{self.name} by {self.auther} which is of {self.pages} pages"


#b = book('everything is OSM','vaishnav','546')
#print(b)

###########____________________________________________________________________######################____________________________________


#class book():
	#def __init__(self,name,auther,pages):                                                ####### string function in a class when asked by the compiler
	#	self.name = name
	#	self.auther= auther
	#	self.pages = pages

	#def __str__(self):
	#	return f"{self.name} by {self.auther} which is of {self.pages} pages"

	#def __len__(self):															## this is the functipn that is usef to use the predefined function when 
		#return self.pages
		
#b = book('everything is OSM','vaishnav',546)
#print(b)
#len(b)


######________________________________________________________$$$$$$$$$$$$$$$$$$$$$$$

# Code starts here
alist = [i for i in range(1,51)]
# initialize both list
blist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def numb(n):
    
final = [i for i in alist if i not in blist]
print(final)

%%%%%%%%%%%%________________________________________________________________________

# Code starts

# class for Circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        area = 3.14*(self.radius**2)
        return area

    
    def perimeter(self):
        perimeter = 2*3.14*self.radius
        return perimeter
    

circle = Circle(3)
circle_area = circle.area()
print(circle_area)

circle_perimeter = circle.perimeter()
print(circle_perimeter)

box = Circle(4)
print(circle.perimeter)
print(box.perimeter)

######_____________________####################################________________

