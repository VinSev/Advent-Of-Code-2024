from typing import List, Set, Tuple, Dict


class ComputerNetwork:
    def __init__(self, connections: List[Tuple[str, str]]) -> None:
        self.network = self.create_network(connections)

    def create_network(self, connections: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
        computer_network = {}
        
        for a, b in connections:
            if a not in computer_network:
                computer_network[a] = set()
            if b not in computer_network:
                computer_network[b] = set()
            computer_network[a].add(b)
            computer_network[b].add(a)
        
        return computer_network

    def find_triangles(self) -> Set[Tuple[str, str, str]]:
        triangles = set()
        
        for a in self.network:
            for b in self.network[a]:
                if a < b:
                    common_neighbors = self.network[a].intersection(self.network[b])
                    for c in common_neighbors:
                        if b < c:
                            triangles.add((a, b, c))
        
        return triangles

    def count_triangles_with_t(self, triangles: Set[Tuple[str, str, str]]) -> int:
        count = 0
        
        for triangle in triangles:
            for node in triangle:
                if node.startswith('t'):
                    count += 1
                    break
        
        return count

    def get_candidates(self, current_node: str) -> List[str]:
        candidates = []
        
        for neighbor in self.network[current_node]:
            if neighbor > current_node:
                candidates.append(neighbor)
        
        candidates.sort(reverse=True)
        
        return candidates

    def update_candidates(self, candidates: List[str], next_candidate: str) -> List[str]:
        updated_candidates = []
        
        for neighbor in candidates:
            if neighbor in self.network[next_candidate] and neighbor > next_candidate:
                updated_candidates.append(neighbor)
        
        return updated_candidates

    def get_largest_lan_party(self) -> List[str]:
        nodes = sorted(self.network.keys())
        largest_lan_party = []

        for current_node in nodes:
            current_lan_party = [current_node]
            candidates = self.get_candidates(current_node)
            largest_lan_party = self.expand_lan_party(candidates, largest_lan_party, current_lan_party)

        return largest_lan_party

    def expand_lan_party(self, candidates: List[str], largest_lan_party: List[str], current_lan_party: List[str]) -> List[str]:
        while candidates:
            next_candidate = candidates.pop()
            current_lan_party.append(next_candidate)

            if len(current_lan_party) > len(largest_lan_party):
                largest_lan_party = current_lan_party[:]

            candidates = self.update_candidates(candidates, next_candidate)

        return largest_lan_party
