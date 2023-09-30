# Q1 ---------------------------------------------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
street = input("Enter your street: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

# Q2 ---------------------------------------------------------------

print(f'"Name: {name}"')
print(f'"Age: {age}"')
print(f'"Address: {street}, {city}, {country}"')

# Q3 ---------------------------------------------------------------

adjusted_age = age - 5
print(f'"Hello {name} Your age is {adjusted_age} Years Old, Your Address is {street}, {city}, {country}."')

# Q4 ---------------------------------------------------------------

print(type(name), type(age))
print(type(street), type(city))
print(type(country))

# Q5 ---------------------------------------------------------------

output_string = f'"Hello {name}, How Are You? \\ """ Your Age Is "{age}"" + And Your Country Is: {country}'
print(output_string)

# Q6 ---------------------------------------------------------------

output_string = f'"Hello {name}, How Are You? \\ \n""" Your Age Is "{age}"" + And\n Your Country Is: {country}'
print(output_string)

# Q7 ---------------------------------------------------------------

name = "ITF Gsg Python"
print(f'First Letter Is "{name[0]}"')
print(f'Second Letter Is "{name[1]}"')
print(f'Last Letter Is "{name[-1]}"')

# Q8 ---------------------------------------------------------------

print(name[4:7])
print(name[:3])
print(name[:6])
print(name[::-1])

# Q9 ---------------------------------------------------------------

name_with_symbols = "$&$Mohammed$&$&"
new_name = name_with_symbols.strip("$&")
print(new_name)

# Q10 ---------------------------------------------------------------

msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg.replace("%7", "Love")
print(new_msg)

# Q11 ---------------------------------------------------------------

num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"

print(f'{num1:05}')
print(f'{num2:05}')
print(f'{num3:05}')
print(f'{num4:05}')
print(f'{num5:05}')
print(f'{num6:05}')

# Note: The :05 in the format specifier ensures that each number is printed with at least 5 digits, adding leading zeros as needed.

# Q14 ---------------------------------------------------------------

# title() Method: Capitalizes the first character of each word in a string.
original_string = "i love gaza sky geeks with zakaria"
new_string = original_string.title()
print(new_string)
#output: I Love Gaza Sky Geeks With Zakaria

#capitalize() Method: Capitalizes the first character of the entire string.
original_string = "i love gaza sky geeks with zakaria"
new_string2 = original_string.capitalize()
print(new_string2)
#output: I love gaza sky geeks with zakaria

# Q15 ---------------------------------------------------------------

my_name = "Nour"

print(f'{"*" * 11}{my_name}')
print(f'{"*" * 11}{my_name}{"*" * 11}')
print(f'{my_name}{"*" * 11}')

# Q15 ---------------------------------------------------------------

name_one = "SaMER"
name_two = "Abed"

print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

# Q16 ---------------------------------------------------------------

# We can use the methods: islower() to check if a string contains only lowercase letters
# and isupper() to check if a string contains only uppercase letters

# Q17 ---------------------------------------------------------------

# startswith() method to check if a string starts with a specific substring
# endswith() method to check if a string ends with a specific substring

# Q18 ---------------------------------------------------------------

msg = "I Love Python And Although I Love GSG with Zakaria"
count_love = msg.count("Love")
count_t = msg.count("t")

print(f'Number of <Love> is: {count_love}')
print(f'Number of <t> is: {count_t}')

# Q19 ---------------------------------------------------------------

msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg.replace("%7", "Love", 1)
print(new_msg)



