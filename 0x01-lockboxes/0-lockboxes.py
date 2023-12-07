#!/usr/bin/python3
'''LockBoxes interview'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    keys = boxes[0]
    while keys:
        key = keys.pop(0)
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])

    return all(unlocked_boxes)
