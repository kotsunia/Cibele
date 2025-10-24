# inshallah
# ------------


# name = input("Your name: ")

# print("your name has this amount of letter: ", int(name))
# ------

# maths = int(input("how many breads have you eaten in your life? "))

# print(f"YOU ATE HOW MUCH? YOU MANAGED TO EAT {maths} FULL SLICES OF BREAD???")
# ------
# a = 1
# b = '2'
# c = 400.3222

# print(type(len(b)))
# ------

# idk why not working lmfao, i maybe be dumb at maths
# floating = float(input("input a floating number please (it will round to 3 decimal places) "))

# print(round(floating, 3))
# ------
# meth = eval(input())

# print(meth)

# user = "cambrao"
# passw = "foda"

# if user == "cambrao":
#     print(f"hello {user}")
#     if passw == "foda":
#         print("vai se foder")
# else:
#     print("vai-te embora e se foda-te")


# idk if i am an idiot

# name = input("Whatcha name? ")
# age = input("What's your age? ")

# if name == 'Foda':
#         print("text")
# elif int(age) == 20:
#     print("Nao podes entrar cralho")


# today_is_opposite_day = oppo_day, say_it_is_opposite_day = isit_oppo_day IDK WHY NOT WORKING SOB
# oppo_day = True


# if oppo_day == True:
#     isit_oppo_day = True
# else:
#     isit_oppo_day = False


# if oppo_day == True:
#     isit_oppo_day = not isit_oppo_day
# if isit_oppo_day == True:
#     print("Oppo day yes!")
# else:
#     print("no oppo day :[")


# print(f"Enter GB/TB for the unit")
# unit = input(">> ")

# true_size = 0

# if unit == 'TB' or unit == "tb":
#     true_size = 1000000000000 / 1099511627776
# elif unit == "GB" or unit == "gb":
#     true_size = 1000000000 / 1073741824

# print("AD Size")
# ad_size = float(input(">>> "))

# real_size = str(round(ad_size + true_size, 2))

# print(f"blah blah {real_size + unit}")

# bread = 7

# while bread < 8:
#     print("I LOVE BREAD <3")
#     bread = bread + 1


# name = input()

# while name != str("namey"):
#     print(name)
# print("thanks")


# while True:
#     print("Please type your name\n")
#     name = input(">")
#     if name == "namey":
#         break
# print("Thanks bitch")

# while True:
#     print("Quem e?")
#     nome = input()
#     if nome != "joao":
#         continue
#     print("what's the mf password?")
#     passw = input()
#     if passw == "Wow":
#         break
#     print("bem-vindo")
#     quit()


# print("ola")
# for i in range(5):
#     print(f"something something i is set to {str(i)}")
# print("\nbyeee")


# a = 0

# for number in range(101):
#     a = a + number
# print(a)


# print("no")

# i = 0

# while i < 8:
#     print(f"something something i is set to {str(i)}")
#     i = i + 1
# print("byeeee")


# for i in range(5, -1, -1):
#     print(i)


# import random

# for i in range(5):
#     print(random.randint(1, 10))


# import random, sys, os, math

# while True:
#     print("Type quit to quit duhhh")
#     reply = input("\n >")
#     if reply == "exit":
#         sys.exit()
#     print(f"twat {reply}")


# import random, sys
# num = random.randint(1, 50)


# i didn't even read this one lmfao
# for guess in range(1, 6):
#     print(f"what is the number the computer is thinking {num}")
#     guess = int(input("\n <>"))
#     if guess == num:
#         print("woww")
#         sys.exit()
#     else:
#         if num < guess:
#             print("number is lower")
#         elif num > guess:
#             print("number is higher")


# wtf am i doing with this rps
# import random, sys

# rps = ["rock", "paper", "scissors"]

# wins = 0
# losses = 0
# ties = 0

# while True:
#     wow = random.choice(rps)

#     print(f"rock paper scissors \n {wins} wins, {losses} losses, {ties} ties\n")
#     print(f"{wow}")

#     game = input("\n<>")
#     if wow == game:
#         ties = ties + 1
#         print("Tied")
#         continue
#     elif game == "quit":
#         sys.exit()
#     elif game != wow:
#         losses = losses + 1
#         print(f"Failed, it was {wow}")
#         continue
