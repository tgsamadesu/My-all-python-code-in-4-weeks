# Calculator :
'''print ("Enter your fisrt num")
n1 = input ()
print ("Enter your second num")
n2 = input ()
print ("Your sum of following number is... ", int (n1) + int (n2))'''
# Dictionary :
'''d1 = {"Manga":"Whimsical-Pictures", "Nani":"What", "Kami":"God", "Nanda":"Why"}
print ("Search meaning for... ")
inp = input ()
print ("Results...")
print (d1[inp])'''
# If-Else-Elif :
'''var1 = 420
var2 = int(input())
if var2>var1:
    print ("Greater")
else:
    print ("Less")'''
'''print ("Enter your age... ")
age = int(input())
if age<7 or age>100:
    print ("Umm... are you serious??")
elif age==18:
    print ("We'll think about it...")
elif age>18:
    print ("Yes you can drive!")'''
# Faulty Calculator:
'''print ("Enter your number")
n1 = input ()
print ("Enter your second number")
n2 = input ()
print ("You've entered a invalid number.", "Please Enter a valid number")'''
# For Loop:
'''lsit1 = ["8000", "5", "90", "2"]
print ("Ask")
inp = input()
if lsit1>6:
    print ("It's a valid number")
else:
    print ("It's a invalid number")'''
'''items1 = [20, 29, 20, 190, 6, 3, 8, 9, 2,]
for item in items1:
    if str(item).isnumeric and item>6:
        print (item)'''
# While loop:
'''i = 0
while(i<45):
    print (i+1)
    i = i + 1 '''
'''print("enter a random number")
c = int(input())
if c>=100:
    print(c, "is valid")
while (c<=100):
    print("Error input another number")
    c = int(input())
    print(c, "is valid")'''
# My First Succsesful Quiz:
'''while (True):
    n1 = int(input))
        print("Enter your number...\n"))
    if n1==100:t ("You have entered a valid number\n")
        break'''
# A fail exercise:
'''n1 = input ("Enter your num..." ,)
n2 = input ("Enter your sec num..." ,) 
print ("Your answer is", int(n1) * int(n2))'''
'''while (True):
    print ("Guess the number. (9 Guesses left")
    inp = input()
    if inp==18:
        print ("You've entered a right number!")
        break
    elif inp>18:
        print ("You've entered the wrong number!")
        continue
    else:
        print ("You have 8 choices ")'''
# A Successful code of someone:
'''n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")'''
# Try except exception handling:
'''print ("Enter you first num")
n1 = input()
print ("Enter your sec num")   
n2 = input ()
try:
    print ("Your sum of these two numbers is",
    int (n1) + int (n2))
except Exception as e:
    print ("Sinjeki no kyojin")'''
# PYTHON FILE IO BASICS (IMPORTANT):
'''r : r mode opens a file for read-only. We do not have permission
 to update or change any data in this mode.
w : w mode does not concern itself with what is
 present in the file. It just opens a file
  for writing and if there is already some
   data present in the file, it overwrites it.
x : x is used to create a new file. It does
 not work for an already existing file, as
  in such cases the operation fails.
a : a stands for append, which means to
 add something to the end of the file. It
  does exactly the same. It just adds the
   data we like in write(w) mode but
   instead of overwriting it just adds
    it to the end of the file. It also
     does not have the permission of reading the file.
t : t mode is used to open our file in text
 mode and only proper text files can be opened
  by it. It deals with the file data as a string.
b : b stands for binary and this mode
 can only open the binary files, that are
  read in bytes. The binary files include
   images, documents, or all other files
    that require specific software to be read.
+ : In plus mode, we can read and write
 a file simultaneously. The mode is mostly
  used in cases where we want to update our file.'''
'''f = open("tg3.txt", "a")
f.write("Pokemon sarre kisne maare?")'''
# Someone's sccessful code:
'''print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()'''
# Reccursions and Iteratives:
'''# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))'''
# BOTCHAT PROGRAM:
'''print ("Do you want to become a programmer?")
n1 = input("Yes or No\n")
if n1 == "Yes":
    print ("Good, Y'know I'm learning programming too!.\n")
elif "No":
    print ("Oh, so bad I was thinking if we could program together...\n")
else:
    ("You should, it's fun!\n")'''
# WHEN YOU"LL BE 100 YEARS OLD CALCULATOR:
'''name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2022 - age)+100)
print(name + " will be 100 years old in the year " + year)
    '''
