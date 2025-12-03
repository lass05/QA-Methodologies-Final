import unittest
from can_drive import can_drive
class TestCanDrive(unittest.TestCase):
    def test_age_below_driving_age_returns_false(self): self.assertFalse(can_drive(15))
    def test_age_equal_to_driving_age_returns_true(self): self.assertTrue(can_drive(16))
    def test_age_above_driving_age_returns_true(self): self.assertTrue(can_drive(18))
    def test_zero_age_returns_false(self): self.assertFalse(can_drive(0))
    def test_negative_age_returns_false(self): self.assertFalse(can_drive(-1))
if __name__ == "__main__": unittest.main()
