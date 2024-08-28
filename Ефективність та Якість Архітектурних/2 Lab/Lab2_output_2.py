class User:
    def __init__(self, name, age, gender, height, weight, scores):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.scores = scores

    def calculate_total_score(self):
        return sum(self.scores)

    def is_adult(self):
        return self.age >= 18

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Total Score:", self.calculate_total_score())
        print("Adult:", self.is_adult())

# Приклад виклику функції
user = User("John", 25, "Male", 175, 70, [85, 90, 75, 88, 92])
user.print_details()
