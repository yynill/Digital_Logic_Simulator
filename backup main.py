import pygame


# colors
BACKGROUND_COLOR = (100, 100, 100,)
WIRE_COLOR = (64, 64, 64)
WIRE_COLOR_ACTIVE = (102, 255, 102)

WIDTH, HEIGHT = 1350, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Digital Logic Simulator!')

FPS = 60

SYMBOL_WIDTH = 24*1.3
SYMBOL_HEIGHT = 37*1.3

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


def delete_gate_by_id(gate_id):
    for gate in gates:
        if gate.id == gate_id:
            gates.remove(gate)


def check_menu_click(mouse_x, mouse_y):
    if 0 < mouse_y < 10+SYMBOL_HEIGHT+10:
        # AND-GATE
        if 0*(SYMBOL_WIDTH+10) + 10 < mouse_x < (0*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            return 'AND_GATE'
        # NOT-GATE
        if 1*(SYMBOL_WIDTH+10) + 10 < mouse_x < (1*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            return 'NOT_GATE'
        # OR-GATE
        if 2*(SYMBOL_WIDTH+10) + 10 < mouse_x < (2*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            return 'OR_GATE'
        # NAND-GATE
        if 3*(SYMBOL_WIDTH+10) + 10 < mouse_x < (3*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            return 'NAND_GATE'
        # NOR-GATE
        if 4*(SYMBOL_WIDTH+10) + 10 < mouse_x < (4*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH:
            return 'NOR_GATE'


def draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                nand_gate_btn, nor_gate_btn, gates):
    window.fill(BACKGROUND_COLOR)

    window.blit(menu_bar, (0, 0))
    window.blit(AND_GATE, (and_gate_btn.x, and_gate_btn.y))
    window.blit(NOT_GATE, (not_gate_btn.x, not_gate_btn.y))
    window.blit(OR_GATE, (or_gate_btn.x, or_gate_btn.y))
    window.blit(NAND_GATE, (nand_gate_btn.x, nand_gate_btn.y))
    window.blit(NOR_GATE, (nor_gate_btn.x, nor_gate_btn.y))

    for gate in gates:
        window.blit(gate.image, (gate.x, gate.y))
    pygame.display.update()


def main():
    program_state = "create"
    # create
    # drag
    # move (screen)

    menu_bar = pygame.Surface(((SYMBOL_WIDTH+10)*5+10, 10+SYMBOL_HEIGHT+10))
    menu_bar.fill((128, 128, 128))
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

    clock = pygame.time.Clock()
    # gameloop
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse (button 1)
                    mouse_x, mouse_y = event.pos

                    new_gate_type = check_menu_click(mouse_x, mouse_y)
                    print(new_gate_type)

                    if new_gate_type is not None:
                        new_gate = Gate(len(gates), new_gate_type,
                                        gate_images[new_gate_type], mouse_x, mouse_y)

                        gates.append(new_gate)
                        new_gate_type = None

                        # clicked_gate = new_gate

        draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                    nand_gate_btn, nor_gate_btn, gates)

    pygame.quit()


if __name__ == '__main__':
    main()
