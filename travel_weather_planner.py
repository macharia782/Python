#This project will use conditional statements to determine whether commuting possible 
# based on the weather, the distance to travel, and the availability of a vehicle.
distance_mi = 20
is_raining = True
has_bike = True
has_car = True
has_car_share_app = False

if not distance_mi:
    print(False)

if distance_mi >= 1 and is_raining == False:
    print(True)
else:
    print(False)

if distance_mi > 1 and distance_mi <= 6:
    if has_bike == True and is_raining == False:
        print(True)
else: 
    print(False)

if distance_mi > 6 and has_car == True or has_car_share_app == True:
    print(True)
else:
    print(False)




#Generated Correction Code

# 1. Correctly named variables as requested by the user stories
distance_mi = 20
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = False  # Fixed variable name here

# 2. Check for falsy values first
if not distance_mi:
    print(False)

# 3. Category A: less than or equal to 1 mile
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

# 4. Category B: greater than 1 mile AND less than or equal to 6 miles
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# 5. Category C: greater than 6 miles (handled safely by else)
else:
    # Parentheses ensure that distance > 6 applies to BOTH vehicle options
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
