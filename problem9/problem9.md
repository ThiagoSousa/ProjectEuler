# Problem 9

# Solution 1
Three nested loops iterating through the variables a,b,c, check if their sum is equal to 1000 and it is a 
pythagorean triplet. There is a function to find if three numbers form a pythagorean triplet called 
`pythagorean_triplet`. Time complexity: O(n^3). 

# Solution 2
Small improvements, we just iterate through a and b and we get c by calculating `c=1000-a-b`. 
Time complexity: O(n^2).

# Solution 3:
Further improvement, we can infer b in terms of a: `b = (2000*a - 1000^2)/(2a-2000)` and `c=1000-a-b`. 
We just need to scan for a. Time complexity O(n).

