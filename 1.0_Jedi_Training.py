'''
1.0 Jedi Training (17pts)  Name: Jake Staton


1. Define Forking (1pt): Creating a copy of a shared read-only repository.

2. Define Cloning (1pt): After forking, the repository is then cloned in order
to make changes. This becomes known as a local repository.

3. Define Branching (1pt): A repository with multiple strands of development
occurring simultaneously.

4. Define Committing (1pt): A 'commit' is a checkpoint in the development
process.

5. Define Merging (1pt): After a repository is cloned and changes have been made,
The editor can make a 'pull request', if accepted, the cloned repository will
combine with merge or combine with the original code.

6. Define Pushing (1pt): Pushing is essentially 'moving' all of our commits
and changes to our remote repository.

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,185) #right ear
yoda.pendown()
yoda.goto(200,210)
yoda.goto(88,145)
yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.goto(-200,210)
yoda.goto(-88,145)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')


yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
