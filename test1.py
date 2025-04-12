def __init__paramters(text_file_name):
    with open(text_file_name) as paramters_file:
        zoo_dimentions = eval(paramters_file.readline())
        drone_depot = eval(paramters_file.readline())
        battery_distance_capacity = eval(paramters_file.readline())    


        line = paramters_file.readline().strip()
        line = line[1:-1]
        tuple_strings = line.split('),(')

        food_storage_coordinates = []
        for entry in tuple_strings:
            entry = entry.strip('()')
            parts = entry.split(',')
            *nums, label = parts
            nums = [int(n) for n in nums]
            food_storage_coordinates.append(tuple(nums + [label]))

        
        #enclosures
        line = paramters_file.readline().strip()
        line = line[1:-1] 
        tuple_strings = line.split('),(')

        enclosures = []
        for entry in tuple_strings:
            entry = entry.strip('()')
            parts = entry.split(',')
            x, y, z = map(int, parts[:3])
            importance = float(parts[3])
            diet = parts[4].strip().strip('"') 
            enclosures.append((x, y, z, importance, diet))

    return zoo_dimentions, drone_depot, battery_distance_capacity, food_storage_coordinates, enclosures


zoo_dimentions, drone_depot, battery_distance_capacity, food_storage_coordinates, enclosures = __init__paramters('1.txt')