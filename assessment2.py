
def find_primes(limit):
    primes = []

    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


# Ask user input
limit = int(input("Enter a number (max 100): "))

# Restrict to max 100
if limit > 100:
    print("Please enter a number up to 100 only.")
else:
    primes = find_primes(limit)

    # Display results
    print("Prime numbers found:", *primes)
    print("Total primes found:", len(primes))

    if primes:
        print("Largest prime:", max(primes))
        print("Smallest prime:", min(primes))
        print("Sum of all primes:", sum(primes))
    else:
        print("No prime numbers found.")