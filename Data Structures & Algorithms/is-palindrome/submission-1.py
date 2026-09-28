class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():  #checking if characters are in alphanumeric set
                newStr += c.lower() #copying the lower case characters into the newstring
        return newStr == newStr[::-1] #checking if new string is  reverse of itself