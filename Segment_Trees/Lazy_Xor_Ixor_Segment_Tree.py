from typing import Any

class Lazy_Xor_Ixor_Segment_Tree:
    def __init__(self, arr):
        self.len = len(arr)

        self.originarr = arr[:]
        #root at idx 1, each node with index idx has child at index 2*i and 2*i + 1
        self.tree = [None for _ in range(4*len(arr) + 1)]
        self.pending_xor = [0 for _ in range(4*len(arr) + 1)]
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
        val = self.__init_sub(node_start_inclu, mid, 2*intrinsicidx) ^ self.__init_sub(mid, node_end_exclu, 2*intrinsicidx + 1)
        self.tree[intrinsicidx] = val
        return val

    def __len__(self) -> int:
        return self.len

    def __pending_xor_push(self,
                           node_start_inclu:int,
                           node_end_exclu:int,
                           intrinsicidx:int) -> None:
        xor = self.pending_xor[intrinsicidx]
        if xor:
            if (node_end_exclu - node_start_inclu) % 2:
                self.tree[intrinsicidx] ^= xor
            if node_start_inclu + 1 != node_end_exclu:
                self.pending_xor[2*intrinsicidx] ^= xor
                self.pending_xor[2*intrinsicidx + 1] ^= xor
            self.pending_xor[intrinsicidx] = 0

    def range_xor(self,
                  range_start_inclu:int,
                  range_end_exclu:int,
                  xor:int) -> None:
        self.__range_xor_sub(0, self.len, 1, range_start_inclu, range_end_exclu, xor)

    def __range_xor_sub(self,
                        node_start_inclu:int,
                        node_end_exclu:int,
                        intrinsicidx:int,
                        range_start_inclu:int,
                        range_end_exclu:int,
                        xor:int) -> Any:
        self.__pending_xor_push(node_start_inclu, node_end_exclu, intrinsicidx)
        if (range_end_exclu - range_start_inclu) % 2:
            self.tree[intrinsicidx] ^= xor
        if node_start_inclu + 1 == node_end_exclu:
            return
        if node_start_inclu == range_start_inclu and node_end_exclu == range_end_exclu:
            self.pending_xor[intrinsicidx*2] ^= xor
            self.pending_xor[intrinsicidx*2 + 1] ^= xor
            return
        mid = (node_start_inclu + node_end_exclu) // 2
        if mid >= range_end_exclu:
            self.__range_xor_sub(node_start_inclu, mid, 2*intrinsicidx, range_start_inclu, range_end_exclu, xor)
        elif mid <= range_start_inclu:
            self.__range_xor_sub(mid, node_end_exclu, 2*intrinsicidx + 1, range_start_inclu, range_end_exclu, xor)
        else:
            self.__range_xor_sub(node_start_inclu, mid, 2*intrinsicidx, range_start_inclu, mid, xor)
            self.__range_xor_sub(mid, node_end_exclu, 2*intrinsicidx + 1, mid, range_end_exclu, xor)

    def __get_sub(self,
                  node_start_inclu:int,
                  node_end_exclu:int,
                  intrinsicidx:int,
                  slice_start_inclu:int,
                  slice_end_exclu:int) -> Any:
        if slice_start_inclu < node_start_inclu or slice_end_exclu > node_end_exclu:
            raise ValueError
        self.__pending_xor_push(node_start_inclu, node_end_exclu, intrinsicidx)
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
            return self.__get_sub(node_start_inclu, mid, 2*intrinsicidx, slice_start_inclu, mid) ^ self.__get_sub(mid, node_end_exclu, 2*intrinsicidx + 1, mid, slice_end_exclu)

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

import sys
N = int(sys.stdin.readline())
arr = [*map(int, sys.stdin.readline().split())]
stree = Lazy_Xor_Ixor_Segment_Tree(arr)
M = int(sys.stdin.readline())
for _ in range(M):
    a, *info = map(int, sys.stdin.readline().split())
    if a == 1:
        i, j, k = info
        stree.range_xor(i, j + 1, k)
    else:
        i, j = info
        sys.stdout.write(f"{stree[i:j + 1]}\n")