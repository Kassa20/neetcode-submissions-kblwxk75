class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    
        current = init 

        for _ in range(iterations):
            derivative = 2 * current 
            current = current - derivative * learning_rate
        
        return round(current, 5)