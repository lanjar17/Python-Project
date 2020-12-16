#sum
def sum(*myData):
    sum = 0
    for data in myData:
        sum += data
    return sum


#average
def average(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data
        i += 1

    ratarata = sum/i
    return ratarata


#nilai maksimum
def maks(*myData):
    maksimum = 0

    for data in myData:
        if data > maksimum:
            maksimum = data
    return maksimum


#nilai minimum
def min(*myData):
    minimum = max(*myData) + 1

    for data in myData:
        if data < minimum:
            minimum = data
    return minimum



