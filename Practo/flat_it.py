
def flat_it(nested_list):
    """
    Function will return flattend list of given nested list
    :param nested_list: [1, 2, [3, 4], [[5, 6], [7, 8]]]
    :return: results = [1, 2, 3, 4, 5, 6, 7, 8]
    """
    results = []
    for item in nested_list:
        if type(item) is int:
            results.append(item)
        else:
            results += flat_it(item)
    return results
