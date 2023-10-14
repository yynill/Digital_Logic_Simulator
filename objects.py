from constants import *
from functions import *
from gate_logic import *


class DrawableObject:
    def __init__(self, _id, image, x, y):
        self.id = _id
        self.image = image
        self.x = x
        self.y = y
        self.input_cables = {}  # empty = no cable / False = off cable / True on cable

    def print_cables(self):
        if isinstance(self, Light) or isinstance(self, Gate):
            print(f'Input cables of {self.id} - {self.input_cables}')


def connect_cable(object_1, object_2, cable_state):
    object_1.input_cables[object_2.id] = cable_state
    object_2.input_cables[object_1.id] = cable_state


class Gate(DrawableObject):
    def __init__(self, _id, gate_type, image, x, y, num_inputs):
        super().__init__(_id, image, x, y)
        self.gate_type = gate_type
        self.num_inputs = num_inputs
        self.output = False

        # Input and output regions

        if self.gate_type == 'NOT_GATE':
            # Common part for all gates
            self.input_region = pygame.Rect(
                x, y + SYMBOL_HEIGHT, SYMBOL_WIDTH, INPUT_REGION_HEIGHT)

        if self.gate_type != 'NOT_GATE':
            # Specific part for NOT gate
            self.input_region1 = pygame.Rect(
                x, y + SYMBOL_HEIGHT, INPUT_REGION_WIDTH, INPUT_REGION_HEIGHT)
            self.input_region2 = pygame.Rect(
                x, y + SYMBOL_HEIGHT, INPUT_REGION_WIDTH, INPUT_REGION_HEIGHT)

        self.output_region = pygame.Rect(
            x, y - OUTPUT_REGION_HEIGHT, SYMBOL_WIDTH, OUTPUT_REGION_HEIGHT)

    # calc output
    def update(self):
        input_values = [obj.input_cables[obj.id] for obj in self.input_cables]
        self.output = gate_logic_algo(input_values, self.gate_type)

        # Update output cable state
        for obj_id, state in self.output_cables.items():
            cable = get_cable_by_connection(self.id, obj_id)
            cable.state = self.output


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


class Light(DrawableObject):
    def __init__(self, _id, state, image, x, y):
        super().__init__(_id, image, x, y)
        self.state = state  # True for on, False for off
        self.light = True

    def update(self):
        if self.input_cables:
            cable_states = list(self.input_cables.values())

            if True in cable_states:
                self.state = True
                self.image = light_images['LIGHT_ON']
            else:
                self.state = False
                self.image = light_images['LIGHT_OFF']
        else:
            self.state = False
            self.image = light_images['LIGHT_OFF']


class Cable():
    def __init__(self, _id, obj_connection_1, obj_connection_2, state):
        self.id = _id
        self.obj_connection_1 = obj_connection_1
        self.obj_connection_2 = obj_connection_2
        self.state = state  # true or false

    def update(self):
        obj1 = get_obj_by_id(self.obj_connection_1)
        obj2 = get_obj_by_id(self.obj_connection_2)

        # check if connection is switch and inherit state
        if isinstance(obj1, Switch):
            self.state = obj1.state
        elif isinstance(obj2, Switch):
            self.state = obj2.state

        elif isinstance(obj2, Gate):
            self.state = obj2.state
        elif isinstance(obj2, Gate):
            self.state = obj2.state

        else:
            self.state = False

        if self.state == True:
            connect_cable(obj1, obj2, True)
        elif self.state == False:
            connect_cable(obj1, obj2, False)
