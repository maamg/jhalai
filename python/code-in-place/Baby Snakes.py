from graphics import GraphWin, Point, Rectangle
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
MOVE_AMOUNT = 10
DELAY = 0.1


def main():
    win = GraphWin("Game Window", CANVAS_WIDTH, CANVAS_HEIGHT)

    blue_square = Rectangle(Point(0, 0), Point(SIZE, SIZE))
    blue_square.setFill('blue')
    blue_square.draw(win)

    last_key = None

    while True:
        key = win.checkKey()

        if key != "":
            last_key = key

        if last_key == "Right":
            blue_square.move(MOVE_AMOUNT, 0)
        elif last_key == "Down":
            blue_square.move(0, MOVE_AMOUNT)
        elif last_key == "Left":
            blue_square.move(-MOVE_AMOUNT, 0)
        elif last_key == "Up":
            blue_square.move(0, -MOVE_AMOUNT)

        time.sleep(DELAY)
        win.update()


if __name__ == '__main__':
    main()
