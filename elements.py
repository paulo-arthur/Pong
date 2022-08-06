import math

def bar(WIDTH, HEIGHT, x):
    return {
    'length': 100,
    'weight': 7,
    'x': x,
    'y': HEIGHT/2
    }

def ball(WIDTH, HEIGHT):
    return {
    'radius': 10,
    'x': WIDTH/2,
    'y': HEIGHT/2,
    'speed': [0.6, 0]
    }


def collision(rect_left, rect_top, width, height, center_x, center_y, radius):

    rect_right, rect_bottom = rect_left + width/2, rect_top + height/2

    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    if rect_right < cleft or rect_left > cright or rect_bottom < ctop or rect_top > cbottom:
        return False

    for x in (rect_left, rect_left+width):
        for y in (rect_top, rect_top+height):
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True

    if rect_left <= center_x <= rect_right and rect_top <= center_y <= rect_bottom:
        return True

    return False
