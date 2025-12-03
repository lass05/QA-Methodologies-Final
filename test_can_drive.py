import unittest
from can_drive import can_drive
class TestCanDrive(unittest.TestCase):
    # Test that an age below the legal driving age returns False
    def test_age_below_driving_age_returns_false(self): self.assertFalse(can_drive(15))
    
    # Test that exactly the legal driving age (16) returns True
    def test_age_equal_to_driving_age_returns_true(self): self.assertTrue(can_drive(16))
    
    # Test that any age above the legal driving age returns True
    def test_age_above_driving_age_returns_true(self): self.assertTrue(can_drive(18))
    
    # Test that age 0 (edge case) is not old enough to drive
    def test_zero_age_returns_false(self): self.assertFalse(can_drive(0))
    
    # Test that negative ages return False (invalid input)
    def test_negative_age_returns_false(self): self.assertFalse(can_drive(-1))
if __name__ == "__main__": unittest.main()
