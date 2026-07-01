class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Sort intervals by start time to process meetings chronologically
        intervals.sort(key=lambda x: x.start)

        def is_conflicting(one, two):
            return not (one.end <= two.start or two.end <= one.start)

        rooms = {}
        nums = 0

        for i in intervals:

            if nums == 0:
                nums += 1
                rooms[nums] = [i]
                continue

            meeting_added = False
            for n in range(1, nums + 1):
                conflict_present = False
                for r in rooms[n]:
                    conflict_present = conflict_present or is_conflicting(r, i)
                    if conflict_present:
                        break

                if not conflict_present:
                    rooms[n].append(i)
                    meeting_added = True
                    break

            if not meeting_added:
                nums += 1
                rooms[nums] = []
                rooms[nums].append(i)
            else:
                continue

        return nums