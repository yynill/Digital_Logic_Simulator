import pygame

BACKGROUND_COLOR = (150, 150, 150,)
WIRE_COLOR = (64, 64, 64)
WIRE_COLOR_ACTIVE = (102, 255, 102)

WIDTH, HEIGHT = 1350, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Digital Logic Simulator!')

FPS = 60
DOUBLE_CLICK_TIME_THRESHOLD = 0.3

SYMBOL_WIDTH = 36
SYMBOL_HEIGHT = 55

LIGHT_WIDTH = 40
LIGHT_HEIGHT = 55

SWITCH_WIDTH = 33
SWITCH_HEIGHT = 55

INPUT_REGION_WIDTH = SYMBOL_WIDTH//2

INPUT_REGION_HEIGHT = SYMBOL_HEIGHT//2
OUTPUT_REGION_HEIGHT = SYMBOL_HEIGHT//2

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

gate_images = {
    'AND_GATE': AND_GATE,
    'NOT_GATE': NOT_GATE,
    'OR_GATE': OR_GATE,
    'NAND_GATE': NAND_GATE,
    'NOR_GATE': NOR_GATE
}

pin_points = {
    'AND_GATE': [(18, 0, 'output'), (9, 55, 'input'), (27, 55, 'input')],
    'OR_GATE': [(18, 0, 'output'), (9, 55, 'input'), (27, 55, 'input')],
    'NAND_GATE': [(18, 0, 'output'), (9, 55, 'input'), (27, 55, 'input')],
    'NOR_GATE': [(18, 0, 'output'), (9, 55, 'input'), (27, 55, 'input')],
    'NOT_GATE': [(18, 0, 'output'), (18, 55, 'input')],

    'SWITCH': [(SWITCH_WIDTH//2, 0, 'output')],

    'LIGHT': [(LIGHT_WIDTH//2, LIGHT_HEIGHT, 'input')],
}

switch_images = {
    'SWITCH_ON': SWITCH_ON,
    'SWITCH_OFF': SWITCH_OFF,
}

light_images = {
    'LIGHT_ON': LIGHT_ON,
    'LIGHT_OFF': LIGHT_OFF
}

cable_mode = False
line_start = None
line_end = None
cables = []

clicked_object = None
objects = []
