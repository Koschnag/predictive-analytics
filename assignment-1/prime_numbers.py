#function to check if a number is prime from 100 to 200
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#function to find all prime numbers from 100 to 200
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

#function to display the prime numbers
def display_primes(primes):
    print("Die Primzahlen zwischen 100 und 200 sind:")
    for prime in primes:
        print(prime, end=" ")
    print()  # Neue Zeile nach der Ausgabe
    
#main function to execute the program
def main():
    start = 100
    end = 200
    primes = find_primes(start, end)
    display_primes(primes)
#execute the main function
if __name__ == "__main__":
    main()