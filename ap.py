from logging import root
from turtle import left, right


class Node():
    def __init__(self,data,left=None,right=None) :
        self.left =left
        self.right= right
        self.data= data


def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepth(root.right)+1
    if root.right is None:
        return minDepth(root.left)+1