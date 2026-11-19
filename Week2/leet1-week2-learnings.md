#FizzBuzz - LeetCode 412

🐛 Bug Report & Post-Mortem: FizzBuzz Implementation

Status: Resolved
Language: Python
Problem: LeetCode 412 – Fizz Buzz

📋 Overview

An implementation of fizzBuzz(self, n) failed due to five distinct runtime and logical errors. While the two-pass approach (populating the list first, then mutating elements in place) is functionally valid, off-by-one boundary errors, operator misuse, and control-flow ordering prevented the code from executing properly.

🔍 Detailed Bug Analysis


1. Off-by-One Loop Boundary (IndexError)

• Problematic Code: for i in range(len(final)+1):
• Why It Is a Bug: Python lists use zero-based indexing. A list of length L has valid indices from 0 to L - 1. Adding + 1 forces the loop to attempt accessing final[len(final)] on the final iteration.
• Why It Won't Work: Attempting to read or write an index equal to the list's length immediately crashes the program with an IndexError: list index out of range.
• Rectification: Remove + 1 and iterate strictly over range(len(final)).

2. Incomplete Upper Bound in range()

• Problematic Code: for i in range(1, n):
• Why It Is a Bug: Python's range(start, stop) function is half-open, meaning it includes start but stops right before stop.
• Why It Won't Work: For n = 5, range(1, 5) only generates 1, 2, 3, 4. The final number n is omitted, making the output array one element shorter than required.
• Rectification: Extend the upper bound by one using range(1, n + 1).

3. Comparison Operator Used Instead of Assignment

• Problematic Code:python
final[i] == "Fizz"
final[i] == "Buzz"
Use code with caution.
• Why It Is a Bug: == is a equality comparison operator, whereas = is the assignment operator.
• Why It Won't Work: Python evaluates final[i] == "Fizz" to False, discards the boolean result, and leaves the original number string inside final[i] unchanged.
• Rectification: Replace == with = (final[i] = "Fizz" and final[i] = "Buzz").

4. Unreachable Condition Due to if / elif Ordering

• Problematic Code:python
if int(final[i]) % 3 == 0:
    ...
elif int(final[i]) % 5 == 0:
    ...
elif int(final[i]) % 3 == 0 and int(final[i]) % 5 == 0:
    ...
Use code with caution.
• Why It Is a Bug: In an if / elif chain, Python executes only the first block whose condition evaluates to True and skips all remaining branches.
• Why It Won't Work: Any number divisible by both 3 and 5 (such as 15) is also divisible by 3. It gets caught by the first if block and becomes "Fizz", making the "FizzBuzz" branch completely dead, unreachable code.
• Rectification: Always place the most specific, restrictive condition (% 3 == 0 and % 5 == 0) at the very top of the chain.

5. Type Mismatch & Index Overwrite in else Block

• Problematic Code:python
else:
    final[i] = i
Use code with caution.
• Why It Is a Bug: Two errors happen here simultaneously:
	1. i is the zero-based index (0, 1, 2...), not the 1-indexed value ("1", "2", "3"...).
	2. i is an int, whereas the specification requires all elements in the returned list to be str.
• Why It Won't Work: Even if the other bugs were fixed, non-multiples like 1 and 2 would be overwritten with integers 0 and 1 (e.g., [0, 1, 'Fizz', 3, 'Buzz']).
• Rectification: Delete the else block entirely. Because final was already pre-populated with the exact string representations (str(i)), non-matching elements already hold the right values.

🛠️ Rectified Implementations


Option A: Fixed Two-Pass Approach (Preserving Your Original Structure)

python
class Solution(object):
    def fizzBuzz(self, n):
        final = []
        for i in range(1, n + 1):
            final.append(str(i))
        
        for i in range(len(final)):
            num = int(final[i])
            if num % 3 == 0 and num % 5 == 0:
                final[i] = "FizzBuzz"
            elif num % 3 == 0:
                final[i] = "Fizz"
            elif num % 5 == 0:
                final[i] = "Buzz"
                
        return final
Use code with caution.

Option B: Optimized Single-Pass Approach (Recommended)

Building the list in one pass eliminates redundant int() type-casting and halves the number of loop iterations.
python
class Solution(object):
    def fizzBuzz(self, n):
        final = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                final.append("FizzBuzz")
            elif i % 3 == 0:
                final.append("Fizz")
            elif i % 5 == 0:
                final.append("Buzz")
            else:
                final.append(str(i))
        return final
Use code with caution.

💡 Key Takeaways & Lessons Learned


Concept	Lesson Learned
Loop Boundaries	Always use range(len(arr)) for index traversal and range(1, n + 1) when an inclusive upper bound n is required.
Operator Precision	Double-check = (assignment) vs. == (comparison), especially inside conditional blocks where Python will not throw a SyntaxError for a stray comparison.
Branch Specificity	Order if / elif statements from most specific to least specific so broader rules do not shadow compound conditions.
Index vs. Value	Keep track of what a loop variable represents—in range(len(arr)), i is a 0-based position, not the 1-based data stored inside arr[i].
Single-Pass Design	Whenever possible, transform data before appending it to a list rather than appending raw data and mutating it in a second loop.

If you'd like to explore string concatenation (which scales better when adding extra rules like "Jazz" for multiples of 7) or time and space complexity analysis for this problem, let me know!

