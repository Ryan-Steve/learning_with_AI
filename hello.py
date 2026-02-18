#Exercise Day 1
#print function
print("My name is Stevieee")
print("I am",19 * 365,"days old")
print((100 + 50)*2 - 25)

#Exercise Day 2
#Data types
Fav_movie = "Need for Speed"
release_date = 2014
rating = 9.5 
print("\n My favourite movie  is",Fav_movie,"released in",release_date,"and I'd rate it",rating,"/10")

#Arithmetics using different data types
coffee_price = 4.5
no_of_coffee = 3
cost = coffee_price * no_of_coffee
print("\n Total cost of coffee is $",cost)

#Exercise Day 3
#String manipulaton
email = "stevie@gmail.com"
print(email.upper())
city = "Nairobi"
country = "kenya"
print("\n I live in",city.upper(),",",country.capitalize())
sentence= "Naibori is the capital of Kenya"
print(sentence.replace("Naibori","Nairobi"))

#Exercise Day 4
#Conditionals
age = int(input("Enter your age: "))

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're a senior")

# Multiple conditions
temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("Great day for a picnic!")




