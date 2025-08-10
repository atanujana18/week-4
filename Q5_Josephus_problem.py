def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n - 1, k) + k) % n
n = 7
k = 3
print(josephus(n, k) + 1)