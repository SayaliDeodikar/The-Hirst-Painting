# import colorgram
# color_val = colorgram.extract('hirst.jpg', 32)
# colors = []
# for color in color_val:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors.append(new_color)
# print(colors)
# print(len(colors))

colors = [
          (239, 236, 238), (238, 237, 236), (237, 237, 241), (25, 108, 164), (194, 38, 81), 
          (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), 
          (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), 
          (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), 
          (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), 
          (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)]


import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.goto(-200,-200)
for i in range(10):
    for j in range(10):
        tim.pencolor(random.choice(colors))
        tim.dot(15)
        tim.penup()
        tim.forward(40)
    tim.left(90)
    tim.forward(40) 
    tim.left(90)      
    tim.forward(400)
    tim.left(180)
        
        
  
screen = t.Screen()
screen.exitonclick()
  