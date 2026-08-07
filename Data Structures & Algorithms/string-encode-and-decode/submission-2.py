"""
Approach:
Include a header before each string, so that the decoder knows how many characters to decode per string.

Option 1: [str length][delimiter][actual string (str length # of characters)]
Option 2: [str length (3 chars)][actual string (str length # of characters)]

Decoding will have two modes; a length parse mode and a character parse mode.
Alternatively, since we know strings will be no more than 200, we can also just encode 3 digits to save some trouble in the decode section.

Test cases:
1) cat, dog, echo
2) '', ask, hi
3) 123, 23, 3
4) ''
5) a,''

Test case encoding:
3;cat;3;dog;4;echo
0;3;ask2;hi
3;1232;231;3
0;
1;a0;

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            slen = len(s)
            result += str(slen)
            result += ';'
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        slen = -1
        i = 0
        lenstr = ""
        # Todo: figure out loop condition
        while i < len(s):

            if slen > -1:
                result.append(s[i:i+slen])
                i += slen
                lenstr = ""
                slen = -1
                continue
            
            # length parse
            c = s[i]
            if c != ';':
                lenstr += c
            else:
                slen = int(lenstr)
            i += 1
        if slen == 0:
            result.append("")
        return result