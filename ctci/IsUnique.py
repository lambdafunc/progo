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
    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True

