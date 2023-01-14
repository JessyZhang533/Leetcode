class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # https://leetcode.com/problems/matrix-block-sum/solutions/482730/python-js-go-c-o-m-n-integral-image-dp-w-explanation/
        " dp; integral image "
        r, c = len(mat), len(mat[0])

        # create the integral matrix from the original matrix
        integral_mat = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            sum = 0  # initialise the sum to 0 every time entering a new outer for loop; the sum is the accumulated sum of the current row
            for j in range(c):
                sum += mat[i][j]
                integral_mat[i][j] = sum
                if i > 0:
                    integral_mat[i][j] += integral_mat[i-1][j]  # if row index > 0, add sum of the previous rows

        # create the output matrix from the integral mtrix
        output_mat = [[0 for _ in range(c)] for _ in range(r)]
        for m in range(r):
            min_r, max_r = max(m-k, 0), min(m+k, r-1)  # min_r requires function max(), max_r requires function min ()
            for n in range(c):
                min_c, max_c = max(n-k, 0), min(n+k, c-1)  # same as above
                output_mat[m][n] = integral_mat[max_r][max_c]
                if min_r > 0:
                    output_mat[m][n] -= integral_mat[min_r-1][max_c]
                if min_c > 0:
                    output_mat[m][n] -= integral_mat[max_r][min_c-1]
                if min_c > 0 and min_r > 0:
                    output_mat[m][n] += integral_mat[min_r-1][min_c-1]
        return output_mat
