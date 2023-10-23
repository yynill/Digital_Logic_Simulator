def gate_logic_algo(inputs, gate_type):
    if len(inputs) == 0:
        pass
    elif len(inputs) == 1:
        input1 = inputs[0]
        if gate_type == 'NOT_GATE':
            if input1 == True:
                return False
            else:
                return True

    elif len(inputs) == 2:
        input1, input2 = inputs
        if input1 is not None and input2 is not None:
            if gate_type == 'AND_GATE':
                if input1 == True and input2 == True:
                    return True
                else:
                    return False

            elif gate_type == 'OR_GATE':
                if (input1 == True) or (input2 == True):
                    return True
                else:
                    return False

            elif gate_type == 'NAND_GATE':
                return not gate_logic_algo(inputs, 'AND_GATE')

            elif gate_type == 'NOR_GATE':
                return not gate_logic_algo(inputs, 'OR_GATE')

            elif gate_type == 'XOR_GATE':
                if input1 != input2:
                    return True
    else:
        return False
