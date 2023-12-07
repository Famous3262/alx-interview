#!/usr/bin/python3
'''LockBoxes interview'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    num_boxes = len(boxes)
    keys = set()
    unlocked_boxes = []
    i = 0

    while i < num_boxes:
        oldi = i
        unlocked_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < num_boxes and key not in unlocked_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(num_boxes):
        if i not in unlocked_boxes and i != 0:
            return False
    return True
