#!/usr/bin/python3

def canUnlockAll(boxes):
    """
        boxes:  list of lists
    """
    array_keys = []
    len_boxes = len(boxes)
    count = 0

    for key in boxes[0]:
        if key not in array_keys and key < len_boxes and key > 0:
            array_keys.append(key)
            count += 1

    index = 0
    while index < len(array_keys):
        setkey = array_keys[index]
        for key in boxes[setkey]:
            if key not in array_keys and key < len_boxes and key > 0:
                array_keys.append(key)
                count += 1
        index += 1

    if (count == len_boxes-1):
        return True
    else:
        return False
