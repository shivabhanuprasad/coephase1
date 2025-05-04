# Function to check if two tuples are equal
def equal(tuple1, tuple2):
    return tuple1 == tuple2

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)

print("tuple1 and tuple3 are equal", equal(tuple1, tuple2))
print("Are tuple1 and tuple3 equal?", equal(tuple1, tuple3))
