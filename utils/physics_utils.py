import pymunk


def create_static_line(space, x1, y1, x2, y2):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (x1, y1), (x2, y2), 10)
    space.add(body, shape)
    return shape


def add_emojis_to_space(space, emojis_body, emojis, radius):
    for i, ball in enumerate(emojis_body):
        emojis_body[i].position = emojis[i]
        shape = pymunk.Circle(emojis_body[i], radius)
        space.add(emojis_body[i], shape)


def add_fingers_to_space(space, fingers, radius):
    for i, finger in enumerate(fingers):
        finger_shape = pymunk.Circle(fingers[i], radius)
        space.add(fingers[i], finger_shape)
