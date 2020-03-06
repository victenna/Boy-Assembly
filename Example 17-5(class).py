import turtle
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('red')

class Boy(turtle.Turtle):
    
    def __init__(self,X,Y,image):
        super().__init__()
        wn.addshape(image)
        self.shape(image)
        self.up()
        self.goto(X,Y)
        self.down()
       
t1=Boy(0,0,'head_.gif')
t2=Boy(-200,-200,'body_.gif')
t3=Boy(200,200,'left_leg_.gif')
t4=Boy(140,-280,'right_leg_.gif')
t5=Boy(-200,200,'left_hand_.gif')
t6=Boy(300,0,'right_hand_.gif')


def dragg(turtle, x, y):
    turtle.up()
    turtle.ondrag(None)  # disable ondrag event inside drag_handler
    turtle.goto(x, y)
    turtle.ondrag(lambda x, y, turtle=turtle: dragg(turtle, x, y))

t2.ondrag(lambda x, y: dragg(t2, x, y))
t3.ondrag(lambda x, y: dragg(t3, x, y))
t4.ondrag(lambda x, y: dragg(t4, x, y))
t5.ondrag(lambda x, y: dragg(t5, x, y))
t6.ondrag(lambda x, y: dragg(t6, x, y))




