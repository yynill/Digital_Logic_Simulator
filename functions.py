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


def drag_screen(event, objects, Gate):

    pan_x, pan_y = event

    for obj in objects:
        if isinstance(obj, Gate):
            if obj.gate_type != 'NOT_GATE':
                obj.x += pan_x
                obj.y += pan_y

                obj.output_region.x += pan_x
                obj.output_region.y += pan_y

                obj.input_region1.x += pan_x
                obj.input_region1.y += pan_y

                obj.input_region2.x += pan_x
                obj.input_region2.y += pan_y

            elif obj.gate_type == 'NOT_GATE':

                obj.x += pan_x
                obj.y += pan_y

                obj.output_region.x += pan_x
                obj.output_region.y += pan_y

                obj.input_region.x += pan_x
                obj.input_region.y += pan_y
        else:
            obj.x += pan_x
            obj.y += pan_y

    # think about zoom in and out


def toggleSwitch(double_clicked_object):
    double_clicked_object.update()
    for cable in cables:
        cable.update()

    for light in objects:
        if hasattr(light, "light"):
            light.update()


def get_cable_by_connection(obj1_id, obj2_id):
    for cable in cables:
        if cable.obj_connection_1 == obj1_id and cable.obj_connection_2 == obj2_id:
            return cable
        elif cable.obj_connection_1 == obj2_id and cable.obj_connection_2 == obj1_id:
            return cable
    return None
