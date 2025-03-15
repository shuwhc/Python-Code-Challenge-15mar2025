from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        # If only one node, path length is 0
        if n == 1:
            return 0
        
        # Target state: all nodes visited (full bitmask)
        target_state = (1 << n) - 1
        
        # Initialize queue with start states for each node
        queue = deque()
        visited = set()
        
        for start in range(n):
            # Initial state: node itself visited
            initial_state = (1 << start)
            queue.append((start, initial_state))
            visited.add((start, initial_state))
        
        # Track path length
        path_length = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                current_node, current_state = queue.popleft()
                
                # If all nodes visited, return path length
                if current_state == target_state:
                    return path_length
                
                # Explore neighbors
                for neighbor in graph[current_node]:
                    # Update state: mark neighbor as visited
                    new_state = current_state | (1 << neighbor)
                    
                    # If this state hasn't been explored
                    if (neighbor, new_state) not in visited:
                        queue.append((neighbor, new_state))
                        visited.add((neighbor, new_state))
            
            # Increment path length after exploring current level
            path_length += 1
        
        return -1  # Impossible path