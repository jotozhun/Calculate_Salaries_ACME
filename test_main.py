import unittest
from main import calculateSalary, validateSchedule

class TestMain(unittest.TestCase):

    # Tests for validateSchedule function

    def test_good_formated_schedule(self):
        schedule = list("MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00".split(","))
        self.assertEqual(validateSchedule(schedule), True)

    def test_wrong_day_code(self):
        schedule = "SU08:00-09:00,SR09:00-16:00"    # SR is not a day code
        self.assertEqual(validateSchedule(schedule), False)
        
    def test_start_greater_than_end_hour(self):
        schedule = list("MO10:00-13:00,TU10:00-13:00,WE14:00-13:00,TH10:00-13:00,SU19:00-22:00".split(",")) # WE start is 14:00 and end 13:00
        self.assertNotEqual(validateSchedule(schedule), True)

    def test_start_equals_end_hour(self):
        schedule = list("MO10:00-13:00,TU10:00-13:00,WE13:00-13:00,TH10:00-13:00,SU19:00-22:00".split(","))
        self.assertEqual(validateSchedule(schedule), False)

    def test_end_hour_equals_zero(self):
        schedule = list("TU13:00-18:00,WE09:00-14:00,TH09:00-15:00,FR02:00-08:00,SA19:00-00:00".split(","))
        self.assertEqual(validateSchedule(schedule), True)


    # Tests for Calculate Salary function
    # This function doesn't need a bad format test because validateSchedule function is in charge of it

    def test_right_salary_calculation(self):
        schedule1 = list("MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00".split(","))
        schedule2 = list("TU13:00-18:00,WE10:00-14:00,TH09:00-15:00,FR02:00-08:00".split(","))
        
        self.assertAlmostEqual(calculateSalary(schedule1), 215)
        self.assertAlmostEqual(calculateSalary(schedule2), 375)

    def test_zero_end_hour_calculation(self):
        schedule = list("TU13:00-18:00,WE09:00-14:00,TH09:00-15:00,FR02:00-08:00,SA19:00-00:00".split(","))
        self.assertEqual(calculateSalary(schedule), 515)

if __name__ == '__main__':
    unittest.main()