class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for fr, to in edges:
            dic[fr].append(to)

        # check if destination node has any outgoing edge
        # if so, return false
        if dic[destination]:
            return False

        visited = set()

        @cache
        def dfs(node):
            ## if loop(node in seen), return False becaus that keep leads to loop and npt destination
            ## if edge doesn't have outgping edge, that means that is destination, so check thatnode == dest
            ## othervise retur True
            if node == destination:
                return True
            
            if node in visited or not dic[node]:
                return False

            # add the node in visted
            visited.add(node)

            # now loop over all the dest nodes we can reach from node
            for neighbour in dic[node]:
                if not dfs(neighbour):
                    return False

            ## backtreck
            visited.remove(node)
            return True

        return dfs(source)
