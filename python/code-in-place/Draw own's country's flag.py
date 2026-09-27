from graphics import Canvas

# Creating my country's flag
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!

    # Green rectangular size and position
    map_width = 200
    map_height = 100
    map_x = map_width - CANVAS_WIDTH / 2
    map_y = map_height - CANVAS_HEIGHT / 2

    # Red Circle size and position
    circle_width = map_width * .4

    canvas.create_rectangle(map_x, map_y, (map_width + map_x), (map_height + map_y), 'green')
    # canvas.create_oval(50, 20, 130, 100, 'red')


if __name__ == '__main__':
    main()