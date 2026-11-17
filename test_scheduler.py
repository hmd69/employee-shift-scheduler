import unittest
from scheduler import add_shift, get_sorted_shifts, has_conflict


class TestShiftScheduler(unittest.TestCase):
    def setUp(self):
        self.sample_shifts = [
            {
                "id": 1,
                "employee": "Alice",
                "role": "Server",
                "day": "Wednesday",
                "start": "11:30",
                "end": "15:30",
            },
            {
                "id": 2,
                "employee": "Marc",
                "role": "Chef",
                "day": "Monday",
                "start": "10:00",
                "end": "16:00",
            },
        ]

    def test_get_sorted_shifts(self):
        sorted_list = get_sorted_shifts(self.sample_shifts)
        self.assertEqual(sorted_list[0]["day"], "Monday")
        self.assertEqual(sorted_list[1]["day"], "Wednesday")

    def test_add_shift_success(self):
        success, msg = add_shift(
            self.sample_shifts, "Claire", "Host", "Tuesday", "18:00", "23:00"
        )
        self.assertTrue(success)
        self.assertEqual(len(self.sample_shifts), 3)
        self.assertEqual(self.sample_shifts[-1]["id"], 3)

    def test_add_shift_conflict(self):
        success, msg = add_shift(
            self.sample_shifts, "Alice", "Server", "Wednesday", "18:00", "22:00"
        )
        self.assertFalse(success)
        self.assertIn("Conflict", msg)
        self.assertEqual(len(self.sample_shifts), 2)

    def test_has_conflict_case_insensitive(self):
        self.assertTrue(has_conflict(self.sample_shifts, "alice", "wednesday"))
        self.assertFalse(has_conflict(self.sample_shifts, "Alice", "Friday"))

    def test_add_shift_invalid_day(self):
        success, msg = add_shift(
            self.sample_shifts, "Lucas", "Server", "Funday", "10:00", "14:00"
        )
        self.assertFalse(success)
        self.assertIn("Invalid day", msg)


if __name__ == "__main__":
    unittest.main()
