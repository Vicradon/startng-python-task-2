import unittest

import user_details_collector


class TestInputs(unittest.TestCase):
    def test_email(self):
        "Test that a valid email returns true"
        email1 = "vicraph7@gmail.com"
        email2 = "vicraph7@gmail"
        result1 = user_details_collector.isValidEmail(email1)
        result2 = user_details_collector.isValidEmail(email2)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    # The next two tests fail for some reason
    def test_firstName(self):
        "Tests that the first name is valid"
        firstName = "Osinachi"
        result = user_details_collector.validateNames(firstName, "first name")
        self.assertIsNone(result)

    def test_lastName(self):
        "Tests that the last name is valid"
        lastName = "Chukwujama"
        result = user_details_collector.validateNames(lastName, "last name")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
