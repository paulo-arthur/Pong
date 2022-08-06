import math, random

def bar(WIDTH, HEIGHT, x):
    return {
    'length': 70,
    'weight': 5,
    'x': x,
    'y': HEIGHT/2
    }

def ball(WIDTH, HEIGHT):
    return {
    'radius': 10,
    'x': WIDTH/2,
    'y': HEIGHT/2,
    'speed': [0.4, random.randint(2, 5)/10],
    'xlr8': 0.00001
    }


def collision(rleft, rtop, width, height, center_x, center_y, radius):

    rright, rbottom = rleft + width, rtop + height

    cleft, ctop     = center_x - radius, center_y - radius
    cright, cbottom = center_x + radius, center_y + radius

    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False

    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            if math.hypot(x-center_x, y - center_y) <= radius:
                return True

    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True

    return False
