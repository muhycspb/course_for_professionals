# Тимур, Артур и новый курс


d1, d2, d3 = (int(input()) for _ in range(3))
print(sum((min(d1, d2 + d3), min(d2, d1 + d3), min(d3, d1 + d2))))
