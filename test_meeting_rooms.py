import random
import unittest

from meeting_rooms import assign_rooms, min_meeting_rooms


def brute_force(meetings):
    """Sweep-line check: max number of overlapping meetings."""
    events = []
    for s, e in meetings:
        events.append((s, 1))
        events.append((e, -1))  # -1 sorts before +1 at same time
    events.sort()
    cur = best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best


class TestMeetingRooms(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(min_meeting_rooms([]), 0)

    def test_single(self):
        self.assertEqual(min_meeting_rooms([(1, 2)]), 1)

    def test_no_overlap(self):
        self.assertEqual(min_meeting_rooms([(1, 2), (2, 3), (3, 4)]), 1)

    def test_all_overlap(self):
        self.assertEqual(min_meeting_rooms([(1, 5), (2, 6), (3, 7)]), 3)

    def test_example(self):
        self.assertEqual(
            min_meeting_rooms([(0, 30), (5, 10), (15, 20), (25, 40), (35, 45)]), 2
        )

    def test_invalid(self):
        with self.assertRaises(ValueError):
            min_meeting_rooms([(5, 5)])

    def test_random_against_brute_force(self):
        rng = random.Random(42)
        for _ in range(300):
            meetings = []
            for _ in range(rng.randint(0, 30)):
                s = rng.randint(0, 50)
                meetings.append((s, s + rng.randint(1, 20)))
            self.assertEqual(min_meeting_rooms(meetings), brute_force(meetings))

    def test_assignment_has_no_conflicts(self):
        rng = random.Random(7)
        meetings = []
        for _ in range(40):
            s = rng.randint(0, 60)
            meetings.append((s, s + rng.randint(1, 15)))
        assigned = assign_rooms(meetings)
        self.assertEqual(len({r for r, _ in assigned}), min_meeting_rooms(meetings))
        by_room = {}
        for room, m in assigned:
            by_room.setdefault(room, []).append(m)
        for ms in by_room.values():
            ms.sort()
            for (_, e1), (s2, _) in zip(ms, ms[1:]):
                self.assertLessEqual(e1, s2)


if __name__ == "__main__":
    unittest.main()
