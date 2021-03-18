import time


def zeef(n):
    num_lst = [i for i in range(2, n + 1)]
    prime_bools = [1 for i in range(2, n + 1)]
    k = 2
    while k**2 <= n:
        for x in range(len(num_lst)):
            if num_lst[x] % k == 0 and num_lst[x] != k:
                prime_bools[x] = 0

        # calc for smallest num that still has 1 (True) for value
        for y in range(len(num_lst)):
            if prime_bools[y] == 1 and num_lst[y] > k:
                k = num_lst[y]
                break


start = time.time()
zeef(1000000)
end = time.time()
print(end-start)
