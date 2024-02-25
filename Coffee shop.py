#Lets build a robot barista!!
print("Hello, welcome to Mikes Coffee")
name = input("What is your name? \n")

if name == "Ben" or name == "Patricia" or name == "Loki":
  evil_status = input("Are you evil?\n")
  good_deed_status = int(input("How many good deeds have you done today?\n")) # Convert input to integer
  if evil_status == "Yes" and good_deed_status < 4:
    print("You're not welcome here " + name + ". Get out!")
    exit()
  else:
    print ("Hello " + name + ", thank you so much for coming in today.\n")
    menu = """Black Coffee, 
Latte,
Cappuccino.\n"""
  print(name + ", What would you like from our menu today? Here is what we are serving\n" + menu)
  order = input()
  price = 8
  quantity = input("How many coffees would you like?\n") # Convert input to integer
  total = price * int(quantity) # Convert input to integer
  print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "'s ready for you in a moment.\n")
  print("Here you go " + name +  ", that will be " + "£" + str(total) + " please.\n")
else:
  print("Hello " + name + ", thank you so much for coming in today.\n")
  menu = """Black Coffee, 
Latte,
Cappuccino.\n"""
  print(name + ", What would you like from our menu today? Here is what we are serving\n" + menu)
  order = input()
  price = 8
  quantity = input("How many coffees would you like?\n") # Convert input to integer
  total = price * int(quantity) # Convert input to integer
  print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "'s ready for you in a moment.\n")
  print("Here you go " + name +  ", that will be " + "£" + str(total) + " please.\n") # Convert total to strBen