# from graphics import GraphWin, Rectangle, Point
# import time

# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = 400
# CELL_SIZE = 40
# ERASER_SIZE = 20

# def is_overlapping(eraser_coords, rect_coords):
#     """Check if eraser overlaps with a rectangle"""
#     er_left, er_top, er_right, er_bottom = eraser_coords
#     r_left, r_top, r_right, r_bottom = rect_coords
    
#     return not (
#         er_right < r_left or
#         er_left > r_right or
#         er_bottom < r_top or
#         er_top > r_bottom
#     )

# def get_coords(rect):
#     """Get rectangle coordinates as left, top, right, bottom"""
#     p1 = rect.getP1()
#     p2 = rect.getP2()
#     return (min(p1.getX(), p2.getX()), min(p1.getY(), p2.getY()),
#             max(p1.getX(), p2.getX()), max(p1.getY(), p2.getY()))

# def main():
#     win = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
#     win.setBackground('white')

#     # Store each cell and its fill status
#     cells = []

#     # Draw blue grid
#     for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
#         for col in range(0, CANVAS_WIDTH, CELL_SIZE):
#             rect = Rectangle(Point(col, row), Point(col + CELL_SIZE, row + CELL_SIZE))
#             rect.setFill('blue')
#             rect.draw(win)
#             cells.append((rect, 'blue'))  # Store cell with its fill color

#     # Wait for user to click to place eraser
#     win.getMouse()
#     click = win.getMouse()
#     click_x = click.getX()
#     click_y = click.getY()

#     # Create eraser (pink rectangle)
#     eraser = Rectangle(Point(click_x, click_y),
#                        Point(click_x + ERASER_SIZE, click_y + ERASER_SIZE))
#     eraser.setFill('pink')
#     eraser.draw(win)

#     # Start tracking mouse and erase cells
#     while True:
#         mouse = win.checkMouse()
#         if mouse:
#             # Move eraser to new position
#             center_x = (eraser.getP1().getX() + eraser.getP2().getX()) / 2
#             center_y = (eraser.getP1().getY() + eraser.getP2().getY()) / 2

#             dx = mouse.getX() - center_x
#             dy = mouse.getY() - center_y
#             eraser.move(dx, dy)

#             # Update eraser position
#             eraser_coords = get_coords(eraser)

#             # Check each cell for overlap
#             for i in range(len(cells)):
#                 cell, color = cells[i]
#                 if color == 'blue':
#                     cell_coords = get_coords(cell)
#                     if is_overlapping(eraser_coords, cell_coords):
#                         cell.setFill('white')
#                         cells[i] = (cell, 'white')  # Update fill color

#         time.sleep(0.05)  # Short delay for smooth movement

# if __name__ == '__main__':
#     main()


from graphics import GraphWin, Rectangle, Point, GraphicsError
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def is_overlapping(eraser_coords, rect_coords):
    """Check if eraser overlaps with a rectangle"""
    er_left, er_top, er_right, er_bottom = eraser_coords
    r_left, r_top, r_right, r_bottom = rect_coords
    
    return not (
        er_right < r_left or
        er_left > r_right or
        er_bottom < r_top or
        er_top > r_bottom
    )

def get_coords(rect):
    """Get rectangle coordinates as left, top, right, bottom"""
    p1 = rect.getP1()
    p2 = rect.getP2()
    return (min(p1.getX(), p2.getX()), min(p1.getY(), p2.getY()),
            max(p1.getX(), p2.getX()), max(p1.getY(), p2.getY()))

def main():
    win = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    win.setBackground('white')

    # Store each cell and its fill status
    cells = []

    # Draw blue grid
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = Rectangle(Point(col, row), Point(col + CELL_SIZE, row + CELL_SIZE))
            rect.setFill('blue')
            rect.draw(win)
            cells.append((rect, 'blue'))  # Store cell with its fill color

    # Wait for user to click to place eraser
    try:
        win.getMouse()
        click = win.getMouse()
    except GraphicsError:
        return  # Window was closed early

    click_x = click.getX()
    click_y = click.getY()

    # Create eraser (pink rectangle)
    eraser = Rectangle(Point(click_x, click_y),
                       Point(click_x + ERASER_SIZE, click_y + ERASER_SIZE))
    eraser.setFill('pink')
    eraser.draw(win)

    # Start tracking mouse and erase cells
    try:
        while True:
            mouse = win.checkMouse()
            if mouse:
                # Move eraser to new position
                center_x = (eraser.getP1().getX() + eraser.getP2().getX()) / 2
                center_y = (eraser.getP1().getY() + eraser.getP2().getY()) / 2

                dx = mouse.getX() - center_x
                dy = mouse.getY() - center_y
                eraser.move(dx, dy)

                # Update eraser position
                eraser_coords = get_coords(eraser)

                # Check each cell for overlap
                for i in range(len(cells)):
                    cell, color = cells[i]
                    if color == 'blue':
                        cell_coords = get_coords(cell)
                        if is_overlapping(eraser_coords, cell_coords):
                            cell.setFill('white')
                            cells[i] = (cell, 'white')  # Update fill color

            time.sleep(0.05)  # Short delay for smooth movement
    except GraphicsError:
        # Window was closed during loop
        pass

if __name__ == '__main__':
    main()
