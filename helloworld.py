#this is comments


y="Faiz Mohammed"



firstName = y[0:4]
Age=35
wight=71

myInfo="My First Name " + firstName + ",Iam {} old"
myInfo=myInfo.format(Age)




fruits = ("apple" , "banana" , "cherry")


thisdict = {
"brand" : "Ford" ,
"model" : "Mustang" ,
"year" : 1964
}

thisdict["color"]="white"

if fruits[1]=="banana":
 print("your selection correct")
else:
 print("your selection not correct")
 
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[1])


 


print("********************************")


print("*****Before*****")
print("Name: " + y)
print("First Name: " + firstName)
print(myInfo)



print("*******After******")


if firstName in y:
    print("first name exit")
if firstName not in y:
 print("first name Not  exit")

print("Frist Name: " + firstName)


print("********************************")




def myFunction(food):
 

 print("###START###")
 print("hello to my function")

 

 print("####END###")


myFunction(fruits)



print("-----------------------------------")




