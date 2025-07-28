# Slice is a part (substring or subsequence) of a sequence extracted using the slicing syntax: sequence[start:stop:step]  
# Note: stop is not included.
 
"""
🔑 Rule Reminder for Slicing:
1. step > 0 : start < stop (left to right)

2. step < 0: start > stop (right to left)
"""

"""
Positive:   H  e  l  l  o     W  o  r  l  d
            0  1  2  3  4  5  6  7  8  9 10
Negative: -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""


text = 'Hello World'


# print( text[0:11:2] )    # Output: HloWrd  (every second step)
# print( text[0:11:2] )    # Output: HloWrd  (every second step)
# print( text[0::2] )      # Output: HloWrd  (every second step)
# print( text[::2] )       # Output: HloWrd  (every second step)
# print( text[0:4:0] )     # ❌ err => ValueError: slice step cannot be zero
# print( text[0:4:] )      # Output: Hell
# print( text[0:4] )       # Output: Hell
# print( text[0:] )        # Output: Hello World
# print( text[0] )         # Output: H
# print( text[] )          # ❌ err => SyntaxError: invalid syntax.



# ------------------------------ What if we pass -ve index to [] ?? 🤔💭 ------------------------------
# print(text[-11::2])     # Output: HloWrd  (every second character from start)
# print(text[-11::-2])    # Output: H  
# print(text[-11::2])     # Output: HloWrd  (same)
# print(text[-11:-7:-1])  # Output: empty
# print(text[-11:-7])     # Output: Hell    (step defaults to 1)
# print(text[-11:])       # Output: Hello World (from start to end)
# print(text[-11])        # Output: H        (first character using negative index)
# print(text[4:2:-1])       # Output: ol
# print(text[-2:-4:-1])     # Output: lr