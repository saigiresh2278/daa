# Given input
jobs = [3, 2, 3]
k = 3

# Helper function to check if a maximum working time is possible
def can_finish(jobs, k, max_working_time):
    workloads = [0] * k
    
    def backtrack(i):
        if i == len(jobs):
            return True
        for j in range(k):
            if workloads[j] + jobs[i] <= max_working_time:
                workloads[j] += jobs[i]
                if backtrack(i + 1):
                    return True
                workloads[j] -= jobs[i]
            if workloads[j] == 0:
                break
        return False
    
    return backtrack(0)

# Binary search to find the minimum possible maximum working time
left, right = max(jobs), sum(jobs)
while left < right:
    mid = (left + right) // 2
    if can_finish(jobs, k, mid):
        right = mid
    else:
        left = mid + 1

# Output the result
result = left
print(result)  # Expected output: 3
