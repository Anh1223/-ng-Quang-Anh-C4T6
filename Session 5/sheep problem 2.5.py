size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my ship sizes")
print(size)
for i in range(1, 4):
    print("MONTH", i, ":")
    print("One month has passed, here is my flock")
    size = [x + 50 for x in size]
    print(size)
    print("Now my biggest ship has size", max(size), "let's shear it")
    max_index = size.index(max(size))
    size[max_index] = 8
    print("After shearing, here is my flock")
    print(size)
