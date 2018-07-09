

class Solution(object):
    def __init__(self):
        self.checks=set()

    def canVisitAllRooms(self, rooms):
        self.checks.add(0)
        self.rooms=rooms
        self.DFS(0)
        return True if len(self.checks) == len(rooms) else False

    def DFS(self,n):
        for k in self.rooms[n]:
            if k not in self.checks:
                self.checks.add(k)
                self.DFS(k)

sln =Solution()
assert False == sln.canVisitAllRooms([[1],[2],[3],[],[3]])
sln =Solution()
assert True == sln.canVisitAllRooms([[1],[2],[3],[]])
sln =Solution()
assert False == sln.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])

