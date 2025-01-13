from turtle import*
#we want to paint a house

#step one draw a square
speed(40)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)\

forward(200)
left(90)

forward(200)
left(90)
#end of square 




#drawing a door
 
forward(70)
color("blue") 
begin_fill()
left(90)
forward(120)   
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()



color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
 
penup()
goto(20,180)
pendown()
left(30)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(20)
left(90)
forward(40)

left(90)
forward(20) 

left(90)
forward(20)

left(90)
forward(40)

penup()
goto(140,180)
pendown()

forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(20)
left(90)
forward(40)

left(90)
forward(20) 

left(90)
forward(20)

left(90)
forward(40)




exitonclick()