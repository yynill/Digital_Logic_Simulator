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
