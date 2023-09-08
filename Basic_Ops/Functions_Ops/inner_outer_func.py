def calculation(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5


res = calculation(40, 50)
print(res)
