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


def drag_screen(event, objects):

    pan_x, pan_y = event

    for obj in objects:
        obj.x += pan_x
        obj.y += pan_y
    # think about zoom in and out


def toggleSwitch(double_clicked_object):
    double_clicked_object.update()
