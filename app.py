# if 5 < 2:
#     print("Five is greater than two!")
#     else
""" print("Hello world")
print("Hello world") """
# print("Hello From Uzbekistan") #it is example to do comment any lines in python.

"""x = 5
y = "John"
print(type(x))
print(type(y)) """

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)

# fruits = ["Apple", "Banana", "Cherry"]
# x, y, z = fruits
# print(y)

# familya = ["Ibrohimova", "Ibrohimov"]
# x, y = familya
# print(y)

# x = "python"
# y = "is"
# z = "awesome"
# print(x + y + z)

# x = "awesome"

# def myFunc():
#     print("Python is " + x)

# myFunc()



# def myFunc():
#     global x, y
#     x = "fantastic"
#     y = "John"

# myFunc() 

# print(y, "is",x)

# x=5
# print(type(x))

# import random

# print(random.randrange(3, 6))

# a = "Hello world"
# print(a[1])

# txt = "The best  things in life are free"
# print("free" in txt)  # Elemen bor yoki yoqligini tekshirish

# Agar print sozi txt qiymatida bolsa ekranga qandaydur soz chiqarish!
# txt = "The best  things in life are free"
# if "or" in txt:
#     print("Yeah, 'free' is present.")

# Biror yozuv yoqligini tekshirish
# txt = "The best things in life are free!"
# print("The" not in txt)

# txt = "The best  things in life are free"
# if "expensive" not in txt:
#     print("Bu soz txt qiymatida mavjud emas!")

#Get the characters from position 2 to position 5 (not included):
# b = "Hello world"
# print(b[-5:-2])

#Write code as uppercase 
# a = "Hello world from Uzbekistan world"
# print(a.replace("w", "J"))

# a = "Hello, world"
# print(a.split(","))

#Stringlarni bir-biriga qoshish
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

#Format strings
# age = 36
# txt = "My name is John, and I am {} "
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# txt = "We are the so-called \"Vikings\" from the north."

#Here we learni BOOLEANS
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# print(bool("Hello"))
# print(bool(1))

# def myFunction() :
#     return False

# print(myFunction())

# def myFunction() :
#   return False

# if myFunction():
#   print("YES!")
# else:
#   print("NO!") 

#String yoki integer ekanligini True yoki false qilgan xolatda tekshirish
# x = 20
# print(isinstance(x, int))


#Learn operators
# x = 100
# y = 2

# print(x // y)

# x = 5

# x <<= 10

# print(x)

# x = 5

# print(not(x > 10 and x < 10))

# x = ["Banana", "apple", "orange"]
# print("pinaple" not in x)


#############################################################################################################
#############################################################################################################
######################################  Learn lists section      ############################################
#############################################################################################################
#############################################################################################################


# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1)
# print(list2)
# print(list3)

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "orange"]
# thislist[1] = "watermelon"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)



# thislist = ["apple", "banana", "watermelon"]
# thislist.insert(1, "orange")
# print(thislist)


#Listni bir-biriga qo'shish.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


#List qo'shish
# thislist = ["Apple", "Banana", "pineapple"]
# thislist.append("orange")
# print(thislist)


#Keraksiz listni o'chirish
# thislist = ["Apple", "Banana", "pineapple"]
# thislist.remove("Apple")
# print(thislist)


#Keraksiz listni raqam bilan o'chirish usuli
# thislist = ["Apple", "Banana", "pineapple"]
# thislist.pop(0) #Bu raqamni o'rniga tepadagi biror bir item ni raqamini yozish mumkin, xozirgi natijada "Apple" stringi o'chadi! Agarda pop yozib raqam bilan korsatilmasa, oxirgi item o'chadi
# print(thislist)

#Keraksiz listni del keywordi bilan o'chirish!
# thislist = ["Apple", "Banana", "pineapple"]
# del thislist[0]
# print(thislist)

#Shuningdek Del keywordi butun LIST ni o'chiraoladi!, Bunda shunchali del keywordidan to'rt burchak qavs ochilmaydi, va del dan so'ng o'chirilishi kerak bo'lgan o'zgaruvchi nomi yoziladi.
# thislist = ["apple", "banana", "cherry"]
# del thislist 
# print(thislist)


#Listni tozalab yuborsaham bo'ladi, bu usul clear buyrugu orqali bo'ladi, list ochirib tashlanmaydi, eslab qolinadi, lekin contentni yo'q xisoblanadi.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["12", "13", "14", "15", "16"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = False)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


################ Tushunmagan mavzularim. W3schools: Sort Lists, 

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


#Listni copy qilish, 2 ta usuli mavjud
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# myList = thislist.copy()
# print(myList)

#Listni copy qilishni 2 chi usuli
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# myList = list(thislist)
# print(myList)

#Join lists 
# list1 = ["banana", "orange"]
# list2 = ["kiwi", "pineapple"]
# list3 = list1 + list2
# print(list3)

#Tuple ni o'rganamiz!
thistuple = ("apple",) #agar tuple 1 ta item dan iborat bo'lsa, shu itemdan so'ng vergul bo'lishi kerak, bo'lmasam python uni tuple ekanligini aniqlay olmaydi! :(
print(type(thistuple))

