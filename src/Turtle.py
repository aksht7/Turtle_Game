import turtle
from random import randint

SIZE = 500

# setup the screen
sc = turtle.Screen()
sc.title("my_turtle")
sc.setup(SIZE + 250, SIZE + 40)
sc.bgcolor("white")

new_turtle = turtle.Turtle()
new_turtle.up()
new_turtle.shape("turtle")
new_turtle.color("black")
new_turtle.ht()


# returns a random position in the sc to put the new_turtle in later
def getRandPos():
    return (randint(-SIZE // 2, SIZE // 2), randint(-SIZE // 2, SIZE // 2))


# initialise randomly the position of the new_turtle
new_turtle_coor = getRandPos()

# setup the turtle
my_turtle = turtle.Turtle()
my_turtle.up()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.ht()

# initialise  my_turtle
my_turtle_coor = [(0, 0)]

stamps = []

# which direction for moving
dir_x = 0
dir_y = 0

stop = False


# clean and redraw the sc
def actualise_display():
    tracer = sc.tracer()
    sc.tracer(0)

    new_turtle.clearstamps(1)
    my_turtle.clearstamps(len(my_turtle_coor))

    new_turtle.goto(new_turtle_coor[0], new_turtle_coor[1])
    new_turtle.stamp()

    for x, y in my_turtle_coor:
        my_turtle.goto(x, y)
        my_turtle.stamp()

    sc.tracer(tracer)


# refresh the my_turtle position and check if died
def actualise_pos():
    global my_turtle_coor, new_turtle_coor, stop
    avance()
    if isSelfCollision() or isBorderCollision():
        stop = True
    if isnew_turtleCollision():
        append()
        new_turtle_coor = getRandPos()

    # main loop :


# - refresh my_turtle position
# - refresh drawings
def loop():
    if stop:
        gameOver()
        return
    actualise_pos()
    actualise_display()
    sc.ontimer(loop, 100)


# check if the my_turtle eats it self
def isSelfCollision():
    global my_turtle_coor
    return len(set(my_turtle_coor)) < len(my_turtle_coor)


# check if the my_turtle eat new_turtle
def isnew_turtleCollision():
    sx, sy = my_turtle_coor[0]
    fx, fy = new_turtle_coor
    distance = ((sx - fx) ** 2 + (sy - fy) ** 2) ** .5
    return distance < 20


# check if the my_turtle eat the border of the sc
def isBorderCollision():
    x, y = my_turtle_coor[0]
    return not (-SIZE // 2 - 50 < x < SIZE // 2 + 50) or not (-SIZE // 2 - 50 < y < SIZE // 2 + 50)


# move the my_turtle in the dir (using the dir global variables declared up)
def avance():
    global my_turtle_coor
    x, y = my_turtle_coor[0]
    x += dir_x * 20
    y += dir_y * 20
    my_turtle_coor.insert(0, (x, y))
    my_turtle_coor.pop(-1)


# append a new cell to the my_turtle
def append():
    global my_turtle_coor
    a = my_turtle_coor[-1][:]
    my_turtle_coor.append(a)


# change the my_turtle dir
def setDir(x, y):
    global dir_x, dir_y
    dir_x = x
    dir_y = y


def right(): setDir(1, 0)


def left(): setDir(-1, 0)


def up(): setDir(0, 1)


def down(): setDir(0, -1)


# display game over
def gameOver():
    d = turtle.Turtle()
    d.up()
    d.ht()
    d.color("black")
    d.write("GAME OVER\nScore:%04d" % (len(my_turtle_coor)*5), align="center", font=("monospace", 20))
    sc.onclick(lambda *a: [sc.bye(), exit()])


# attach events to keys
sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(right, "Right")
sc.onkeypress(left, "Left")
sc.listen()
loop()  # run the main loop
turtle.mainloop()