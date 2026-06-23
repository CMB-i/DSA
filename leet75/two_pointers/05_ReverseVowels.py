# 1st version: 11ms:
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        while right>left:
            if s[left] not in "AEIOUaeiou":
                left += 1
            if s[right] not in "AEIOUaeiou":
                right -=1
            if s[left] in "AEIOUaeiou" and s[right] in "AEIOUaeiou":
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
        return "".join(s)

#2nd version: 6ms waayy better; got rid of the 3rd if condiiton

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        while right>left:
            if s[left] not in "AEIOUaeiou":
                left += 1
                continue
            if s[right] not in "AEIOUaeiou":
                right -=1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
        return "".join(s)

# alt to creating a list:
class Solution:
        def reverseVowels(self, s: str) -> str:
            vowels = set("aeiouAEIOU")
            found = [c for c in s if c in vowels]
            found.reverse()
            result = []
            vi = 0  # pointer into `found`
            for c in s:
                if c in vowels:
                    result.append(found[vi])
                    vi += 1
                else:
                    result.append(c)
            return "".join(result)

''' 1. THE STRING IMMUTABILITY BUG
-------------------------------
Strings in Python are IMMUTABLE — you cannot change a character at a given
index directly. This fails:

    s = "hello"
    s[0] = "H"
    # TypeError: 'str' object does not support item assignment

Why: under the hood, a str's character data is fixed at creation; there's no
mechanism to overwrite a slot in place. Every "modification" to a string
(concatenation, slicing, .replace(), etc.) actually creates a BRAND NEW
string object — the original is never touched.

The fix: convert to a list first (lists ARE mutable — they support item
assignment), do all swapping there, then join back into a string at the end:
  s = list(s)              # ['h','e','l','l','o'] — now mutable
    s[0] = "H"                # works fine
    s = "".join(s)            # back to a normal string when done

In version 1, EVERY iteration of the while loop evaluates all three `if`
  conditions, even when the first one already told you nothing useful can
  happen this round (e.g. s[left] still isn't a vowel). The third check
  (`s[left] in vowels and s[right] in vowels`) gets evaluated on every
  single pass, doing redundant membership tests that were already implied.

- In version 2, `continue` exits the loop body immediately the moment you
  know a swap can't happen yet. By the time the code reaches the swap line,
  it's guaranteed (by elimination — neither earlier `if` fired) that both
  s[left] and s[right] are already vowels — no need to re-check.

- Fewer redundant membership checks per iteration = fewer total operations
  across the whole string = faster runtime, especially for inputs with
  large stretches of consonants where the skip-checks fire often.

Takeaway: `continue` is a great tool any time you have a sequence of
conditions where an early condition makes a later one logically guaranteed —
skip ahead instead of re-checking.
'''
