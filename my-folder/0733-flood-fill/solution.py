class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image

        self.fill(image, sr, sc, color, image[sr][sc])
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, old_color: int):

        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): 
            return

        if old_color != image[sr][sc]:
            return
        
        image[sr][sc] = color
        self.fill(image, sr-1, sc, color, old_color)
        self.fill(image, sr+1, sc, color, old_color)
        self.fill(image, sr, sc-1, color, old_color)
        self.fill(image, sr, sc+1, color, old_color)

