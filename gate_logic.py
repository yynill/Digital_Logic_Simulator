def gate_logic_algo(inputs, gate_type):
    if gate_type == 'AND_GATE':
        input1, input2 = inputs
        if input1 == True and input2 == True:
            return True
        else:
            return False

    elif gate_type == 'OR_GATE':
        input1, input2 = inputs
        if input1 == True or input2 == True:
            return True
        else:
            return False

    elif gate_type == 'NOT_GATE':
        input1 = inputs
        if input1 == True:
            return False
        else:
            return True

    elif gate_type == 'NAND_GATE':
        input1, input2 = inputs
        return not gate_logic_algo(input1, input2, 'AND_GATE')

    elif gate_type == 'NOR_GATE':
        input1, input2 = inputs
        return not gate_logic_algo(input1, input2, 'OR_GATE')
