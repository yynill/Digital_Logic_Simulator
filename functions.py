import pygame
from constants import *
from objects import *
from functions import *


def get_obj_by_position(mouse_x, mouse_y, objects):
    for obj in objects:
        if obj.x < mouse_x < obj.x + SYMBOL_WIDTH and obj.y < mouse_y < obj.y + SYMBOL_HEIGHT:
            return get_obj_by_id(obj.id)


def get_obj_by_id(obj_id):
    for obj in objects:
        if obj.id == obj_id:
            return obj
    return None


def drag_screen(event, objects, cables):

    pan_x, pan_y = event

    for obj in objects:
        obj.x += pan_x
        obj.y += pan_y
    for cbl in cables:
        cbl.pin1[0] += pan_x
        cbl.pin1[1] += pan_y
        cbl.pin2[0] += pan_x
        cbl.pin2[1] += pan_y

    # think about zoom in and out


def toggleSwitch(double_clicked_object):
    double_clicked_object.update()
    for cable in cables:
        cable.update()

    for light in objects:
        if hasattr(light, "light"):
            light.update()


def create_right_click_menu(this_obj):
    pass
    # obj id, objects type,
    # show gate connections and signals,
    # show gate inout output table,
    # show ecplanation,
    # delete gate button
    # same with lamp and switches


def is_near_pin(mouse_x, mouse_y, pin_x, pin_y):
    distance = ((mouse_x - pin_x) ** 2 + (mouse_y - pin_y) ** 2) ** 0.5
    return distance <= 8


def check_red_marker_click(mouse_x, mouse_y, Gate, Switch, Light):
    for obj_type, pin_attributes in pin_points.items():
        for obj in objects:
            if isinstance(obj, Gate) and obj.get_gate_type() == obj_type:
                for pin_x, pin_y, pin_type in pin_attributes:
                    pin_x_abs = obj.x + pin_x
                    pin_y_abs = obj.y + pin_y
                    if is_near_pin(mouse_x, mouse_y, pin_x_abs, pin_y_abs):
                        return {
                            "Position": (pin_x_abs, pin_y_abs),
                            "Object ID": obj.id,
                            "Object Type": obj_type,
                            "Pin Type": pin_type
                        }
            elif isinstance(obj, Switch) and obj_type == 'SWITCH':
                for pin_x, pin_y, pin_type in pin_attributes:
                    pin_x_abs = obj.x + pin_x
                    pin_y_abs = obj.y + pin_y
                    if is_near_pin(mouse_x, mouse_y, pin_x_abs, pin_y_abs):
                        return {
                            "Position": (pin_x_abs, pin_y_abs),
                            "Object ID": obj.id,
                            "Object Type": "SWITCH",
                            "Pin Type": pin_type
                        }
            elif isinstance(obj, Light) and obj_type == 'LIGHT':
                for pin_x, pin_y, pin_type in pin_attributes:
                    pin_x_abs = obj.x + pin_x
                    pin_y_abs = obj.y + pin_y
                    if is_near_pin(mouse_x, mouse_y, pin_x_abs, pin_y_abs):
                        return {
                            "Position": (pin_x_abs, pin_y_abs),
                            "Object ID": obj.id,
                            "Object Type": "LIGHT",
                            "Pin Type": pin_type
                        }

    return None


def find_nearest_pin(objects, x, y, Gate, Switch, Light):
    min_distance = float('inf')
    nearest_pin = None

    for obj in objects:
        if isinstance(obj, Gate):
            for pin_x, pin_y, pin_type in pin_points.get(obj.get_gate_type(), []):
                pin_x_abs = obj.x + pin_x
                pin_y_abs = obj.y + pin_y
                distance = ((x - pin_x_abs) ** 2 + (y - pin_y_abs) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    nearest_pin = [pin_x_abs, pin_y_abs]

        elif isinstance(obj, Switch):
            obj_type = 'SWITCH'
            for pin_x, pin_y, pin_type in pin_points.get(obj_type, []):
                pin_x_abs = obj.x + pin_x
                pin_y_abs = obj.y + pin_y
                distance = ((x - pin_x_abs) ** 2 + (y - pin_y_abs) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    nearest_pin = [pin_x_abs, pin_y_abs]

        elif isinstance(obj, Light):
            obj_type = 'LIGHT'
            for pin_x, pin_y, pin_type in pin_points.get(obj_type, []):
                pin_x_abs = obj.x + pin_x
                pin_y_abs = obj.y + pin_y
                distance = ((x - pin_x_abs) ** 2 + (y - pin_y_abs) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    nearest_pin = [pin_x_abs, pin_y_abs]

    return nearest_pin


def find_object_by_pin(pin_x, pin_y, objects):
    nearest_object = None
    nearest_distance = float('inf')

    for obj in objects:
        for obj_type, pin_attributes in pin_points.items():
            for pin_xu, pin_yu, pin_type in pin_attributes:
                pin_x_abs = obj.x + pin_xu
                pin_y_abs = obj.y + pin_yu
                distance = ((pin_x_abs - pin_x) ** 2 +
                            (pin_y_abs - pin_y) ** 2) ** 0.5
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_object = obj

    return nearest_object

# get the conected obj
# on the pin, whhere if pin = input
# append cables into {self.input_cables}


def connect_input_ouput(pin1_type, pin2_type, pin1_x, pin1_y, pin2_x, pin2_y, Gate, Light, Switch, new_cable):
    if (pin1_type == 'input' and pin2_type == 'output') or (pin1_type == 'output' and pin2_type == 'input'):

        nearest_obj1 = find_object_by_pin(
            pin1_x, pin1_y, objects)

        nearest_obj2 = find_object_by_pin(
            pin2_x, pin2_y, objects)

        print(nearest_obj1.id)
        print(nearest_obj2.id)

        if pin1_type == 'input':
            nearest_obj1.input_cables.append(new_cable)
            nearest_obj2.output_cables.append(new_cable)
        else:
            nearest_obj1.output_cables.append(new_cable)
            nearest_obj2.input_cables.append(new_cable)
