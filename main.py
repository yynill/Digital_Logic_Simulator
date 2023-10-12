import pygame
from constants import *
from objects import *
from menu import *
from functions import *


def check_cable_click(mouse_x, mouse_y):
    global cable_mode
    if 9*(SYMBOL_WIDTH+10) + 10 < mouse_x < (9*(SYMBOL_WIDTH+10) + 10) + SYMBOL_WIDTH and mouse_y < SYMBOL_HEIGHT:
        cable_mode = not cable_mode  # toggle cable mode
        print(cable_mode)


def create_right_click_menu(this_obj):
    pass
    # obj id, objects type,
    # show gate connections and signals,
    # show gate inout output table,
    # show ecplanation,
    # delete gate button
    # same with lamp and switches


def draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg, line_start, line_end):
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

    for cable in cables:
        start_obj = get_obj_by_id(cable.obj_connection_1)
        end_obj = get_obj_by_id(cable.obj_connection_2)

        if start_obj and end_obj:
            start = (start_obj.x + SYMBOL_WIDTH // 2,
                     start_obj.y + SYMBOL_HEIGHT // 2)
            end = (end_obj.x + SYMBOL_WIDTH // 2,
                   end_obj.y + SYMBOL_HEIGHT // 2)

            if cable.state == True:
                pygame.draw.line(window, WIRE_COLOR_ACTIVE, start, end, 3)
            elif cable.state == False:
                pygame.draw.line(window, WIRE_COLOR, start, end, 3)

    if line_start is not None and line_end is not None:
        pygame.draw.line(window, WIRE_COLOR, line_start, line_end, 3)

    window.blit(CABLE, (cable_btn.x, cable_btn.y))

    pygame.display.update()


def main():
    print(pygame.display.list_modes())
    global cable_mode

    global dragging_object
    dragging_object = None

    global panning
    panning = False

    last_click_time = 0

    right_click_menu = None
    right_click_menu_visible = False  # Menu visibility flag

    menu_bar = pygame.Surface((WIDTH, 10+SYMBOL_HEIGHT+10))
    menu_bar.fill((128, 128, 128))

    cable_bg = pygame.Surface((SYMBOL_WIDTH+10, 10+SYMBOL_HEIGHT))
    cable_bg.fill((85, 85, 85))

    and_gate_btn = pygame.Rect(
        0*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)
    not_gate_btn = pygame.Rect(
        1*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)
    or_gate_btn = pygame.Rect(
        2*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)
    nand_gate_btn = pygame.Rect(
        3*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)
    nor_gate_btn = pygame.Rect(
        4*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)

    switch_off_btn = pygame.Rect(
        6*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)
    light_off_btn = pygame.Rect(
        7*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)

    cable_btn = pygame.Rect(
        9*(SYMBOL_WIDTH+10) + 10, 10, SYMBOL_WIDTH, SYMBOL_HEIGHT + 20)

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
                                check_cable_click(mouse_x, mouse_y)

                    if clicked_object_id is not None:
                        dragging_object = get_obj_by_id(clicked_object_id)

                    elif clicked_object_id is None:
                        dragging_object = get_obj_by_position(
                            mouse_x, mouse_y, objects)

                    current_time = pygame.time.get_ticks() / 1000  # Convert to seconds

                    # double click
                    if current_time - last_click_time <= DOUBLE_CLICK_TIME_THRESHOLD:
                        mouse_x, mouse_y = event.pos
                        double_clicked_object = get_obj_by_position(
                            mouse_x, mouse_y, objects)

                        double_clicked_object.print_cables()

                        if hasattr(double_clicked_object, "switch"):
                            toggleSwitch(double_clicked_object)

                        else:
                            pass
                    last_click_time = current_time

            # drag mouse
            if event.type == pygame.MOUSEMOTION and cable_mode == False:
                if dragging_object != None:
                    mouse_x, mouse_y = event.pos
                    dragging_object.x = mouse_x - SYMBOL_WIDTH // 2
                    dragging_object.y = mouse_y - SYMBOL_HEIGHT // 2

            # release obj
            if event.type == pygame.MOUSEBUTTONUP and dragging_object is not None:
                if event.button == 1:
                    if dragging_object.y > SYMBOL_HEIGHT:
                        dragging_object = None
                else:
                    objects.remove(dragging_object)

            # Cable mode on
            if event.type == pygame.MOUSEBUTTONDOWN and cable_mode:
                global line_start
                x, y = event.pos
                if line_start is None and y > SYMBOL_HEIGHT:
                    line_start = event.pos

            if event.type == pygame.MOUSEMOTION and cable_mode:
                global line_end
                if line_start is not None:
                    line_end = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and cable_mode and line_start is not None:
                    try:
                        c1, c2 = line_start
                        c3, c4 = line_end

                        obj_connection_1 = get_obj_by_position(c1, c2, objects)
                        obj_connection_2 = get_obj_by_position(c3, c4, objects)

                        if (isinstance(obj_connection_1, Switch) and isinstance(obj_connection_2, Switch)) or (isinstance(obj_connection_1, Light) and isinstance(obj_connection_2, Light)):
                            line_start = None
                            line_end = None
                        # problematic, because than cant attach ouput cable
                        # elif (isinstance(obj_connection_1, Gate) and len(obj_connection_1.input_cables) > 2) or (isinstance(obj_connection_2, Gate) and len(obj_connection_2.input_cables) > 2):
                        #     line_start = None
                        #     line_end = None
                        else:
                            print(
                                f'Connections: {obj_connection_1.id}/{obj_connection_2.id}')

                            new_cable = Cable(
                                len(cables), obj_connection_1.id, obj_connection_2.id, False)
                            cables.append(new_cable)

                            connect_cable(obj_connection_1.id,
                                          obj_connection_2.id, False)

                            print('cable created')

                            line_start = None
                            line_end = None

                    except Exception as e:
                        line_start = None
                        line_end = None

                elif event.button == 2:
                    panning = False

            # right click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right click
                    mouse_x, mouse_y = event.pos
                    this_obj = get_obj_by_position(mouse_x, mouse_y, objects)
                    right_click_menu = create_right_click_menu(this_obj)
                    right_click_menu_visible = True
                elif event.button == 2:
                    cable_mode = False
                    panning = True

            # middle mouse
            if event.type == pygame.MOUSEMOTION and panning == True:
                print(event.rel)
                drag_screen(event.rel, objects)

        draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                    nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg, line_start, line_end)

    pygame.quit()


if __name__ == '__main__':
    main()
