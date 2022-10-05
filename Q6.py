# Prime number generator
def prime_generator(end):
    for n in range(2, end):     # n starts from 2 to end
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            yield n             # generate the prime


g = prime_generator(int(input()))       # give firt 1000 prime numbers
print(list(g))