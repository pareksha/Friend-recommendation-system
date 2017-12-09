import unittest
import network_functions


class TestGetAverageFriendCount(unittest.TestCase):

    def test_get_average_empty(self):
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_one_person_many_friends(self):
        param = {'Alex Dunphy': ['Gloria Pritchett','Mitchell Pritchett']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_floating_value(self):
        param = {'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':
    ['Gloria Pritchett','Mitchell Pritchett']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_long_floating_value(self):
        param = {'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':
    ['Gloria Pritchett','Mitchell Pritchett'], 'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.3333333333333333
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_same_number_of_friends(self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett',
                                   'Manny Delgado'], 'Claire Dunphy':
            ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 3
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_many_people_many_friends(self):
        param = {'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
                 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money':
                     ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
                 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado',
                                 'Mitchell Pritchett', 'Phil Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


if __name__ == '__main__':
    unittest.main()