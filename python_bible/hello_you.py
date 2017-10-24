#Ask user for name
name = raw_input("Name: ")

#Ask for age
age = raw_input("How old are you: ")

#Ask for city
city = raw_input("Which city are you from: ")

# Ask what they enjoy
hobby = raw_input("Any Hobbies: ")

#Create output text
output = "{} is {} year old, living in {}, and love to play {} sometime"

#Print Output to screen
print output.format(name, age, city, hobby)
