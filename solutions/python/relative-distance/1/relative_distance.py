from collections import deque 
class RelativeDistance:
    def __init__(self, family_tree):
        
        
        self.graph = {}
        for parent, children in family_tree.items():
            self.graph.setdefault(parent, set())
            for child in children:
                self.graph.setdefault(child, set())
                self.graph[parent].add(child)
                self.graph[child].add(parent)
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    self.graph[children[i]].add(children[j])
                    self.graph[children[j]].add(children[i])

    def degree_of_separation(self, person_a, person_b):
        if person_a not in self.graph:
            raise ValueError("Person A not in family tree.")
        if person_b not in self.graph:
            raise ValueError("Person B not in family tree.")
            
        queue = deque([(person_a, 0)])
        visited = {person_a}
        while queue:
            current_person, distance = queue.popleft()
            
            if current_person == person_b:
                return distance
            else:
                for neighbor in self.graph[current_person]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
                        
        raise ValueError("No connection between person A and person B.")