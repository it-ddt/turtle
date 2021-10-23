import turtle as t
from PIL import ImageGrab


def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#000000", walls_width = 20, walls_height = 20, walls_fill = "#000000", roof_width = 0, roof_height = 0, roof_fill = "#000000", door_fill = "red"):
    """
        base_x — X левого нижнего угла фундамента
        base_y — Y левого нижнего угла фундамента
        base_width — ширина фундамента
        base_height — высота фундамента
        base_fill — цвет заливки фундамента

        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - считаем автоматически
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика

        door_x - сичтаем автоматически, (walls_width - door_width) / 2
        door_y - счиатаем автоматически, base_y + base_height
        door_width - ширина двери, стандарт
        door_height - высота двери, стандарт
        door_fill - цвет двери, спрашиваем у заказчика

        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - считаем автоматически, 120% ширины крыши
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """

    # забираем размер экрана пользователя
    img = ImageGrab.grab()
    screen_width = img.size[0]
    screen_height = img.size[1]

    print(screen_width)
    print(screen_height)

    # назначаем черепахе размер экрана
    ts = t.getscreen()
    ts.screensize(screen_width, screen_height)

    # скорость строительства
    t.speed(0)

    # считаем автоматические величины
    walls_x = base_x
    walls_y = base_y + base_height
    walls_width = base_width
    door_width = 50
    door_height = 100
    door_x = walls_x + ((walls_width - door_width) / 2)
    door_y = base_y + base_height
    roof_x = walls_x - (walls_width * 0.1)
    roof_y = base_height + walls_height
    roof_width = walls_width * 1.2


    def build_base(base_x, base_y, base_width, base_height, base_fill):
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.fillcolor(base_fill)
        t.pendown()
        t.begin_fill()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.end_fill()


    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        t.penup()
        t.goto(walls_x, walls_y)
        t.setheading(0)
        t.fillcolor(walls_fill)
        t.pendown()
        t.begin_fill()
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.end_fill()

    def build_door(door_x, door_y, door_width, door_height, door_fill):
        t.penup()
        t.goto(door_x, door_y)
        t.setheading(0)
        t.fillcolor(door_fill)
        t.pendown()
        t.begin_fill()
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.end_fill()


    def build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill):
        t.penup()
        t.goto(roof_x, roof_y)
        t.setheading(0)
        t.fillcolor(roof_fill)
        t.pendown()
        t.begin_fill()
        t.forward(roof_width)
        t.goto(walls_width / 2, base_height + walls_height + roof_height)
        t.goto(roof_x, roof_y)
        t.end_fill()


    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill)
    build_door(door_x, door_y, door_width, door_height, door_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill)


build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#660000", walls_height = 150, walls_fill = "#FF9999", roof_height = 100, roof_fill = "green", door_fill = "#000000")
t.done()
