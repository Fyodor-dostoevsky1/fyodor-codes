num=int(input("enter your number:"))
print(num)

num2=int(input('enter your second number:'))
print(num2)

add = int(num +num2)
substract = int(num - num2)
multiply = int(num * num2)
division = float(num / num2)
exponential = (num ** num2)
print('additon of your number is : ', add)
print ('substraction of your numbers is :' , substract)
print('multiplication of your number is:' , multiply)
print('divisio of your numbers is:' , division)
print('expotential of your number is :', exponential)





# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("A Message for Venus")

# # Create the turtle
# pen = turtle.Turtle()
# pen.color("red")
# pen.pensize(3)
# pen.speed(5)

# # Function to draw a heart
# def draw_heart():
#     pen.begin_fill()
#     pen.left(50)
#     pen.forward(133)
#     pen.circle(50, 200)
#     pen.right(140)
#     pen.circle(50, 200)
#     pen.forward(133)
#     pen.end_fill()

# # Draw the heart
# pen.penup()
# pen.goto(0, -150)
# pen.pendown()
# pen.fillcolor("red")
# draw_heart()

# # Write the message
# pen.penup()
# pen.goto(0, 0)
# pen.color("white")
# pen.write("Dear Venus,\nYou light up my world!", align="center", font=("Arial", 24, "bold"))
# pen.hideturtle()

# # Keep the window open
# turtle.done()






import time
import sys
import os

# Function to display a heart animation
def heart_animation():
    heart = [
        "  ***     ***  ",
        " *****   ***** ",
        "******* *******",
        " *********** ",
        "  *********  ",
        "   *******   ",
        "    *****    ",
        "     ***     ",
        "      *      "
    ]
    
    for _ in range(3):  # Repeat animation
        for line in heart:
            print(line)
        time.sleep(0.5)
        sys.stdout.write("\033[F" * len(heart))  # Move cursor up to redraw
        sys.stdout.flush()
    
    print("\n")

# Function to display text with a typing effect
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# Function to propose to Venus
def propose_to_venus():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    heart_animation()
    
    type_text("Dear Venus,\n\n", 0.08)
    type_text("From the moment I met you, my world has been brighter.\n", 0.07)
    type_text("You are the star that lights up my universe.\n", 0.07)
    type_text("Every moment with you feels magical, and every day, I find myself falling for you even more.\n", 0.06)
    type_text("\nWould you make me the happiest person in the galaxy and be my Venus forever? 💖", 0.08)
    
    # User input for response
    answer = input("\nType 'Yes' if you accept, or 'No' if you want me to try harder: ").strip().lower()

    if answer == "yes":
        type_text("\n✨ YAY! You've made me the happiest person in the world! ✨", 0.08)
    elif answer == "no":
        type_text("\n💔 Oh no! I'll try even harder to win your heart! 💔", 0.08)
    else:
        type_text("\n🤔 I'll take that as a 'Maybe'... but I'll keep trying! 💖", 0.08)

# Run the proposal
propose_to_venus()
# #noice!!!!!!!