import math

def is_perfect(n):
    div_sum = 1
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            div_sum += x
            if x != n // x:
                div_sum += n // x
    return div_sum == n and n != 1

per_num = [n for n in range(2,1000000) if is_perfect(n)]
print(per_num)