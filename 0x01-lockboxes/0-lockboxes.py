#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Check if it's possible to unlock all the boxes based on a set of keys.

    Parameters:
    - boxes (List[List[int]]): A list of lists.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    array_keys = []
    len_boxes = len(boxes)
    count = 0

    for key in boxes[0]:
        if key not in array_keys and 0 < key < len_boxes:
            array_keys.append(key)
            count += 1

    index = 0
    while index < len(array_keys):
        setkey = array_keys[index]
        for key in boxes[setkey]:
            if key not in array_keys and 0 < key < len_boxes:
                array_keys.append(key)
                count += 1
        index += 1

    return count == len_boxes - 1