# QUIZ😎:
'''import pygame
x = pygame.init()
Quiz = pygame.display.set_mode((1200, 500))
print("What is the capital of Paksitan?🤔")
q1 = input()
if q1== "Islamabad":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("Who is the most badass character in demon slayer?🤔")
q1 = input()
if q1== "Yorrichi":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("What is the salary of Mizunoe in demon slayer?🤔")
q1 = input()
if q1== "30,000 Yen":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("What is the best thing about demon slayer?🤔")
q1 = input()
if q1== "Characters" or "Character":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("What is the second name of Tengen Uzui?🤔")
q1 = input()
if q1== "Flamboyant":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("Who is the strongest hashira/demon slayer?🤔")
q1 = input()
if q1== "Himejima" or "Gyomei" or "Himejima Gyomei" or "Gyomei Himejima":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
print("Who the most kind character in demon slayer?🤔")
q1 = input()
if q1== "Tanjiro":
    print ("Correct Answer!🤗")
else:
    print ("You're wrong!😫")
'''
'''print ("What era Tanjiro lived in Japan of demon slayer?🤔")
print ("A. Sengoku Era")
print ("B. Taisho Era")
print ("C. Reiwa Era")
n1 = str(input())
if n1=="A" or "a" or "C" or "c":
    print ("Wrong Answer❌")
else:
    print ("Correct Answer✔")
'''
'''from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is :", current_time)'''
# SOMEONE'S SUCCESSFUL GAME 😮:
'''import random
n = input('Enter your name : ')
print('Welcome to our game ',n, '- Snake Water Gun')
r = int(input('Enter the number of rounds you wants to play : '))
rounds = 1
options = ['s','w','g']
player_win = 0
computer_win = 0

while rounds <= r:
    print(f"Round : {rounds}")
    print("Hit 's' for snake , Hit 'g' for gun , Hit 'w' for water")
    player = input('Choose your option : ')
    if player!='s' and player!='g' and player!='w':
        print('Invalid input! Please enter again')
        continue
    computer = random.choice(options)
    
    if computer=='s':
        if player=='g':
            player_win +=1
        elif player=='w':
            computer_win +=1
            
    if computer=='g':
        if player=='w':
            player_win +=1
        elif player=='s':
            computer_win +=1
            
    if computer=='w':
        if player=='s':
            player_win +=1
        elif player=='g':
            computer_win +=1
            
    if player_win>computer_win:
        print('Congarts!You win in this round', n)
    elif player_win<computer_win:
        print('Oops!You lose in this round', n)
        print('Better luck next time')
    else:
        print('Round draw!', n)

    rounds +=1

if player_win>computer_win:
    print('Congrats!You win the game', n)  
elif player_win<computer_win:
    print('Oops!You lose the game', n)
else:
    print('Match draw!', n)
print('Your score : ',player_win)
print('Computer score : ',computer_win)'''
# MY FAILED GAME 🙄:
'''import random
name = input("Enter your name:\n")
print ("Welcome",name,",to Snake, Water, Gun!")
print ("s for Snake, w for water, g for gun")
print ("Choose your option...")
 if player!='s' and player!='g' and player!='w':
        print('Invalid input! Please enter again')
        continue
    computer = random.choice(options)
    
option = input()
computer = 0
player_win = 0
if option =="s":
    if computer =="g":
        computer +=1
    elif option =="w":
        player_win +=1'''
# *ARGS AND **KWARGS:
'''# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)'''
'''name = str(input("Enter your name...\n"))
print ("Welcome",name,"to a little quiz of Demon Slayer/Kimetsu no yaiba.\n","You just have to answer to the quetions asked by program and get points!\n If you give a 'Wrong answer' the program will subtract your point\n and if you give a 'Correct answer' you'll get a point\n and your all points will be shown at last of the game.\nGood luck!")    
points = 0
print("Who is the most badass character in demon slayer?🤔") #1
q1 = input()
if q1== "Yorrichi":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print("What is the salary of Mizunoe in demon slayer?🤔") #2
q1 = input()
if q1== "30,000 Yen":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print("What is the best thing about demon slayer?🤔") #3
q1 = input()
if q1== "Characters" or "Character":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print("What is the second name of Tengen Uzui?🤔") #4
q1 = input()
if q1== "Flamboyant":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print("Who is the strongest hashira/demon slayer?🤔") #5
q1 = input()
if q1== "Himejima" or "Gyomei" or "Himejima Gyomei" or "Gyomei Himejima":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print("Who the most kind character in demon slayer?🤔") #6
q1 = input()
if q1== "Tanjiro":
    print ("Correct Answer!🤗")
    points +=1
else:
    print ("You're wrong!😫")
    points -=1
print ("Your points are:", points)
print ("If your points are bad then do you want to try the 'Lucky number score' option to increase your points?\n")
askifyesfunc = str(input("Select a option y/n, y for yes and n for no." ,))
if askifyesfunc == "y":
    print ("The program will ask a number and if you answer it correct you'll get 100+ points!")
    askifyesfunc2 = int(input("Answer here:" ,))
    if askifyesfunc2 ==24084: 
        points +=100
        print ("Correct answer! Your points:",points)
    else:
        print ("Goodbye fella!")
'''
'''from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("song.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
	
	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	query = input(" ")
	
	if query == 'p':

		# Pausing the music
		mixer.music.pause()	
	elif query == 'r':

		# Resuming the music
		mixer.music.unpause()
	elif query == 'e':

		# Stop the mixer
		mixer.music.stop()
		break'''
