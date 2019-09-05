# Import the python testing framework
import unittest
# Our "unit"
# This is what we are running our test on



def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list


def anotherFunction(list):
    pass




# Our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class reverseArrayTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([5,1,2,3], [3,2,1,5])
    # any task you want to run before any method above is executed put them in the same
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want to run after the tests are executed, put them in the tearDown
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")





class anotherFunctionTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([5,1,2,3], [3,2,1,5])
    # any task you want to run before any method above is executed put them in the same
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want to run after the tests are executed, put them in the tearDown
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()         # This runs our tests



# .assertEqual(a,b)
# .assertNotEqual(a,b)
# .assertTrue(x)
# .assertFalse(x)
# .assertIs(a,b)
# .assertIsNot(a,b)
# .assertIsNone(x)
# .assertIsNotNone(x)
# .assertIn(a,b)
# .assertNotIn(a,b)
# .assertIsInstance(a,b)
# .assertIsNotInstance(a,b)
