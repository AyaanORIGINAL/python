import turtle 
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(500,500)

pen = turtle.Turtle()

num_sides = 7
side_length = 80
angle = 360/num_sides

for i in range(num_sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()