import math, time


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0: return False
    return True


def count_primes(limit):
    count = 0
    for number in range(2, limit):
        if is_prime(number): count += 1
    return count


start_time = time.time()
print(f"素数の数: {count_primes(3000000)}")
end_time = time.time()

print(f"計算時間: {end_time - start_time}秒")
