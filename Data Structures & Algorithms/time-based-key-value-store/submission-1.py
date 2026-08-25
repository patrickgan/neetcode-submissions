"""
Timestamp search

Edge cases:
* if no values, return ""
* if all values are greater, return ""
* if all values are lesser, return values[-1]
* (optional: if final value is equal to timestamp, return values[-1])
    * this case is covered by just running the right half until we get only one value.
pivot = (right - left) // 2 + left
* if pivot value is equal to timestamp, return values[pivot]
* if pivot value is greater than timestamp, check left remaining half. (values[left:pivot])
* if pivot value is less than timestamp, check right remaining half, inclusive. (values[pivot:right])

1 3 5 [6] 7 .. | search 2
-> 1 [3] 5
-> 1 => return values["1"]

345678 ... 200 => search 4
=> 345678... 60
... 
=> 34[5]678
=> 34

1 3 5 [6] 7 .. | search 4
-> 1 [3] 5
-> [3] 5

1 2 3 [199] 200 204   | search 7
-> 1 2 3 => return values['3']

12345 | search 7 => return values['5']

1 3 199 200 204   | search 201

1 3 6 7 9 | search 0
-> return ""

0 51 101 | search 50
pivot = '0'
left = '0'

"""

class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(value, timestamp)]
        else:
            self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        if not values or timestamp < values[0][1]:
            return ""
        if timestamp > values[-1][1]:
            return values[-1][0]
        last_guess = ""
        left, right = 0, len(values) - 1
        while left <= right:
            pivot = (right - left) // 2 + left
            if timestamp == values[pivot][1]:
                return values[pivot][0]
            elif timestamp < values[pivot][1]:
                right = pivot - 1
            elif timestamp > values[pivot][1]:
                last_guess = values[pivot][0]
                left = pivot + 1 # check this condition
        return last_guess
            