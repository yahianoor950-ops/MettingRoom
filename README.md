# Meeting Rooms (Min-Heap)

CS314 – Heap Sort mini project #12.

Given a list of meetings `(start, end)`, find the **minimum number of rooms**
needed so that no two overlapping meetings share a room. A min-heap that stores
the end times of the rooms in use gives an `O(n log n)` solution.

## How it works

1. Sort meetings by start time.
2. Keep a min-heap of end times (one entry per room in use).
3. For each meeting:
   - if `heap[0] <= start` → the earliest room is free, reuse it (`heapreplace`);
   - otherwise → open a new room (`heappush`).
4. The heap size at the end = number of rooms.

| Operation | Complexity |
|-----------|-----------|
| Sorting   | O(n log n) |
| Heap ops  | O(n log n) |
| Space     | O(n) |

## Usage

```bash
python meeting_rooms.py          # run the demo
python -m unittest -v            # run the tests
```

```python
from meeting_rooms import min_meeting_rooms, assign_rooms

min_meeting_rooms([(0, 30), (5, 10), (15, 20)])   # -> 2
assign_rooms([(0, 30), (5, 10), (15, 20)])        # room for each meeting
```

Requires Python 3.8+ and no external packages.

## Files

- `meeting_rooms.py` – solution + demo
- `test_meeting_rooms.py` – unit tests (includes random check vs. a sweep-line brute force)
