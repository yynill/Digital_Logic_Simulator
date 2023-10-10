import pygame

# colors
BACKGROUND_COLOR = (150, 150, 150,)
WIRE_COLOR = (64, 64, 64)
WIRE_COLOR_ACTIVE = (102, 255, 102)

WIDTH, HEIGHT = 1350, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Digital Logic Simulator!')

FPS = 60

SYMBOL_WIDTH = 36
SYMBOL_HEIGHT = 55

LIGHT_WIDTH = 40
LIGHT_HEIGHT = 55

SWITCH_WIDTH = 33
SWITCH_HEIGHT = 55

# load images

AND_IMG = pygame.image.load('./ASSETS/AND.png')
AND_GATE = pygame.transform.scale(AND_IMG, (SYMBOL_WIDTH, SYMBOL_HEIGHT))

NOT_IMG = pygame.image.load('./ASSETS/NOT.png')
NOT_GATE = pygame.transform.scale(NOT_IMG, (SYMBOL_WIDTH, SYMBOL_HEIGHT))

OR_IMG = pygame.image.load('./ASSETS/OR.png')
OR_GATE = pygame.transform.scale(OR_IMG, (SYMBOL_WIDTH, SYMBOL_HEIGHT))

NAND_IMG = pygame.image.load('./ASSETS/NAND.png')
NAND_GATE = pygame.transform.scale(NAND_IMG, (SYMBOL_WIDTH, SYMBOL_HEIGHT))

NOR_IMG = pygame.image.load('./ASSETS/NOR.png')
NOR_GATE = pygame.transform.scale(NOR_IMG, (SYMBOL_WIDTH, SYMBOL_HEIGHT))


SWITCH_OFF_IMG = pygame.image.load('./ASSETS/SWITCH_OFF.png')
SWITCH_OFF = pygame.transform.scale(
    SWITCH_OFF_IMG, (SWITCH_WIDTH, SWITCH_HEIGHT))

SWITCH_ON_IMG = pygame.image.load('./ASSETS/SWITCH_ON.png')
SWITCH_ON = pygame.transform.scale(
    SWITCH_ON_IMG, (SWITCH_WIDTH, SWITCH_HEIGHT))

LIGHT_OFF_IMG = pygame.image.load('./ASSETS/LIGHT_OFF.png')
LIGHT_OFF = pygame.transform.scale(
    LIGHT_OFF_IMG, (LIGHT_WIDTH, LIGHT_HEIGHT))

LIGHT_ON_IMG = pygame.image.load('./ASSETS/LIGHT_ON.png')
LIGHT_ON = pygame.transform.scale(
    LIGHT_ON_IMG, (LIGHT_WIDTH, LIGHT_HEIGHT))

CABLE_IMG = pygame.image.load('./ASSETS/CABLE.png')
CABLE = pygame.transform.scale(
    CABLE_IMG, (SWITCH_WIDTH, SWITCH_HEIGHT))

cable_mode = False


class DrawableObject:
    def __init__(self, _id, image, x, y):
        self.id = _id
        self.image = image
        self.x = x
        self.y = y


class Gate(DrawableObject):
    def __init__(self, _id, gate_type, image, x, y):
        super().__init__(_id, image, x, y)
        self.gate_type = gate_type
        # self.inputs = []  #  input connections
        # self.outputs = []  #  output connections

    def update(self):
        #  logic to compute outputs based on inputs
        pass


class Switch(DrawableObject):
    def __init__(self, _id, switch_state, image, x, y):
        super().__init__(_id, image, x, y)
        self.switch_state = switch_state  # True for on, False for off


class Light(DrawableObject):
    def __init__(self, _id, light_state, image, x, y):
        super().__init__(_id, image, x, y)
        self.light_state = light_state  # True for on, False for off


gate_images = {
    'AND_GATE': AND_GATE,
    'NOT_GATE': NOT_GATE,
    'OR_GATE': OR_GATE,
    'NAND_GATE': NAND_GATE,
    'NOR_GATE': NOR_GATE
}

switch_images = {
    'SWITCH_ON': SWITCH_ON,
    'SWITCH_OFF': SWITCH_OFF,
}

light_images = {
    'LIGHT_ON': LIGHT_ON,
    'LIGHT_OFF': LIGHT_OFF
}

clicked_object = None
objects = []


