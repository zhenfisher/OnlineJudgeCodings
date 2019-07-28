# class Solution:

#     def __init__(self, radius: float, x_center: float, y_center: float):
#         self.r = radius
#         self.x = x_center
#         self.y = y_center

#     def randPoint(self) -> List[float]:
#         low, high = -self.r, self.r
#         a = random.uniform(low, high)
#         b = random.uniform(low, high)
#         # print(a,b)
#         if a**2+b**2 > self.r**2:
#             return self.randPoint()
#         return [a+self.x, b+self.y]

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        low, high = -self.r, self.r
        while True:
            a = random.uniform(low, high)
            b = random.uniform(low, high)
            if a**2+b**2 <= self.r**2:
                return [a+self.x, b+self.y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()