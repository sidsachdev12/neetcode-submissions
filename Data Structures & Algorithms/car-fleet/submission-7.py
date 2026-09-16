class Solution:
    def position_to_insert(self, arr, pos):
        start, end = 0, len(arr) - 1
        res = end

        while start <= end:
            mid = (start + end) // 2

            if pos >= arr[mid][0]:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res

    def timeToDestination(self, pos, speed, target):
        return (target - pos) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_with_speed = []

        for pos, sp in zip(position, speed):
            # pos_with_speed.insert(self.position_to_insert(pos_with_speed, pos), [pos, sp])
            pos_with_speed.append((pos, sp))

        pos_with_speed.sort()

        # stack
        fleet = []

        while pos_with_speed:
            pos, sp = pos_with_speed.pop()

            if len(fleet) == 0:
                fleet.append(self.timeToDestination(pos, sp, target))
            else:
                top = fleet[-1]
                curr_time = self.timeToDestination(pos, sp, target)

                if curr_time <= top:
                    continue
                else:
                    fleet.append(curr_time)

        return len(fleet)
