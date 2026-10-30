class Solution:
    def shortestPath(self, n: int, edges: list, labels: str, k: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # Custom Min-Heap Implementation (no imports)
        heap = []
        
        def push(item):
            heap.append(item)
            curr = len(heap) - 1
            while curr > 0:
                parent = (curr - 1) // 2
                if heap[curr][0] < heap[parent][0]:
                    heap[curr], heap[parent] = heap[parent], heap[curr]
                    curr = parent
                else:
                    break

        def pop():
            if not heap:
                return None
            top = heap[0]
            bottom = heap.pop()
            if heap:
                heap[0] = bottom
                curr = 0
                length = len(heap)
                while True:
                    left = 2 * curr + 1
                    right = 2 * curr + 2
                    smallest = curr
                    
                    if left < length and heap[left][0] < heap[smallest][0]:
                        smallest = left
                    if right < length and heap[right][0] < heap[smallest][0]:
                        smallest = right
                        
                    if smallest != curr:
                        heap[curr], heap[smallest] = heap[smallest], heap[curr]
                        curr = smallest
                    else:
                        break
            return top

        # Initial state: (total_weight, current_node, consecutive_count)
        # Starting at node 0 with its label contributing a count of 1.
        push((0, 0, 1))
        
        # dist[u][count] stores the minimum weight to reach node u with a given count
        dist = {}
        
        while heap:
            d, u, count = pop()
            
            # If we reached the destination node, return the accumulated weight
            if u == n - 1:
                return d
                
            if u in dist and count in dist[u] and dist[u][count] < d:
                continue
                
            if u not in dist:
                dist[u] = {}
            dist[u][count] = d
            
            # Explore neighbors
            for v, w in graph[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count > k:
                    continue
                    
                new_d = d + w
                if v not in dist or next_count not in dist[v] or new_d < dist[v][next_count]:
                    if v not in dist:
                        dist[v] = {}
                    dist[v][next_count] = new_d
                    push((new_d, v, next_count))
                    
        return -1