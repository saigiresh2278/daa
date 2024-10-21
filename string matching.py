main_string = "hello world"
substring = "world"
n = len(main_string)
m = len(substring)
found = False  
for i in range(n - m + 1): 
    match = True 
    for j in range(m):  
        if main_string[i + j] != substring[j]: 
            match = False 
            break  
    if match:  
        found = True
        start_index = i 
        break  
if found:
    print(f"Substring '{substring}' found at index: {start_index}")
else:
    print(f"Substring '{substring}' not found in the main string.")
