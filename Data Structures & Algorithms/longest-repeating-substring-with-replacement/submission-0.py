"""
We can take a sliding window approach.
When we hit a character that doesn't match our starting character, we make a note of it,
and do this up to k times.

We do want to do this with O(n) runtime, since the input is on the order of 100,000.

ABABB
Once we hit k+1, if the next character is in the list of top counts, we can continue to grow the window. If not, then we shrink the window until it is, and no other ones are above k.

k=2
ABAB => 4 {A:2, B:2}
ABABB => 5 {A:2, B:3}
ABABC => {A:2, B:2, C:1} length = 5, max(counter) = 2
-BABC => {A:1, B:2, C:1} length = 4, max(counter) = 2
-BABCB => {A:1, B:3, C:1} length = 5, max(counter) = 3
ABABBA {B:3, A:2}
-BABBA
--ABBA
--ABBAB => 5 {B:3, A:2}
--ABBAA => 5

Since the input space is only A-Z, we could just run a naive sliding window algorithm 26 times,
one for each letter. I think we can do better, though.

For the sake of having a solution, though:
Find longest uninterrupted sequence of A's, k = 0.
Sliding window

The solution will always be at least 1 + k, and at most len(s).

AAAABBBBAAAABBB
"""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest = 0, 0
        counter = Counter()
        for right in range(0, len(s)):
            counter[s[right]] += 1
            if right - left + 1 - max(counter.values()) <= k:
                longest = max(longest, right - left + 1)
            while right - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
        return longest
        