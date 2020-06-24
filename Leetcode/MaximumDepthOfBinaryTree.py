# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:46:44 2020

@author: Vishnu
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxdepth(root):
    if not root:
        return 0
    return 1+max(maxdepth(root.left)+maxdepth(root.right))
