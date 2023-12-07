import turtle
import random


class Polygon:
    def __init__(self, size, orientation, location, color, border_size):
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        reduction_ratio = 0.618
        self.size *= reduction_ratio
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]               


class PolygonSimulator(Polygon):
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.num_list = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(self.num_sides):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            border_size = random.randint(1, 10)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.num_list.append(Polygon.draw_polygon(num_sides, size, orientation, location, color, border_size))

    def run(self):
        while True:
            turtle.clear()
            for i in range(self.num_sides):
                self.num_list[i].draw_polygon()
            turtle.update()
        turtle.done()


num_sides = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
class_ploygon = PolygonSimulator(num_sides)
PolygonSimulator.run()

# turtle.speed(0)
# turtle.bgcolor('black')
# turtle.tracer(0)
# turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = Polygon.get_new_color()
# border_size = random.randint(1, 10)
# Polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618

# reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
# size *= reduction_ratio

# draw the second polygon embedded inside the original 
# Polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
# turtle.done()