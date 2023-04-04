n =100
pos = 0
k = 2
for i in range(2, n + 1):
    pos = (pos + k) % i

pos += 1
pos
