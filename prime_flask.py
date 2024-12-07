from flask import Flask, request
import math, time

app = Flask(__name__)


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


@app.route('/')
def index():
    start_time = time.time()
    prime_count = count_primes(3000000)
    end_time = time.time()

    return f'''
        <p>素数の数: {prime_count}</p>
        <p>計算時間: {end_time - start_time} 秒</p>
        '''


app.run()
