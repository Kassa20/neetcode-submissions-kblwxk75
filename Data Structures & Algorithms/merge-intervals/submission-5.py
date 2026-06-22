class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()


        res = [intervals[0]]

        for i in range(1, len(intervals)):

            tail = res[-1]

            if intervals[i][0] <= tail[1]:
                tail[0] = min(tail[0], intervals[i][0])
                tail[1] = max(tail[1], intervals[i][1])
            else:
                res.append(intervals[i])


        return res

"""
TASK: merge overlapping intervals

My-idea:
# if a merges with b. i can merge them and 
add to result. then i will try to merge it
with another element that comes next.

[[1, 3] [1, 5] [6, 7]]

[1, 3] -> [1, 5] = [1, 5]
then i will try to merge [1, 5] with [6, 7]
they cant merge. [[1, 5], [6, 7]]

i need to start at the 2nd index and compare?
but what if they dont merge? that would skip the 
second index.

if the array was [[4, 5], [6, 7]]
these dont merge, and so res would be empty
-----------------------------
no. res would be [[4, 5]] and if they dont merge, 
we just append [6, 7] and if there happens to be 
another element that merges with [6, 7] (the tail)
we will update it. 
-----------------------------


The other problem, if they dont merge and 
i append [6, 7], what if i get [7, 9], 
now it must merge, but ive already added [6, 7]...
---------------------------
The solution: use the tail
(most recent array element) and update it Even if 
already added, it can be updated. This works since the 
array is sorted. 
---------------------------

"""