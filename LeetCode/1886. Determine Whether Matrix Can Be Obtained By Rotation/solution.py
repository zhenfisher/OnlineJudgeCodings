class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 最多旋转 4 次
        for k in range(4):
            # 旋转操作
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    mat[i][j], mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i] \
                        = mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i], mat[i][j]
            
            if mat == target:
                return True
        return False


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solution/pan-duan-ju-zhen-jing-lun-zhuan-hou-shi-qa9d0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            new_mat = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new_mat[j][n-i-1] = mat[i][j]
            return new_mat

        def equal(new_mat, target):
            n = len(mat)
            for i in range(n):
                for j in range(n):
                    if new_mat[i][j] != target[i][j]:
                        return False
            return True

        for i in range(4):
            if equal(mat, target):
                return True
            mat = rotate(mat)
        return False

