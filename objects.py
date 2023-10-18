from constants import *
from functions import *
from gate_logic import *


class DrawableObject:
    def __init__(self, _id, image, x, y):
        self.id = _id
        self.image = image
        self.x = x
        self.y = y
        self.input_cables = []  # empty = no cable / False = off cable / True on cable
        self.output_cables = []

    def print_cables(self):
        if isinstance(self, Light) or isinstance(self, Gate):
            print(f'Input cables of {self.id} - {self.input_cables}')


class Gate(DrawableObject):
    def __init__(self, _id, gate_type, image, x, y, num_inputs):
        super().__init__(_id, image, x, y)
        self.gate_type = gate_type
        self.num_inputs = num_inputs
        self.state = False

    def get_gate_type(self):
        return self.gate_type

    # calc output
    def update(self):
        input_states = [cable.state for cable in self.input_cables]
        self.state = gate_logic_algo(input_states, self.gate_type)

        for output_cable in self.output_cables:
            output_cable.state = self.state


class Switch(DrawableObject):
    def __init__(self, _id, state, image, x, y):
        super().__init__(_id, image, x, y)
        self.state = state  # True for on, False for off
        self.switch = True

    def update(self):
        self.state = not self.state
        if self.state == True:
            self.image = switch_images['SWITCH_ON']
        else:
            self.image = switch_images['SWITCH_OFF']
        for cbl in self.output_cables:
            cbl.state = self.state


class Light(DrawableObject):
    def __init__(self, _id, state, image, x, y):
        super().__init__(_id, image, x, y)
        self.state = state  # True for on, False for off
        self.light = True

    def update(self):
        # Check if any of the input cables are True
        if any(cable.state for cable in self.input_cables):
            self.state = True
            self.image = light_images['LIGHT_ON']
        else:
            self.state = False
            self.image = light_images['LIGHT_OFF']


class Cable():
    def __init__(self, _id, pin1, pin2, state):
        self.id = _id
        self.pin1 = pin1  # (x, y) of pin1
        self.pin2 = pin2  # (x, y) of pin2
        self.state = False

    def update(self, mouse_x, mouse_y, cable, dragging_object, Gate, Light, Switch):
        # x1, y1, type1 = 0, 0, ''
        # x2, y2, type2 = 0, 0, ''

        # distance_to_pin1 = (
        #     (self.pin1[0] - dragging_object.x) ** 2 + (self.pin1[1] - dragging_object.y) ** 2)
        # distance_to_pin2 = (
        #     (self.pin2[0] - dragging_object.x) ** 2 + (self.pin2[1] - dragging_object.y) ** 2)

        # for obj in objects:
        #     if cable in obj.input_cables:
        #         obj_at_input = obj
        #         if isinstance(obj_at_input, Gate):
        #             obj_at_input_type = obj_at_input.gate_type
        #         elif isinstance(obj_at_input, Light):
        #             obj_at_input_type = 'LIGHT'
        #         elif isinstance(obj_at_input, Switch):
        #             obj_at_input_type = 'SWITCH'

        #         x1, y1, type1 = pin_points[obj_at_input_type][0]

        #     if cable in obj.output_cables:
        #         obj_at_output = obj
        #         if isinstance(obj_at_output, Gate):
        #             obj_at_output_type = obj_at_output.gate_type
        #         elif isinstance(obj_at_output, Light):
        #             obj_at_output_type = 'LIGHT'
        #         elif isinstance(obj_at_output, Switch):
        #             obj_at_output_type = 'SWITCH'

        #         x2, y2, type2 = pin_points[obj_at_output_type][0]

        #     if distance_to_pin1 < distance_to_pin2:
        #         self.pin1 = [x1 + dragging_object.x, y1 + dragging_object.y]
        #     else:
        #         self.pin2 = [x2 + dragging_object.x, y2 + dragging_object.y]
        pass
