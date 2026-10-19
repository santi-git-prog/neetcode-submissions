class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(x.start for x in intervals)
        end = sorted(x.end for x in intervals)

        rooms = 0
        max_rooms = 0
        i = 0
        j = 0

        while i < len(intervals):
            if start[i] < end[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1

        return max_rooms