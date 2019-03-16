# O(N)

import unittest

def unique(string):
    '''
    Approach here is that we will create a bool list of 128 chars set to 'False',
    then we will iterate through our given string,
    then we will find the "order" of given char.
    then we will check if that is True for "char_set", if thats first occurence,
    it will set bit to true and will continue, once it encounter repeated char,
    condition will return false and will exited.
    Use PyCharm Debugger to make life easy.
    '''
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
