def shuffleString(x, n):
    import random
    result = []
    for i in range (n):
        randomString = ''.join(random.sample(x, len (x)))
        result.append(randomString)
    print(result)
    return result
    
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 3)


