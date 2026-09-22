class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]

            clone = Node(node.val)
            mp[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)