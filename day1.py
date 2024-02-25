
#print string in one line
# for x in "Banana":

#     if x == "n":
#         continue
#     print(x)

# for x in range(10,101,2 ):

#     print(x)

#Nested loop

# data1=["red","big","tasty"]
# data2=["red","big","tasty"]
# i=0
# j=0

# while i <len(data1) :
#     i=0
  
#     while j <len(data2):
    
#         print(data1[i], data2[j])
#         j=j+1
#     i=i+1
  
 



#print in one line for loop data
# my_list = ['bobby', 'hadz', 'com']

# result = '-'.join(my_list)
# print(result)my_list = ['bobby', 'hadz', 'com']


# result = '-'.join(my_list)
# print(result)

# my_list = ['bobby', 'hadz', 'com']

# result = ' '.join(my_list)
# print(result)
    


# x = ["red","big","tasty"]
# y = ["red","big","tasty"]
# i = 0

# while i < len(x) :
#   j = 0
#   while j < len(y) :
#     print(x[i] , y[j])
#     j = j + 1
#   i = i + 1


#Function
# def add():
#   a=9+6
#   print(a)

# def sub():
#   a=9-6
#   print(a)

# def multification():
#   a=9*6
#   print(a)

# def devistion():
#   a=9/6
#   print(a)


# def devistion():
#   a=9/6
#   print(a)



# add()
# sub()
# multification()
# devistion()
  
# def my_function(fname,lname):
#   print(fname  ,  lname)

# my_function("Email1","Id")
# my_function("Email2","Id")
# my_function("Email3","Id")
# my_function("Email4","Id")
# my_function("Email5","Id")


#When we don't know how much value we
# def munni(*kids):
#   print("The child is " + kids[2])
# munni("Email","ID","linus")

# def my_function(x,y,z):
#   print("The value is " + y)

# my_function(
#   x='khadija',
#   y='Munni',
#   z='kk'
  
#   )

# def my_function(**kid):
#   print("The value is " + kid['x'] , kid['y'] )

# my_function(
#   x='khadija',
#   y='Munni',
#   z='kk'
  
#   )

# a=int(input())

# if a%2 !=0 :
#   print("Weird")

# elif a%2 == 0 and 1<a<6:
#   print(" Not Weird")

# elif a%2 == 0 and 5<a<21:
#   print(" Weird")

# else:
#   print("Not Weird")


# a=int(input())
# limit=a+1
# for i in range(1,limit):

#     print(i , end='')

# def myfunction(food):
#     for x in food:
#         print(x)

# fruits=("apple","Banna")
# myfunction(fruits)



# def function(food):
#     food[1]="Orange"
#     return fruits


# fruits=["apple","Banna"]
# y=function(fruits)

# print(y)


# def munni(x,y):
#     c=x+y
#     d=c*5*6
#     return d
# print(munni(2,4))


# li=[22,3,4,4]

# def function(number):
#     a=0
#     for i in number:
#         a=a+i
#         return a

# print(function(li))

# dic= {
#     11:"khadija",
#     12:"kK",
#     "m":"Ayisha",
#     "clr":["black","pink"]

# }
# dic["clr"] [1] ='green'
# print(dic ["clr"] )

#type Convertion


# thisdic = dict(name ="khadija" , age=36)

# print(thisdic["name"])



#OOP constractor
# class Person:
#   def __init__(self, name, age, address):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# p2 = Person("kk", 36)


# print(p2.name)
# print(p2.age)


# print(p1.name)
# print(p1.age)


#Object

# class Nijeria():
#   x="Black"
#   y="tall"

# osman=Nijeria()
# print(osman.x,osman.y)

# Nijeria.x="pink"
# print(osman.x)

#Inheritence

# class Person:
#   def __init__(self, fname, lname):#parent
#     self.firstname = fname
#     self.lastname = lname
    

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


# class student(Person):#Child
# 	pass

# class mother(student):
#     pass

# x =student("John", "Doe")
# x.printname()

# y=Person("khadija","khatun")
# y.printname()

# z=mother("juhair","fahmid")
# z.printname()




# class Person:
#   def __init__(self, fname, lname):#parent
#     self.firstname = fname
#     self.lastname = lname
    

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


# class student(Person): #Child
#   def __init__(self, fname, lname,year):
#      super().__init__(fname, lname)
#      self.graduationyear = year

# x =student("John", "Doe",2019)
# x.printname(x.graduationyear)
  
# list1=[4,6,7,8,9,10,2]
# Even_list=[]
# odd_list=[]
# for i in list1:
#     if i%2 == 0:
#         Even_list.append(i)
        
#     else:
#         odd_list.append(i)

# sum=0
# for j in Even_list:
#     sum=sum+j
#     print(j)
# print("Total even number sum =",sum)

# sum=0
# for k in odd_list:
#     sum=sum+k
#     print(k)
# print("Total odd number sum =",sum)

# flag=int(input())
# search=1

# for i in list1:
#     if i == flag:
#       print("The number",i)
#       break
    
# print("Not found")

#find out sum  
# mylist=[8,10,15,3,2,4,0,6,88,9,3,8]

# sum=0
# for i in mylist:
#     sum=sum+i
# print("Total sun of myList",sum)

# Even_list=[]
# odd_list=[]

# for i in mylist:
#     if i%2 == 0:
#         Even_list.append(i)
#     else:
#         odd_list.append(i)
# sum=0

# for j in Even_list:
#     sum=sum+j
# print(Even_list)
# print("total even number sum",sum)



# list=[1,8,9,10]
# sum=0

# def A():
#     for i in list:
#         sum=sum+i
#         return sum
    
# A(list)


# mylist=[8,10,15,3,2,4,0,6,88,9,3,8]

# sum=0
# for i in mylist:
#     sum=sum+i
# print("Total sun of myList",sum)



