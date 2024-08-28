# lab_1_input.py

def long_method(data):
    result = []
    for item in data:
        if item % 2 == 0:
            squared = item ** 2
            result.append(squared)
        else:
            cubed = item ** 3
            result.append(cubed)
        # Processing further conditions
        if item > 50:
            result[-1] = result[-1] - 10
        elif item < 20:
            result[-1] = result[-1] + 10
        # Simulating some complex processing
        for i in range(5):
            result[-1] += i
    return result

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
print(long_method(data))
