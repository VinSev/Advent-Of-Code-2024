from debugger import Debugger


class InitialValueFinder:   
    @staticmethod
    def get_lowest_initial_a(program_data, initial_a=0, depth=0, target_output=None):
        if depth == len(target_output):
            return initial_a
        
        for i in range(8):
            output = Debugger(program_data, initial_a * 8 + i).run()
            
            if output and output[0] == target_output[depth]:
                lowest_initial_value = InitialValueFinder.get_lowest_initial_a(program_data, (initial_a * 8 + i), depth + 1, target_output)
                
                if result := lowest_initial_value:
                    return result
        return 0
