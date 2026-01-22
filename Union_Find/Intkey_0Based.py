class Union_Find:
    def __init__(self, N):
        '''
        key is indexed with 0 to N - 1
        '''
        self.N = N
        self.__parent = [*range(N)]
        self.__rank = [0]*N
    
    def find_root(self, key):
        while True:
            if self.__parent[key] == key:
                return key
            key = self.__parent[key]
    
    def union(self, key1, key2) -> None:
        root1 = self.find_root(key1)
        root2 = self.find_root(key2)
        if self.__rank[root1] > self.__rank[root2]:
            self.__parent[root2] = root1
        elif self.__rank[root1] < self.__rank[root2]:
            self.__parent[root1] = root2
        elif root1 == root2:
            return
        else:
            self.__rank[root1] += 1
            self.__parent[root2] = root1
    
    def is_same_set(self, key1, key2) -> bool:
        return self.find_root(key1) == self.find_root(key2)
    
    #Comment the part below if you do not want to use stringfy of this class: tepk2924
    def __child_root_evaluation(self):
        self.__child_lazy_eval = [set() for _ in range(self.N)]
        self.__roots_lazy_eval = set()
        for key in range(self.N):
            curr = key
            while True:
                parent = self.__parent[curr]
                if parent == curr:
                    self.__roots_lazy_eval.add(curr)
                    break
                self.__child_lazy_eval[parent].add(curr)
                curr = parent

    def __str_DFS(self, key, depth):
        self.__strins.append(" "*depth + str(key))
        for child in self.__child_lazy_eval[key]:
            self.__str_DFS(child, depth + 1)

    def __str__(self):
        self.__child_root_evaluation()
        self.__strins = ["<Union Find>"]
        for root in self.__roots_lazy_eval:
            self.__str_DFS(root, 0)
        return "\n".join(self.__strins)

uf = Union_Find(10)
uf.union(3, 4)
uf.union(9, 2)
uf.union(1, 7)
print(uf)
uf.union(0, 7)
print(uf)