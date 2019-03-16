# 1. Write a programme to check if a list has unique elements
import unittest
str = ["a", "y", "o", "g", "i", 1, 3, 0, 0]
def unique(str):
    if len(str) > 128:
       exit

    str2 = set(str)
    print(str)
    print(str2)
    if len(str) == len(str2):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_if_string_OK(self):
        str = ["yogii"]
        result = unique(str)
        expected = True
        self.assertEquals(result, expected)


    def test_if_duplicate(self):
        str = ["a", "y", "o", "g", "g"]
        result = unique(str)
        expected = False
        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main()


