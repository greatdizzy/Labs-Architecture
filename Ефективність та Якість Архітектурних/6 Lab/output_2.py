# output_2.py

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_total(self):
        return sum(self.data)

    def calculate_average(self):
        count = len(self.data)
        return self.calculate_total() / count if count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None

# Приклад використання класу
data = [10, 20, 30, 40, 50]
analyzer = DataAnalyzer(data)
print("Total:", analyzer.calculate_total())
print("Average:", analyzer.calculate_average())
print("Minimum:", analyzer.calculate_minimum())
print("Maximum:", analyzer.calculate_maximum())
