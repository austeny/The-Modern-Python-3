# def next_prime():
#     cur_num = 2
#     while True:
#         prime = True
#         for i in range(2, int(cur_num/2)+1):
#             if cur_num%i == 0:
#                 prime = False
#                 break
#         if prime: yield cur_num
#         cur_num += 1

def next_prime():
    num = 2
    all_primes = set()
    while True:
        for prime in all_primes:
            print(all_primes)
            if num % prime == 0:
                break
        else:
            all_primes.add(num)
            yield num
        num += num % 2 + 1

test = next_prime()
print(next(test))
print(next(test))
print(next(test))

all_primes = set()
print(all_primes)

for prime in all_primes:
    if num % prime == 0:
        print(num)
        break