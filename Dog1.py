import turtle,time
wn=turtle.Screen()
wn.setup(1300,700)
wn.bgpic('road.gif')
t=turtle.Turtle()
t.up()
image=['dog0.gif','dog1.gif','dog2.gif','dog3.gif','dog4.gif',\
       'dog5.gif','dog6.gif','dog7.gif','dog8.gif','dog9.gif']
for i in range(10):
    wn.addshape(image[i])

t.hideturtle
t.goto(-350,-30)
t.showturtle()

for i in range (100):
    for j in range(10):
        time.sleep(0.1)
        t.shape(image[j])
        t.fd(5)

    
    

