Set: In the first solution, you use a set to keep track of characters you’ve seen so far in the substring. A set is great here for quick lookups (O(1)), but it only tracks whether a character is present, not its index.
HashMap (or Dictionary in Python): The second solution uses a hashmap to store each character along with its most recent index. This gives more information since it lets you know where the character was last seen. When you encounter a repeating character, you can jump directly to the next valid substring by updating the left pointer.
Why if doesn't work but while does:

In the set solution, using an if condition would only remove one occurrence of the duplicate, but multiple duplicates could exist in the substring. Using a while loop ensures you remove all previous duplicates to keep the window valid.
How to Use HashMap in the Function:

In the second solution, the hashmap stores each character’s most recent index. If a character is found again, you move the left pointer to ensure there are no duplicate characters between left and right. This method is more efficient than the set-based approach, as you can skip characters in one go instead of removing them one by one.