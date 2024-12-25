class InstructionSet:
    @staticmethod
    def advance(register_a, combo_operand):
        return int(register_a / 2**combo_operand)

    @staticmethod
    def bitwise_xor(register_b, literal_operand):
        return register_b ^ literal_operand

    @staticmethod
    def bitwise_store(combo_operand):
        return combo_operand % 8

    @staticmethod
    def jump_if_not_zero(register_a, literal_operand, instruction_pointer):
        return instruction_pointer if register_a == 0 else literal_operand - 2

    @staticmethod
    def bitwise_xor_with_register_c(register_b, register_c):
        return register_b ^ register_c

    @staticmethod
    def output(register_b, combo_operand):
        return register_b, combo_operand % 8

    @staticmethod
    def bitwise_divide(register_a, combo_operand):
        return int(register_a / 2**combo_operand)

    @staticmethod
    def copy_divide(register_a, combo_operand):
        return int(register_a / 2**combo_operand)
