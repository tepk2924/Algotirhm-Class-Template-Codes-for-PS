from collections import deque

class Real_Range:
    def __init__(self):
        self.pts = deque()
    
    def __ior__(self, other:tuple):
        start, end = other
        start_used = False
        end_used = False
        status = 0
        new_pts = deque()
        while self.pts:
            val, pttype = self.pts.popleft()
            if not start_used and start <= val:
                self.pts.appendleft((val, pttype))
                val, pttype = start, 1
                start_used = True
            elif start_used and not end_used and end <= val:
                self.pts.appendleft((val, pttype))
                val, pttype = end, -1
                end_used = True
            old_status = status
            status += pttype
            if old_status == 0 and status == 1:
                new_pts.append((val, 1))
            elif old_status == 1 and status == 0:
                new_pts.append((val, -1))
        if not start_used:
            new_pts.append((start, 1))
        if not end_used:
            new_pts.append((end, -1))
        self.pts = new_pts
        return self
    
    def __str__(self):
        return f"{[*self.pts]}"