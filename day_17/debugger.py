from instruction_set import InstructionSet


class Debugger:    
    def __init__(self, instructions, initial_a):
        self.instructions = instructions
        self.register_a = initial_a

    def execute_instruction(self, instruction_pointer, register_a, register_b, register_c, literal_operand, combo_operand):
        match self.instructions[instruction_pointer]:
            case 0: register_a = InstructionSet.advance(register_a, combo_operand)
            case 1: register_b = InstructionSet.bitwise_xor(register_b, literal_operand)
            case 2: register_b = InstructionSet.bitwise_store(combo_operand)
            case 3: instruction_pointer = InstructionSet.jump_if_not_zero(register_a, literal_operand, instruction_pointer)
            case 4: register_b = InstructionSet.bitwise_xor_with_register_c(register_b, register_c)
            case 5: return InstructionSet.output(register_b, combo_operand)
            case 6: register_b = InstructionSet.bitwise_divide(register_a, combo_operand)
            case 7: register_c = InstructionSet.copy_divide(register_a, combo_operand)
        
        return register_a, register_b, register_c, instruction_pointer

    def run(self):
        instruction_pointer, register_b, register_c, outputs = 0, 0, 0, []
       
        while 0 <= instruction_pointer < len(self.instructions):
            literal_operand = self.instructions[instruction_pointer + 1]
            combo_operand = [0, 1, 2, 3, self.register_a, register_b, register_c, None][literal_operand]
            result = self.execute_instruction(instruction_pointer, self.register_a, register_b, register_c, literal_operand, combo_operand)
            
            if isinstance(result, tuple) and len(result) == 4:
                self.register_a, register_b, register_c, instruction_pointer = result
            else:
                register_b, output_value = result
                outputs.append(output_value)
            
            instruction_pointer += 2
            
        return outputs
