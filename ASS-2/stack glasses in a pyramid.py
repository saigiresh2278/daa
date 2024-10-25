poured = 2          
query_row = 1   
query_glass = 1    
tower = [[0] * (r + 1) for r in range(101)]  

tower[0][0] = poured
for row in range(100):  
    for col in range(row + 1):
        if tower[row][col] > 1:
            overflow = (tower[row][col] - 1) / 2.0  
            tower[row][col] = 1              
            tower[row + 1][col] += overflow
            tower[row + 1][col + 1] += overflow
print(min(1, tower[query_row][query_glass]))
