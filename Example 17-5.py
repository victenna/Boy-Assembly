import turtle
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('gold')

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()

image1='head_.gif'
image2='body_.gif'
image3='left_leg_.gif'
image4='right_leg_.gif'
image5='left_hand_.gif'
image6='right_hand_.gif'

wn.addshape(image1)
t1.shape(image1)
t1.up()
t1.goto(0,200)

wn.addshape(image2)
t2.shape(image2)
t2.up()
t2.goto(-300,300)

wn.addshape(image3)
t3.shape(image3)
t3.up()
t3.goto(100,100)

wn.addshape(image4)
t4.shape(image4)
t4.up()
t4.goto(-200,150)

wn.addshape(image5)
t5.shape(image5)
t5.up()
t5.goto(170,-250)

wn.addshape(image6)
t6.shape(image6)
t6.up()
t6.goto(210,-200)

def dragging2(x, y):
    t2.ondrag(None)
    t2.goto(x, y)
    t2.ondrag(dragging2)
t2.ondrag(dragging2)

def dragging3(x, y):
    t3.ondrag(None)
    t3.goto(x, y)
    t3.ondrag(dragging3)
t3.ondrag(dragging3)

def dragging4(x, y):
    t4.ondrag(None)
    t4.goto(x, y)
    t4.ondrag(dragging4)
t4.ondrag(dragging4)

def dragging5(x, y):
    t5.ondrag(None)
    t5.goto(x, y)
    t5.ondrag(dragging5)
t5.ondrag(dragging5)

def dragging6(x, y):
    t6.ondrag(None)
    t6.goto(x, y)
    t6.ondrag(dragging6)
t6.ondrag(dragging6)




