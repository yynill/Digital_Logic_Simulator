import pygame
from constants import *
from objects import *


def check_menu_switch_click(mouse_x, mouse_y):
    new_switch_type = None
    if 6*(SYMBOL_WIDTH+10) + 10 < mouse_x < (6*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        new_switch_type = 'SWITCH_OFF'

    if new_switch_type is not None:
        new_switch = Switch(len(objects), False,
                            switch_images[new_switch_type], mouse_x, mouse_y)
        global cable_mode
        cable_mode = False

        clicked_object = new_switch.id
        objects.append(new_switch)
        new_switch_type = None

        return clicked_object


def check_menu_light_click(mouse_x, mouse_y):
    new_light_type = None

    if 7*(SYMBOL_WIDTH+10) + 10 < mouse_x < (7*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        new_light_type = 'LIGHT_OFF'

    if new_light_type is not None:
        new_light = Light(len(objects), False,
                          light_images[new_light_type], mouse_x, mouse_y)

        global cable_mode
        cable_mode = False

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

        if new_gate_type is not None:

            num_inputs = 2
            if new_gate_type == 'NOT_GATE':
                num_inputs = 1

            new_gate = Gate(len(objects), new_gate_type,
                            gate_images[new_gate_type], mouse_x, mouse_y, num_inputs)

            clicked_object = new_gate.id
            objects.append(new_gate)
            new_gate_type = None

            global cable_mode
            cable_mode = False

            return clicked_object
        else:
            return None
