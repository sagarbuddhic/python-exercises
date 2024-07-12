


# tuple values

tuple = (3, 2,1)
x, y, z = tuple
print(y)

# objects

customers = {
  "name": "sagar",
  "age": "40"
}

print(customers.get("name1"))

# def

def add(a, b):
    return a + b


added = add(2, 3)

print(added)

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid Value")


    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

            point = Point(1, 2)
            print(point.x)