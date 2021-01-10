# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#split(", ") splits the string in list of strings using separator ", "

print(names)
winner=random.randint(0,len(names))
print(f"{names[winner]} is going to buy the meal today!")

