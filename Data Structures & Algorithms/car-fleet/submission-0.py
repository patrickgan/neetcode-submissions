"""
target = 10, position = [1,4], speed = [3,2]
target = 10, position = [4,1,0,7], speed = [2,2,1,1]

naive: iterate through each time frame? (downside: if target is extremely high and speed low, this takes many iterations)
to simplify, we assume they are sorted. if the solution is O(n log n) or greater, this is free.
to improve on this, we process by greatest position
calculate the number of turns for each car. if car $i has a better time than car $(i-1), set car $i time to car $(i-1) time

Sorting:
sorted_pos = sorted([(pos, i) for pos in positions])
sorted_spd = [speed[i] for (pos, i) in sorted_pos]

Time:
raw_time = (target - pos) / spd
actual_time = max(time_of_ahead_car, raw_time)

positions: [4,1], speed: [2,3], target: 10
time (car 0) = (10-4)/2 => 3 turns
time (car 1) = (10-1)/3 => 3 turns (same fleet) # this number can only be the same or worse than the one in front of it
1 fleet

what if it's fast enough to catch up?
positions: [4,1], speed: [2,4], target: 10
time (car 0) = (10-4)/2 => 3 turns
time (car 1) = (10-1)/4 => 2 turns => 3 turns
1 fleet

what if more fleets, cars?
positions: [4,1,0], speed: [2,1,2], target: 10
time (car 0) = ...      => 3 turns
time (car 1) = (10-1)/1 => 9 turns
time (car 2) = (10-0)/2 => 5 turns => 9 turns (same as car ahead)

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = sorted([(pos, i) for (i, pos) in enumerate(position)], reverse=True)
        times = []
        for pos, i in sorted_positions:
            spd = speed[i]
            time = (target - pos) / spd
            if not times:
                times.append(time)
            elif time > times[-1]:
                times.append(time)
        return len(times)
