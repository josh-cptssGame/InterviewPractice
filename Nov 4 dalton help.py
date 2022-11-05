
"""
Playground



class Node
    val   (int)
    left  (Node)
    right (Node)


    1
 5     4
8 2   9 12


BFS: 1, 5, 4, 8, 2, 9, 12
DFS: 1, 5, 8, 2, 4, 9, 12


Breadth-First-Search

* Use a queue
* []
* Check if anything in queue to do? Nope, so add next node to queue, which is 1
* [1]
* Check if queue isn't empty, which it's not, so grab leading value in queue
* [], processing 1, and we add all of node 1's children to queue
* [5,4]
* Check if queue isn't empty, which it's not, so grab leading value in queue, which is 5
* [4], processing 5, and we add all of node 5's children to queue
* [4, 8, 2]
* ... repeat


Node
    val
    children (List of Nodes)

1: 3 children ([2,1,7])
2: 1 child ([45])


So far, solved for different tree
  * Trees have parent->child relationship

Graph
  * Similar to trees
  * Instead of parent->child, graphs have siblings

1 -> 5 -> 2
^---------|




"""

def bfs(root):
    q = []
    # root is a Node, which has fields: val (int), left (Node), right (Node)
    #    -> if child missing, left or right will be None (Python's variant of null)
    #
    # q.add(x) -> adds to end of queue
    # q.pop() -> returns front value of queue
    hold = root
    q.add(hold)
    s = {} # Set: unique collection of objects (things), at most one of each unique thing
    # s.add(x)
    # s.contains(x) -> returns true or false
    while q:
        temp = q.pop()
        if temp not in s:
            for child in q.children:
                q.add(child)

            s.add(temp)
        # if temp.left:
        #     q.add(temp.left)
        # if temp.right:
        #     q.add(temp.right)
        print(temp.val)




def search_improved(sorted_nums, num_to_find):
    if_Found = False
    lower = 0
    higer = len(sorted_nums)
    half = len(sorted_nums)/2
    while not if_Found:
        if sorted_nums[half] == num_to_find:
            return half
        elif lower == half or higer == half: # [5] 
            return -1
        elif sorted_nums[half] > num_to_find:
            # 0, 25, 50
            # Current strategy produces new half of 12ish
            #
            # 40, 50, 60
            # Current strategy produces? 
            # 0,1
            temp = (lower + half)/2
            higer = half
            half = temp
        elif sorted_nums[half] < num_to_find:
            temp = (higer + half)/2
            lower = half
            half = temp

    return -1   
            


def search_simple(sorted_nums, num_to_find):
    # for i in range(len(list_name)):
    for i in range(len(sorted_nums)):
        if sorted_nums[i] == num_to_find:
            return i

    #else return -1
    return -1

# Input: sorted list of integers, and item to find in list
# Ouput: index of item, or -1 if item is not in list
#
# Example: search([1,3,7,11,20], 7) -> returns 2
# Example: search([1,3,7,11,20], 6) -> returns -1
