# Переворатор


n, x, y, a, b = map(int, input().split())

lst = [i for i in range(n + 1)]
lst[x: y + 1] = lst[y: x - 1: -1]
lst[a: b + 1] = lst[b: a - 1: -1]

print(*lst[1:])