import unittest
from src.main.python import driver


class KNearestPointsTest(unittest.TestCase):
    """ Test class for Colors and PieceType representations """

    def test_distance_function(self):
        vertex = [1,2]
        point = [1,2]
        actual = driver.get_distance(vertex, point)
        expected = 0

        self.assertEqual(expected, actual)

    def test_distance_from_1_2_to_1_3_is_1(self):
        vertex = [1,2]
        point = [1,3]
        actual = driver.get_distance(vertex, point)
        expected = 1

        self.assertEqual(expected, actual)

    def test_distance_from_1_0_to_3_1_is_sqrt_5(self):
        vertex = [1,0]
        point = [3,1]
        actual = driver.get_distance(vertex, point)
        expected = 5 ** .5

        self.assertEqual(expected, actual)

    def test_sort_list_of_points_from_vertex(self):
        points = [[10,10], [1,2], [2,3]]
        vertex = [1,2]

        actual = driver.sort_points(vertex, points)
        expected = [[1,2], [2,3], [10,10]]

        self.assertEqual(expected, actual)


