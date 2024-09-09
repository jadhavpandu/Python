l=[1,2,3]

# approach 1
l+=[4]
print(l)
""" 
Approach 1: l += [4]

This is an in-place operation that modifies the list directly. The list is extended with one element, so the time complexity is O(1) (constant time) because we are only adding one element.

"""
l=l+[4]
print(l)
"""
# Approach 2: l = l + [4]

This creates a new list by concatenating l and [4]. Since a new list is created, it requires copying all the elements of l into a new list and then appending [4]. The time complexity is O(n), where n is the length of the list.
"""
l.append(4)
print(l)

"""
Approach 3: l.append(4)

The append() method adds an element to the end of the list in-place. The time complexity is O(1) (constant time), as no copying or resizing of the list is involved.
Best Approach:
Approach 1 (l += [4]) and Approach 3 (l.append(4)) both have O(1) time complexity and are the most efficient.
Approach 3 (l.append(4)) is generally preferred for readability and because it's a direct method for adding a single element to the list.
Approach 2 is the least efficient because it requires creating a new list, which is O(n).
Thus, Approach 3 (l.append(4)) is the best with respect to time.
 """









