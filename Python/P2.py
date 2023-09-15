import time

def sum(limit):
    a, b = 1, 2
    sum = 0

    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b

    return sum

tic = time.perf_counter()
sum = sum(4000000)
toc = time.perf_counter()
print(f"Summed in {toc - tic:0.8f} seconds")
print(sum)
