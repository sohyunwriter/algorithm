# 접두사 합(Prefix Sum) 배열 계산
def solve_prefix_sum(data):
    sum_value = 0
    prefix_sum = [0]
    for i in data:
        sum_value += i
        prefix_sum.append(sum_value)
    return prefix_sum

#### test ####
# 구간 합 계산(3rd~4th)
prefix_sum = solve_prefix_sum(data=[10, 20, 30, 40, 50])
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])
