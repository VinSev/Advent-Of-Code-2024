class TowelProcessor():
    def count_possible_towel_arrangements(self, towel_patterns, target_design):
        arrangement_count = [0] * (len(target_design) + 1)
        arrangement_count[0] = 1

        for end in range(1, len(target_design) + 1):
            for start in range(0, end):
                if target_design[start:end] in towel_patterns:
                    arrangement_count[end] += arrangement_count[start]

        return arrangement_count[-1]
