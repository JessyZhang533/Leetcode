class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:  # include the value check into base case if statement
                return
            image[row][col] = newColor
            traverse(row-1, col)
            traverse(row+1, col)
            traverse(row, col-1)
            traverse(row, col+1)  # !!!: do this when need to traverse a matrix in 4 directions --> Q200
        if orig_color != newColor:  # Save the effort for some cases
            traverse(sr, sc)
        return image
