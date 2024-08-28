# lab_1_output.py

def process_even(item):
    return item ** 2

def process_odd(item):
    return item ** 3

def adjust_value(value, item):
    if item > 50:
        return value - 10
    elif item < 20:
        return value + 10
    return value

def simulate_complex_processing(value):
    for i in range(5):
        value += i
    return value

def refactored_method(data):
    result = []
    for item in data:
        if item % 2 == 0:
            processed_value = process_even(item)
        else:
            processed_value = process_odd(item)
        
        adjusted_value = adjust_value(processed_value, item)
        final_value = simulate_complex_processing(adjusted_value)
        
        result.append(final_value)
    
    return result

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
print(refactored_method(data))
