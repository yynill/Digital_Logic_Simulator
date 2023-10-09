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

LIGHT_OFF_IMG = pygame.image.load('./ASSETS/LIGHT_OFF.png')
LIGHT_OFF = pygame.transform.scale(
    LIGHT_OFF_IMG, (LIGHT_WIDTH, LIGHT_HEIGHT))

# make IMG sharper by Screen shot of original zoomed in

gate_images = {
    'AND_GATE': AND_GATE,
    'NOT_GATE': NOT_GATE,
    'OR_GATE': OR_GATE,
    'NAND_GATE': NAND_GATE,
    'NOR_GATE': NOR_GATE
}

clicked_gate = None
gates = []


class Gate:
    def __init__(self, _id, gate_type, image, x, y):
        self.id = _id
        self.gate_type = gate_type
        self.image = image
        self.x = x
        self.y = y


def check_menu_click(mouse_x, mouse_y):
    if 0 < mouse_y < 10+SYMBOL_HEIGHT+10:
        # AND-GATE
        new_gate_type = None
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
            new_gate = Gate(len(gates), new_gate_type,
                            gate_images[new_gate_type], mouse_x, mouse_y)

            clicked_gate = new_gate.id
            gates.append(new_gate)
            new_gate_type = None
            return clicked_gate


def drag_screen(mouse_x, mouse_y, gates):
    pass
    # select all gates and wires and move all in the mocing position and amount from mouse
    # think about zoom in and out


def get_gate_by_position(mouse_x, mouse_y, gates):
    for gate in gates:
        if gate.x < mouse_x < gate.x + SYMBOL_WIDTH and gate.y < mouse_y < gate.y + SYMBOL_HEIGHT:
            return get_gate_by_id(gate.id)


def get_gate_by_id(gate_id):
    for gate in gates:
        if gate.id == gate_id:
            return gate
    return None


def right_click_menu(mouse_x, mouse_y, this_gate):
    pass
    # gate id, gate type,
    # show gate connections and signals,
    # show gate inout output table,
    # show ecplanation,
    # delete gate button


def draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                nand_gate_btn, nor_gate_btn, gates, switch_off_btn, light_off_btn):
    window.fill(BACKGROUND_COLOR)

    for gate in gates:
        window.blit(gate.image, (gate.x, gate.y))
    window.blit(menu_bar, (0, 0))

    window.blit(AND_GATE, (and_gate_btn.x, and_gate_btn.y))
    window.blit(NOT_GATE, (not_gate_btn.x, not_gate_btn.y))
    window.blit(OR_GATE, (or_gate_btn.x, or_gate_btn.y))
    window.blit(NAND_GATE, (nand_gate_btn.x, nand_gate_btn.y))
    window.blit(NOR_GATE, (nor_gate_btn.x, nor_gate_btn.y))

    window.blit(SWITCH_OFF, (switch_off_btn.x, switch_off_btn.y))
    window.blit(LIGHT_OFF, (light_off_btn.x, light_off_btn.y))

    pygame.display.update()


def main():
    global dragging_gate
    dragging_gate = None

    menu_bar = pygame.Surface((WIDTH, 10+SYMBOL_HEIGHT+10))
    menu_bar.fill((128, 128, 128))

    menu_seperator = pygame.Surface((5, 10+SYMBOL_HEIGHT+10))
    menu_seperator.fill((85, 85, 85))

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

    clock = pygame.time.Clock()
    # gameloop
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse (button 1)
                    mouse_x, mouse_y = event.pos

                    clicked_gate_id = check_menu_click(mouse_x, mouse_y)
                    if clicked_gate_id is not None:
                        dragging_gate = get_gate_by_id(clicked_gate_id)
                    elif clicked_gate_id is None:
                        dragging_gate = get_gate_by_position(
                            mouse_x, mouse_y, gates)

            # drag mouse
            if event.type == pygame.MOUSEMOTION:
                if dragging_gate != None:
                    mouse_x, mouse_y = event.pos
                    dragging_gate.x = mouse_x - SYMBOL_WIDTH // 2
                    dragging_gate.y = mouse_y - SYMBOL_HEIGHT // 2
                else:
                    pass

            # release gate
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and dragging_gate is not None:
                    if dragging_gate.y > SYMBOL_HEIGHT:
                        # Release the gate by setting dragging_gate to None
                        dragging_gate = None
                else:
                    gates.remove(dragging_gate)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right click
                    mouse_x, mouse_y = event.pos
                    this_gate = get_gate_by_position(mouse_x, mouse_y, gates)
                    right_click_menu(mouse_x, mouse_y, this_gate)

            # middle mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    drag_screen(mouse_x, mouse_y, gates)

        draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                    nand_gate_btn, nor_gate_btn, gates, switch_off_btn, light_off_btn)

    pygame.quit()


if __name__ == '__main__':
    main()
