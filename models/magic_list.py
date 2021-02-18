"""
a file contains the magic list class
"""


class MagicList(list):
    """
    a class represents a magic list
    """
    def __init__(self, cls_type: type = None):
        if cls_type:
            obj: cls_type = cls_type()
            self[0] = obj

    def __setitem__(self, index: int, value):
        self.extend([None])
        super().__setitem__(index, value)
