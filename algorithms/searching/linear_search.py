def linear_search_iterative(list_elements, element):
    """
    Implementation of a linear search iterative
    :param list_elements:
    :param element:
    :return: the index where the element was found or -1 if the element is no in the list
    """
    i = 0
    while i < len(list_elements):
        if list_elements[i] == element:
            return i
        i += 1

    return -1