def check_cable_click(mouse_x, mouse_y):
    global cable_mode
    if 9*(SYMBOL_WIDTH+10) + 10 < mouse_x < (9*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        cable_mode = not cable_mode  # toggle cable mode
        return True


def check_menu_switch_click(mouse_x, mouse_y):
    new_switch_type = None
    if 6*(SYMBOL_WIDTH+10) + 10 < mouse_x < (6*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        new_switch_type = 'SWITCH_OFF'

    print(new_switch_type)
    if new_switch_type is not None:
        new_switch = Switch(len(objects), new_switch_type,
                            switch_images[new_switch_type], mouse_x, mouse_y)

        clicked_object = new_switch.id
        objects.append(new_switch)
        new_switch_type = None
        return clicked_object


def check_menu_light_click(mouse_x, mouse_y):
    new_light_type = None
    if 7*(SYMBOL_WIDTH+10) + 10 < mouse_x < (7*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        new_light_type = 'LIGHT_OFF'

    print(new_light_type)
    if new_light_type is not None:
        new_light = Light(len(objects), new_light_type,
                          light_images[new_light_type], mouse_x, mouse_y)

        clicked_object = new_light.id
        objects.append(new_light)
        new_light_type = None
        return clicked_object


def check_menu_gate_click(mouse_x, mouse_y):
    if 0 < mouse_y < 10+SYMBOL_HEIGHT+10:
        new_gate_type = None
        # AND-GATE
        if 0*(SYMBOL_WIDTH+10) + 10 < mouse_x < (0*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            new_gate_type = 'AND_GATE'
        # NOT-GATE
        if 1*(SYMBOL_WIDTH+10) + 10 < mouse_x < (1*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            new_gate_type = 'NOT_GATE'
        # OR-GATE
        if 2*(SYMBOL_WIDTH+10) + 10 < mouse_x < (2*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            new_gate_type = 'OR_GATE'
        # NAND-GATE
        if 3*(SYMBOL_WIDTH+10) + 10 < mouse_x < (3*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            new_gate_type = 'NAND_GATE'
        # NOR-GATE
        if 4*(SYMBOL_WIDTH+10) + 10 < mouse_x < (4*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            new_gate_type = 'NOR_GATE'

        print(new_gate_type)
        if new_gate_type is not None:
            new_gate = Gate(len(objects), new_gate_type,
                            gate_images[new_gate_type], mouse_x, mouse_y)

            clicked_object = new_gate.id
            objects.append(new_gate)
            new_gate_type = None
            return clicked_object
        else:
            return None


def drag_screen(mouse_x, mouse_y, objects):
    pass
    # select all objects and wires and move all in the mocing position and amount from mouse
    # think about zoom in and out


def get_obj_by_position(mouse_x, mouse_y, objects):
    for obj in objects:
        if obj.x < mouse_x < obj.x + SYMBOL_WIDTH and obj.y < mouse_y < obj.y + SYMBOL_HEIGHT:
            return get_obj_by_id(obj.id)


def get_obj_by_id(obj_id):
    for obj in objects:
        if obj.id == obj_id:
            return obj
    return None


def right_click_menu(mouse_x, mouse_y, this_objects):
    pass
    # obj id, objects type,
    # show gate connections and signals,
    # show gate inout output table,
    # show ecplanation,
    # delete gate button
    # same with lamp and switches


def draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg):
    window.fill(BACKGROUND_COLOR)

    for obj in objects:
        window.blit(obj.image, (obj.x, obj.y))
    window.blit(menu_bar, (0, 0))

    window.blit(AND_GATE, (and_gate_btn.x, and_gate_btn.y))
    window.blit(NOT_GATE, (not_gate_btn.x, not_gate_btn.y))
    window.blit(OR_GATE, (or_gate_btn.x, or_gate_btn.y))
    window.blit(NAND_GATE, (nand_gate_btn.x, nand_gate_btn.y))
    window.blit(NOR_GATE, (nor_gate_btn.x, nor_gate_btn.y))

    window.blit(SWITCH_OFF, (switch_off_btn.x, switch_off_btn.y))
    window.blit(LIGHT_OFF, (light_off_btn.x, light_off_btn.y))

    if cable_mode == True:
        window.blit(cable_bg, (cable_btn.x - 5, 5))

    window.blit(CABLE, (cable_btn.x, cable_btn.y))

    pygame.display.update()


def main():
    global dragging_object
    dragging_object = None

    menu_bar = pygame.Surface((WIDTH, 10+SYMBOL_HEIGHT+10))
    menu_bar.fill((128, 128, 128))

    cable_bg = pygame.Surface((SYMBOL_WIDTH+10, 10+SYMBOL_HEIGHT))
    cable_bg.fill((85, 85, 85))

    and_gate_btn = pygame.Rect(
        0*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)
    not_gate_btn = pygame.Rect(
        1*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)
    or_gate_btn = pygame.Rect(
        2*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)
    nand_gate_btn = pygame.Rect(
        3*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)
    nor_gate_btn = pygame.Rect(
        4*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)

    switch_off_btn = pygame.Rect(
        6*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)
    light_off_btn = pygame.Rect(
        7*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)

    cable_btn = pygame.Rect(
        9*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT)

    clock = pygame.time.Clock()
    # gameloop
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # left click
            clicked_object_id = None

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:  # left mouse (button 1)
                    mouse_x, mouse_y = event.pos

                    clicked_object_id = check_menu_gate_click(mouse_x, mouse_y)

                    if clicked_object_id is None:
                        clicked_object_id = check_menu_switch_click(
                            mouse_x, mouse_y)

                        if clicked_object_id is None:
                            clicked_object_id = check_menu_light_click(
                                mouse_x, mouse_y)

                            if clicked_object_id is None:
                                cable_mode = check_cable_click(
                                    mouse_x, mouse_y)

                    if clicked_object_id is not None:
                        dragging_object = get_obj_by_id(clicked_object_id)

                    elif clicked_object_id is None:
                        dragging_object = get_obj_by_position(
                            mouse_x, mouse_y, objects)

            # drag mouse
            if event.type == pygame.MOUSEMOTION:
                if dragging_object != None:
                    mouse_x, mouse_y = event.pos
                    dragging_object.x = mouse_x - SYMBOL_WIDTH // 2
                    dragging_object.y = mouse_y - SYMBOL_HEIGHT // 2
                else:
                    pass

            # release obj
            if event.type == pygame.MOUSEBUTTONUP and dragging_object is not None:
                if event.button == 1:
                    if dragging_object.y > SYMBOL_HEIGHT:
                        dragging_object = None
                else:
                    objects.remove(dragging_object)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right click
                    mouse_x, mouse_y = event.pos
                    this_obj = get_obj_by_position(mouse_x, mouse_y, objects)
                    right_click_menu(mouse_x, mouse_y, this_obj)

            # middle mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    drag_screen(mouse_x, mouse_y, objects)

        draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                    nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg)

    pygame.quit()


if __name__ == '__main__':
    main()
