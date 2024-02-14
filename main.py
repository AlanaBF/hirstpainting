import colorgram
import random
import turtle as t

rgb_colors = []

colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

rgb_colors = [(249, 248, 247), (251, 248, 250), (241, 249, 245), (242, 245, 250), (239, 221, 113), (18, 111, 193),
              (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50), (212, 127, 164), (34, 194, 117),
              (139, 183, 18), (189, 18, 39), (108, 105, 194), (232, 55, 45), (244, 147, 183), (113, 191, 149),
              (191, 46, 66), (19, 187, 206), (45, 52, 105), (136, 221, 240), (146, 229, 169), (202, 210, 7),
              (22, 151, 116), (233, 174, 159), (31, 43, 76), (112, 42, 40), (181, 178, 220), (80, 34, 37)]


tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
tim.pensize(10)
# tim.shape("turtle")
tim.speed("fastest")


def draw_dot():
    tim.setheading(225)
    tim.penup()
    tim.fd(300)
    tim.setheading(0)
    tim.pendown()
    tim.color(random.choice(rgb_colors))
    tim.dot(20, random.choice(rgb_colors))  # Choose a random color from the extracted image colors
    # stamp_id = tim.stamp()


def draw_grid(rows, columns, spacing):
    for row in range(rows):
        for col in range(columns):
            x = col * spacing
            y = row * spacing
            tim.penup()
            tim.goto(x, y)
            tim.pendown()
            draw_dot()
            tim.hideturtle()


grid_rows = 10
grid_columns = 10
grid_spacing = 50

draw_grid(grid_rows, grid_columns, grid_spacing)


screen.exitonclick()