# FINALLY PLAYSOUND WORKED 😌:
'''from playsound import playsound
playsound('Z:/Project calculator/sound/gaana.mp3')
'''
# DECORATORS:
'''def inner1(func): 
    def inner2():
        print("Executing..."); 
        func() 
        print("Executed!")    
    return inner2 

@inner1
def function_to_be_used(): 
    print("Misiile launched, Seccesfully!") 

function_to_be_used()  '''
# FIRST CLASS 😎:
'''class Betsu_No_Sekai:
    pass
tg = Betsu_No_Sekai()
Shinae = Betsu_No_Sekai()
Shouko = Betsu_No_Sekai()
Maki = Betsu_No_Sekai()
Reijie = Betsu_No_Sekai()
tg.name = "TG"
tg.elements = ["Flame", "Water", "Speed"]
tg.danger_level = "1"
Shinae.name = "Shinae"
Shinae.elements = ["Psychic", "Magic"]
Shinae.danger_level = "7"

info = input("Who want to know about?😋:\n")
if info == "TG" or "tg" or "Tg":
    print ("Name:", tg.name,"\n" "Elements:", tg.elements,"\n" "Danger Level:", tg.danger_level)
elif info == "Shinae" or "shinae":
    print ("Name:", Shinae.name)
    print ("Elements", Shinae.elements)
    print ("Danger Level", Shinae.danger_level)
else:
    print ("Invalid Input!")
'''
'''ask_password = input("Enter the password\n")
if ask_password == "TGSamaDesu":
    pass
else:
    print ("Incorrect Password.")'''
#PYGAME TUTORIALS😂:
'''# Import and initialize the pygame library
from turtle import Screen
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 0, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit() 

'''
# Just a game 🙂:
'''name = input("Name: ")
print ("Please tell me a little about yourself", name,"and I'll guess your gender 😎")
print ("So, what are your hobbies", name,"?")
hobbies = input("My hobbies are: ")
fav_food = input("What type of food is your favourite, spicy or sweet?: ")
fav_colour = input("My favourite color is: ")
if hobbies == "Games" or "Game" or "game" or "gaming" or "Gaming", fav_food == "Spicy" or "spicy" or "Spice" or "spice",
    fav_colour == "Black" or "black" or "Blue" or "blue":
    fav_food == "Spicy" or "spicy" or "Spice" or "spice":
    fav_colour == "Black" or "black" or "Blue" or "blue":
    boy = input("You're a boy! Am I right? y/n ")
             if boy== "y":
                print("Yes😋! Thanks for playing!")
            else:
                print ("Oh NO! I should have guessed it right😫! Anyways, thanks for playing!")            
if hobbies == "Tennis" or "tennis" or "playing" or "Playing":
    if fav_food == "Sweet" or "sweet" or "sweets" or "Sweets":
        if fav_colour == "pink" or "Pink" or "red" or "Red":
            girl = input("You're a girl! Am I right? y/n ")
            if girl == "y":
                print("See, I told you I can guess it right!😎 Thanks for playing!")
            elif girl == "n":
                print ("Ohh Mann🙄 Anyways, thanks for playing!")'''
# A MOTIVATION APP 😀:
'''import random
ask_moti = input("Ask for motivation? Type M or m: ")
moti = ["You can get everything in life you want if you will just help enough other people get what they want.",
"Inspiration does exist, but it must find you working.",
"Show up, show up, show up, and after a while the muse shows up, too."]
if ask_moti == "M" or "m":
    print (random.choice(moti))
else:
    print("Was it a valid input?")'''
# MULTILEVEL INHERITANCE:
'''class Electronic_device():
    power_source = "Alternating current or Direct Current"
    use = "Automates works and make the work very faster and efficient"
    start = "It is a kind of device which uses"
   
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}".capitalize()

class Pocket_gadget(Electronic_device):
    power_source = "Direct current"
    addon_features = "It is portable and looks super awesome"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()

class Phone(Pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


computer = Electronic_device()
miband = Pocket_gadget()
redmi = Phone()

print(computer.printdetails())
print(miband.printdetails())
print(redmi.printdetails())'''
