
import unittest

import outing_repo


class TestOuting(unittest.TestCase):

    def test_create_outing_should_add_item(self):
        # Arrange - Setup variables
        # Act - Perform test
        outing_repo.create_outing('event_type', 'event_date', 100 , 12)
        expected = 1
        actual = len(outing_repo.outings)
        # Assert - Check output
        self.assertEqual(expected, actual)

    def test_get_outings_should_return_list_of_outings(self):
        expected = outing_repo.get_outings
        actual = outing_repo.get_outings
        self.assertEqual(expected, actual)

    def test_get_cost_should_return_cost_of_outing(self):
        expected =  1200
        actual = outing_repo.get_cost(outing_repo.outings)
        self.assertEqual(expected, actual)

