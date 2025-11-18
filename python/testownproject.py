# EMPTY until i learn shit, inshallah,,,,,,

# import requests

# while True:
#     try:
#         testpingsite = input("insert website \n")
#         response = requests.get("https://" + testpingsite, timeout=5)
#         print(f"{testpingsite} can be accessed")
#     except:
#         print(f"{testpingsite} cannot be accessed")


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# for i in range(15):
#     print(f"{fib(i)}")


# choice = input("°C or °F\n <> ")

# def Fahrenheit(F):
#     f = float(F)
#     cal = (f - 32) * 5/9
#     return cal

# def Celcius(C):
#     c = float(C)
#     fah = (c * 9/5) + 32
#     return fah

# if choice == "C" or choice == "c":
#     w = input("Input Celcius to Fah\n")
#     print(f"{Celcius(w)}°F")
# elif choice == "f" or choice == 'F':
#     b = input("Input Fah to Celcius\n")
#     print(f"{Fahrenheit(b)}°C")
# else:
#      print("wtf did you type")

#  To-Do List - 2025-11-9 this confusing ngl
# import os.path, sys

# k = 'save.txt'

# if os.path.isfile(k) == False:
#     open("save.txt", 'x')
#     print("file not found, creating")
# else:
#     print("file found, dimwit")

# commands = print("\n R - Read, W - Write, E - Exit")

# def iqra():
#     try:
#         with open(k, "r") as l:
#             reading = l.readlines()
#             if not reading:
#                 print("wtf")
#             else:
#                 print("shit you have to do")
#                 for i, reading in enumerate(l, 1):
#                     print(f"{i}, {reading.strip()}")
#     except Exception as e:
#         print(f"error {e}")

# def writing():
#     with open(k, "a") as l:

# iqra()
