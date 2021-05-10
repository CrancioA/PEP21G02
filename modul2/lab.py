# word = input("Enter the word: ")
# first_letter = word[0]
#
# if first_letter == 'S':
#     print('Yes - Spathiphyllum is the best plant ever!')
# elif first_letter == 's':
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not",word,"!")

# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     percent = (18/100) * income
#     tax = percent - 556.2
#     tax = round(tax, 0)
#     print(tax)
# else:
#     dif = income - 85528
#     percent1 = (32/100) * dif
#     tax = 14839.2 + percent1
#     tax = round(tax, 0)
#     print("The tax is:", tax, "thalers")

# year = int(input("Enter a year: "))
#
# if year >= 1582:
#     if year % 4 != 0:
#         print("It's a common year")
#     elif year % 100 != 0:
#         print("It's a leap year")
#     elif year % 400 != 0:
#         print("It's a common year")
#     else:
#         print("It's a leap year")
# else:
#     print("Not within the Gregorian calendar period")
from typing import List

secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# while True:
#     picked_number = int(input("Enter a number: "))
#     if picked_number == secret_number:
#         print("m-ai prins")
#     else:
#         print("fraiere")

# import time
#
# for numar in range(1, 6):
#     print(numar, "Mississipi")
#     time.sleep(1)

# c0 = int(input("Insert a number: "))
# step = 0
#
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 / 2
#         print(int(c0))
#         step += 1
#     elif c0 % 2 == 1:
#         c0 = 3 * c0 + 1
#         print(int(c0))
#         step += 1
# print("steps:", step)

# beatles = []
# print("Step 1:", beatles)
#
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
#
# for i in range(2):
#     beatles.append(input("Add new member to the band: "))
# print("Step 3:", beatles)
#
# del beatles[3]
# del beatles[3]
# print("Step 4:", beatles)
#
# beatles.insert(0, 'Ringo Starr')
# print("Step 5:", beatles)
#
#
# # testing list legth
# print("The Fab", len(beatles))

# my_list: list[int] = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list2 = my_list
#
# for i in my_list2:
#     if my_list2[i+1] == my_list2[i]:
#         del my_list2[i]
#     else:
#         print(my_list)

