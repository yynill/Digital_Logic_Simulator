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


def draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg, line_start, line_end):
    window.fill(BACKGROUND_COLOR)

    for obj in objects:
        window.blit(obj.image, (obj.x, obj.y))

        if isinstance(obj, Light):
            obj.update()

        if isinstance(obj, Gate):
            obj.update()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for obj_type, pin_attributes in pin_points.items():
            if isinstance(obj, Gate):
                this_gate_type = obj.get_gate_type()  # Get the gate type
                if obj_type == this_gate_type:
                    for pin_x, pin_y, pin_type in pin_attributes:
                        if is_near_pin(mouse_x, mouse_y, obj.x + pin_x, obj.y + pin_y):
                            pygame.draw.circle(
                                window, (255, 0, 0), (obj.x + pin_x, obj.y + pin_y), 5)

            elif isinstance(obj, Switch):
                if obj_type == 'SWITCH':
                    for pin_x, pin_y, pin_type in pin_attributes:
                        if is_near_pin(mouse_x, mouse_y, obj.x + pin_x, obj.y + pin_y):
                            pygame.draw.circle(
                                window, (255, 0, 0), (obj.x + pin_x, obj.y + pin_y), 5)

            elif isinstance(obj, Light):
                if obj_type == 'LIGHT':
                    for pin_x, pin_y, pin_type in pin_attributes:
                        if is_near_pin(mouse_x, mouse_y, obj.x + pin_x, obj.y + pin_y):
                            pygame.draw.circle(
                                window, (255, 0, 0), (obj.x + pin_x, obj.y + pin_y), 5)

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

    if line_start is not None and line_end is not None:
        pygame.draw.line(window, WIRE_COLOR, line_start, line_end, 3)
    else:
        pass

    for cable in cables:
        if cable.state == True:
            pygame.draw.line(window, WIRE_COLOR_ACTIVE,
                             cable.pin1, cable.pin2, 3)
        else:
            pygame.draw.line(window, WIRE_COLOR,
                             cable.pin1, cable.pin2, 3)

    window.blit(CABLE, (cable_btn.x, cable_btn.y))

    pygame.display.update()


def main():
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
                        try:
                            double_clicked_object = get_obj_by_position(
                                mouse_x, mouse_y, objects)

                            double_clicked_object.print_cables()

                            if hasattr(double_clicked_object, "switch"):
                                toggleSwitch(double_clicked_object)
                        except:
                            pass

                    last_click_time = current_time

            # drag mouse
            if event.type == pygame.MOUSEMOTION and cable_mode == False:
                if dragging_object != None:
                    mouse_x, mouse_y = event.pos
                    pan_x, pan_y = event.rel

                    dragging_object.x = mouse_x - SYMBOL_WIDTH // 2
                    dragging_object.y = mouse_y - SYMBOL_HEIGHT // 2

                    for cable in dragging_object.input_cables:
                        # bug other cable as well and it is not at the pin yet
                        cable.pin1 = (dragging_object.x + pan_x,
                                      dragging_object.y + pan_y)

            # release obj
            if event.type == pygame.MOUSEBUTTONUP and dragging_object is not None:
                if event.button == 1:
                    if dragging_object.y > SYMBOL_HEIGHT:
                        dragging_object = None
                else:
                    objects.remove(dragging_object)

            # When Cable mode on
            if event.type == pygame.MOUSEBUTTONDOWN and cable_mode:
                global line_start
                x, y = event.pos
                line_start = find_nearest_pin(
                    objects, x, y, Gate, Switch, Light)

            if event.type == pygame.MOUSEMOTION and cable_mode:
                global line_end
                if line_start is not None:
                    line_end = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and cable_mode and line_start is not None:
                    try:
                        pin1_x, pin1_y = find_nearest_pin(
                            objects, line_start[0], line_start[1], Gate, Switch, Light)
                        pin2_x, pin2_y = find_nearest_pin(
                            objects, line_end[0], line_end[1], Gate, Switch, Light)

                        pin1_type = check_red_marker_click(
                            pin1_x, pin1_y, Gate, Switch, Light).get("Pin Type")
                        pin2_type = check_red_marker_click(
                            pin2_x, pin2_y, Gate, Switch, Light).get("Pin Type")

                        print(pin1_type, pin1_x, pin1_y)
                        print(pin2_type, pin2_x, pin2_y)

                        new_cable = Cable(
                            len(cables), [pin1_x, pin1_y], [pin2_x, pin2_y], True)
                        cables.append(new_cable)

                        connect_input_ouput(
                            pin1_type, pin2_type, pin1_x, pin1_y, pin2_x, pin2_y, Gate, Light, Switch, new_cable)

                        line_start = None
                        line_end = None

                    except Exception as e:
                        line_start = None
                        line_end = None
                        print(e)

                elif event.button == 2:
                    panning = False

            # right click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right click
                    mouse_x, mouse_y = event.pos
                    this_obj = get_obj_by_position(
                        mouse_x, mouse_y, objects)
                    right_click_menu = create_right_click_menu(this_obj)
                    right_click_menu_visible = True
                elif event.button == 2:
                    cable_mode = False
                    panning = True

            # middle mouse
            if event.type == pygame.MOUSEMOTION and panning == True:
                drag_screen(event.rel, objects, cables)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                clicked_pin_info = check_red_marker_click(
                    mouse_x, mouse_y, Gate, Switch, Light)
                if clicked_pin_info:
                    print(f"Clicked Red Marker Info: {clicked_pin_info}")

        draw_window(menu_bar, and_gate_btn, not_gate_btn, or_gate_btn,
                    nand_gate_btn, nor_gate_btn, objects, switch_off_btn, light_off_btn, cable_btn, cable_bg, line_start, line_end)

    pygame.quit()


if __name__ == '__main__':
    main()
