"""Meeting Rooms - minimum number of rooms needed using a min-heap of end times.

Idea: sort meetings by start time. The heap keeps the end time of every
room currently in use. The room that frees up first is always heap[0].
- If that room is free before the new meeting starts, reuse it.
- Otherwise, open a new room.
The final heap size is the answer.

Time complexity: O(n log n)   Space complexity: O(n)
"""

import heapq
from typing import List, Sequence, Tuple

Meeting = Tuple[int, int]


def _validate(meetings: Sequence[Meeting]) -> None:
    for m in meetings:
        if len(m) != 2:
            raise ValueError(f"Meeting must be (start, end), got {m!r}")
        start, end = m
        if start >= end:
            raise ValueError(f"Start must be before end, got {m!r}")


def min_meeting_rooms(meetings: Sequence[Meeting]) -> int:
    """Return the minimum number of rooms needed to host all meetings."""
    _validate(meetings)
    if not meetings:
        return 0

    heap: List[int] = []  # end times of rooms in use
    for start, end in sorted(meetings, key=lambda m: m[0]):
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)  # reuse the room that frees first
        else:
            heapq.heappush(heap, end)  # need a new room
    return len(heap)


def assign_rooms(meetings: Sequence[Meeting]) -> List[Tuple[int, Meeting]]:
    """Return a (room_number, meeting) pair for each meeting (rooms start at 1)."""
    _validate(meetings)
    heap: List[Tuple[int, int]] = []  # (end_time, room_id)
    free_ids: List[int] = []
    next_id = 1
    result: List[Tuple[int, Meeting]] = []

    for start, end in sorted(meetings, key=lambda m: m[0]):
        while heap and heap[0][0] <= start:
            _, room = heapq.heappop(heap)
            heapq.heappush(free_ids, room)
        if free_ids:
            room = heapq.heappop(free_ids)
        else:
            room = next_id
            next_id += 1
        heapq.heappush(heap, (end, room))
        result.append((room, (start, end)))
    return result


def main() -> None:
    meetings = [(0, 30), (5, 10), (15, 20), (25, 40), (35, 45)]
    print("Meetings:", meetings)
    print("Minimum rooms needed:", min_meeting_rooms(meetings))
    print("\nSchedule:")
    for room, (s, e) in sorted(assign_rooms(meetings)):
        print(f"  Room {room}: {s} -> {e}")


if __name__ == "__main__":
    main()
