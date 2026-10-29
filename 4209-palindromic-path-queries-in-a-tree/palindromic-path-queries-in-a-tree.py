class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()

            if state == 0:
                parent[0][node] = node if par == -1 else par
                tin[node] = timer
                timer += 1

                stack.append((node, par, 1))

                for nei in reversed(graph[node]):
                    if nei != par:
                        depth[nei] = depth[node] + 1
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer - 1

        for k in range(1, LOG):
            for node in range(n):
                parent[k][node] = parent[k - 1][parent[k - 1][node]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def point_query(i):
            result = 0
            i += 1

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        masks = [1 << (ord(c) - ord('a')) for c in s]

        for node in range(n):
            add(tin[node], masks[node])

            if tout[node] + 1 < n:
                add(tout[node] + 1, masks[node])

        def prefix(node):
            return point_query(tin[node])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))
                change = masks[u] ^ new_mask

                if change:
                    add(tin[u], change)

                    if tout[u] + 1 < n:
                        add(tout[u] + 1, change)

                    masks[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                path_mask = (
                    prefix(u)
                    ^ prefix(v)
                    ^ masks[ancestor]
                )

                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer