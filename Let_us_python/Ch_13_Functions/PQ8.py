def create_array(x, y, z, value):
    # Creating 3D array
    array = []

    for i in range(x):
        layer = []
        for j in range(y):
            row = []
            for k in range(z):
                row.append(value)
            layer.append(row)
        array.append(layer)

    return array


# Calling function
arr = create_array(2, 3, 4, 10)

print(arr)