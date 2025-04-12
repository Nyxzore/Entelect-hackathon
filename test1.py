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
def score(pi , TD): #pi = priorities, TD = total distance
    weighted_sum = 0
    for priority_multiplier in pi:
        weighted_sum += priority_multiplier * 1000
    return weighted_sum  - TD


#shortest path
def twod_euclid_distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def feed(feeding_order): #hoc
    route = []
    TD = 0
    drone_coords = [drone_depot[0],drone_depot[1]] # intitial drone coords
    route.append(tuple(drone_coords))

    __init__distance = zoo_dimentions[2]-drone_depot[2] # drone flying up to zoo height from the depot
    TD += __init__distance 
    for diet in feeding_order:
        #get current food storage
        for coords in food_storage_coordinates:
            if feeding_order[0] in coords:
                current_food_storage =  list(coords)[:-1]

        #travel to food storage
        TD += twod_euclid_distance(drone_coords, current_food_storage)
        drone_coords = current_food_storage[:-1]
        route.append(drone_coords)
        #pick up food storage
        TD += 2*(zoo_dimentions[2]-current_food_storage[2]) # moving down and back up

        enclosures_to_feed = [enclosure for enclosure in enclosures if (feeding_order[0] in enclosure)]
        #distances to next various enclosures
        def dist(drone_coord, enclosure):
            return twod_euclid_distance(drone_coord, (enclosure[0], enclosure[1]))

        #feed every animal of that type
        while len(enclosures_to_feed)> 0:
            distances = [dist(drone_coords,enclosure) for enclosure in enclosures_to_feed]
        
            closest_enclosure = enclosures_to_feed[distances.index(min(distances))]

            #travel to enclosure
            TD += twod_euclid_distance(drone_coords, closest_enclosure[:2])
            drone_coords = closest_enclosure[:2]
            route.append(drone_coords)
            #feed animal
            TD += 2*(zoo_dimentions[2]-closest_enclosure[2]) # moving down and back up
            enclosures_to_feed.remove(closest_enclosure)


    #
    summedPrioH = 0.0
    summedPrioC = 0.0
    summedPrioO = 0.0
    for i in range(len(enclosures) - 1): #sums up the priority, grouped by diet (h,c,o)
        if enclosures[i][4] == "h":
            summedPrioH += float(enclosures[i][3]) *1000
        elif enclosures[i][4] == "c":
            summedPrioC += float(enclosures[i][3]) *1000
        else:
            summedPrioO += float(enclosures[i][3]) *1000 
    priority_sum = summedPrioH + summedPrioO + summedPrioC  
    return route, priority_sum - TD


def shortest_distance():
    routes = ['hco', 'hoc', 'och', 'ohc', 'coh', 'cho']
    min_score = None
    min_route = None

    for route in routes:
        score = feed(route)
        if min_score is None or score < min_score:
            min_score = score
            min_route = route

    return min_route, min_score

print(shortest_distance())
