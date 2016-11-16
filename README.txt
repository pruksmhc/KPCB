
KCBG Challenge:
Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). 

My solution:

Thiis solution has algorithmic runtime of the following:
1) Set: O(1) (No chaining possible, collision detection using linear probing under SUHA is O(1) amortized)
2) Delete: O(1) 
3) Get: O(1)
4) Load: O(1) 

Space complexity:
O(n), where n = size 

