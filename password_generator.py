import random
import string

# this program generates a password

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to password generator!")
count_letters = int(input("How many letters would you like in your password?: "))
count_symbols = int(input("How many symbols would you like?: "))
count_numbers = int(input("How many numbers would you like?: "))

# 1 - way of generating password
total_character = count_symbols + count_letters + count_numbers
character_list = [letters, numbers, symbols]
generated_password = ""

while (count_letters + count_symbols + count_numbers) != 0:
    chosen_type = random.choice(character_list)
    generated_character = random.choice(chosen_type)
    if generated_character in letters:
        count_letters -= 1
        if count_letters == 0:
            character_list.remove(letters)
    elif generated_character in symbols:
        count_symbols -= 1
        if count_symbols == 0:
            character_list.remove(symbols)
    elif generated_character in numbers:
        count_numbers -= 1
        if count_numbers == 0:
            character_list.remove(numbers)
    generated_password += generated_character

print(generated_password)


# 2 - way of generating password
password_list = []
password = ""

for n in range(count_letters):
    password_list.append(random.choice(letters))
for n in range(count_symbols):
    password_list.append(random.choice(symbols))
for n in range(count_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
for character in password_list:
    password += character

print(password)
