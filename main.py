import time
import getpass

print("Password is world")
while True:
  print("What's the Password?")
  passwd = getpass.getpass("Password: ")
  if passwd == "world":
    break
  else:
    print("Wrong Password! Try again!")
    time.sleep(1)
    print("Hint: look at the top")


print("Hello World!")
time.sleep(2)
print("What's your name?")
name = input("Name: ")
time.sleep(1)
print(f"Hello {name}!")
time.sleep(2)
print(f"What do you want to tell about {name}?")
ask = input("Type here: ")
time.sleep(1)
print("You said:", ask)
time.sleep(2)
print(f"Goodbye {name}!")
time.sleep(2)
print("Goodbye World!")
time.sleep(2)
