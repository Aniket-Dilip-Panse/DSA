# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
def reverseWords(S):
        # code here 
        rev = "."
        L = S.split(".")
        return (rev.join(L[::-1]))
reverseWords("i.like.this.program.very.much")
