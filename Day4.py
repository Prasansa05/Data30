
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)

with open("primes.txt", "w") as file:
    file.write("Prime numbers between 1 and 100:\n")
    for prime in prime_numbers:
        file.write(str(prime) + "\n")

print("Prime numbers saved successfully in 'primes.txt'")
