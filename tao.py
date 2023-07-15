import turtle #แพ็คเกจเต่าวาดรูป
import random #ฟังชั่นแรมดอม

tao = turtle.Pen() #เต่า
tao.shape('turtle')
tao.pensize(3)
def siliam():
    # function
    size = random.randint(50,100)
    # for loop
    for i in range(4):
        tao.forward(size)
        tao.left(90)


for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    tao.up()
    tao.goto(x,y)
    tao.down()
    # list
    color = ['red','green','blue','yellow']
    select = random.choice(color)
    tao.color(select)
    siliam()


