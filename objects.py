class DrawableObject:
    def __init__(self, _id, image, x, y):
        self.id = _id
        self.image = image
        self.x = x
        self.y = y


class Gate(DrawableObject):
    def __init__(self, _id, gate_type, image, x, y):
        super().__init__(_id, image, x, y)
        self.gate_type = gate_type
        # self.inputs = []  #  input connections
        # self.outputs = []  #  output connections

    def update(self):
        #  logic to compute outputs based on inputs
        pass


class Switch(DrawableObject):
    def __init__(self, _id, switch_state, image, x, y):
        super().__init__(_id, image, x, y)
        self.switch_state = switch_state  # True for on, False for off


class Light(DrawableObject):
    def __init__(self, _id, light_state, image, x, y):
        super().__init__(_id, image, x, y)
        self.light_state = light_state  # True for on, False for off


class Cable():
    def __init__(self, _id, obj_connection_1, obj_connection_2, active):
        self.id = _id
        self.obj_connection_1 = obj_connection_1
        self.obj_connection_2 = obj_connection_2
        self.active = active  # true or false
