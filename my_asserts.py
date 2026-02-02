print("ex 1")

def square_positive(x):
    assert x > 0
    return x * x

print(square_positive(2))

print("\nex 2")

def first_item(items):
    assert len(items) > 0
    return items[0]

print(first_item([1,2,3,4,5]))

print("\nex 3")

def greet(name):
    assert type(name) == str
    return f"Hello, {name}"

print(greet("Bob"))


print("\nex 4")

def get_grade(score):
    assert score > 0 and score < 101
    return score

print(get_grade(100))

print("\nex 5")

def add_unique(items, item):
    assert not item in items
    items.append(item)
    return items


print(add_unique([1, 2, 3],4))

