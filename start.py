print('Bartosz Rzemek')
x = 3 #integer
f = 3.24 #float
name = "Python" #string
arr = ["apple", "banana", "cherry"] #list
dict = {"name" : "John", "age" : 36, "maria" : 33} #dict
logic = True #boolean
name = name[1:4]
x = 1/3
sum =  x + f
age = str(dict["age"])
johnAge = age + " John"
johnAge2 = "John age is: %s, x : %s" % (age, x)

print('Age: %s, X: %s' % (age, x))
age = int(age) + 1
maria = list(dict)[2]
ageFromUser  = input("What is your age?:")
ageFromUserInt = int(ageFromUser)
print("Your age is: %s" % ageFromUser)


sumInteger = (int(x) + int(f))

print(sumInteger)