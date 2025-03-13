def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    else:
        counter = 2
        primes = [2]
        while number > len(primes):
            counter += 1
            for p in primes:
                if counter % p == 0:
                    break
            else:
                primes.append(counter)
        return primes[-1]
