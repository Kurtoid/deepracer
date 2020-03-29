import math
def reward_function(params):
    # incentivize speed, while remaining on track

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    
    reward = math.sqrt(speed/0.8)

    # Penalize reward if the car is steering too much
    if not (all_wheels_on_track): 
        reward *= 0.8

    return float(reward)
