from tkinter import Canvas

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUAR_SIZE = 100


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!

    # get the middle of the canvas
    middle_x = CANVAS_WIDTH / 2
    middle_y = CANVAS_HEIGHT / 2

    half_SQUAR_SIZE = SQUAR_SIZE / 2

    # calculate the top left of square
    left_x = middle_x - half_SQUAR_SIZE
    left_y = middle_y - half_SQUAR_SIZE
    print(left_x, left_y)

    # calculate the right bottom of the square

    right_x = middle_x + half_SQUAR_SIZE
    right_y = middle_y + half_SQUAR_SIZE
    print(right_x, right_y)

    # draw the square
    # canvas.create_rectangle(left_x, top_y, right_x, bottom_y)


if __name__ == '__main__':
    main()