# make a geometric pattern
import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black")

##for n in range(6):
  ##shelly.forward(100) #moves 100 steps forward in one direction
  ##shelly.left(60) #turns 60 degrees to the left


colors = ["red", "orange", "yellow", "green", "blue", "violet"]


for n in range(36):
  for i in range(6):
      shelly.color(colors[i])
      shelly.forward(100)
      shelly.left(60)
  shelly.right(10)



shelly.penup()
shelly.color("white")

for i in range(36):
  shelly.forward(220)
  shelly.pendown() #there needs to be a penup and pendown because it helps avoid the turtle make unnecessary tracks in the design.
  shelly.circle(5)
  shelly.penup()
  shelly.backward(220)
  shelly.right(10)
  shelly.hideturtle()