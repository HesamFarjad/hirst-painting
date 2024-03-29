# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for i in colors:
#     # rgb_colors.appen(i.rgb)
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import random
import turtle

turtle.colormode(255)
color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
tim = turtle.Turtle()
tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()


for _ in range(10):
    for num in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)






turtle.exitonclick()














