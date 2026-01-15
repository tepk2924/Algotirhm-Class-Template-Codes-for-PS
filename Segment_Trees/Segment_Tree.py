from typing import Any

class Segment_Tree:
    def __init__(self, arr, func):
        self.len = len(arr)

        self.originarr = arr[:]
        #root at idx 1, each node with index idx has child at index 2*i and 2*i + 1
        self.tree = [None for _ in range(4*len(arr) + 1)]
        self.func = func
        self.__init_sub(0, self.len, 1)
        del self.originarr
    
    def __init_sub(self,
                   node_start_inclu:int,
                   node_end_exclu:int,
                   intrinsicidx:int) -> Any:
        if node_start_inclu + 1 == node_end_exclu:
            val = self.originarr[node_start_inclu]
            self.tree[intrinsicidx] = val
            return val
        mid = (node_start_inclu + node_end_exclu) // 2
        val = self.func(self.__init_sub(node_start_inclu, mid, 2*intrinsicidx), self.__init_sub(mid, node_end_exclu, 2*intrinsicidx + 1))
        self.tree[intrinsicidx] = val
        return val

    def __len__(self) -> int:
        return self.len

    def __setitem__(self,
                    idx:int,
                    val:int | float) -> None:
        self.__set_sub(0, self.len, 1, val, idx)

    def __set_sub(self,
                  node_start_inclu:int,
                  node_end_exclu:int,
                  intrinsicidx:int,
                  val:int | float,
                  setidx:int) -> Any:
        if node_start_inclu + 1 == node_end_exclu:
            self.tree[intrinsicidx] = val
            return val
        mid = (node_start_inclu + node_end_exclu) // 2
        if mid > setidx:
            retval = self.func(self.__set_sub(node_start_inclu, mid, 2*intrinsicidx, val, setidx), self.tree[2*intrinsicidx + 1])
            self.tree[intrinsicidx] = retval
            return retval
        elif mid <= setidx:
            retval = self.func(self.__set_sub(mid, node_end_exclu, 2*intrinsicidx + 1, val, setidx), self.tree[2*intrinsicidx])
            self.tree[intrinsicidx] = retval
            return retval
        return

    def __get_sub(self,
                  node_start_inclu:int,
                  node_end_exclu:int,
                  intrinsicidx:int,
                  slice_start_inclu:int,
                  slice_end_exclu:int) -> Any:
        if slice_start_inclu < node_start_inclu or slice_end_exclu > node_end_exclu:
            raise ValueError
        if node_start_inclu + 1 == node_end_exclu:
            return self.tree[intrinsicidx]
        if node_start_inclu == slice_start_inclu and node_end_exclu == slice_end_exclu:
            return self.tree[intrinsicidx]
        mid = (node_start_inclu + node_end_exclu) // 2
        if mid >= slice_end_exclu:
            return self.__get_sub(node_start_inclu, mid, 2*intrinsicidx, slice_start_inclu, slice_end_exclu)
        elif mid <= slice_start_inclu:
            return self.__get_sub(mid, node_end_exclu, 2*intrinsicidx + 1, slice_start_inclu, slice_end_exclu)
        else:
            return self.func(self.__get_sub(node_start_inclu, mid, 2*intrinsicidx, slice_start_inclu, mid), self.__get_sub(mid, node_end_exclu, 2*intrinsicidx + 1, mid, slice_end_exclu))

    def __getitem__(self, idx:int | slice) -> Any:
        """
        if idx is integer, returns as normal array.
        if idx is a slice, returns result of elements with indices that (equal to or greater than) slice start and (less than) slice stop
        """
        if isinstance(idx, int):
            return self.__get_sub(0, self.len, 1, idx, idx + 1)
        elif isinstance(idx, slice):
            if idx.start >= idx.stop:
                raise ValueError("slice stop must be greater than slice start index")
            else:
                return self.__get_sub(0, self.len, 1, idx.start, idx.stop)
        return None

if __name__ == "__main__":
    arr = [10, 20, 40, 20, 30, 70]
    stree = Segment_Tree(arr, lambda x, y : x + y)
    stree[5] = 50
    print(stree[2:6])
    print(stree[0])
    stree[0] = 5
    print(stree[0:3])