#Version 1: super simple and intuitive
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] != 1) and (i == len(flowerbed)-1 or flowerbed[i+1] != 1):
                flowerbed[i] = 1
                count += 1
        if count >= n:
            return True
        else:
            return False

#Version 2: shubham sirs method: padding trick
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                count += 1
        if count >= n:
            return True
        else:
            return False
        

