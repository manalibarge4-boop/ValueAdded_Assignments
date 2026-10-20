def longestCommonPrefix(str: list[str]) -> str:
    if len(str) == 0: #Does the list contain zero words
        return ""
    prefix = str[0] #This line tries to access the first item in the list. i.e flower
    for word in str[1:]: #Take everything from index 1 to the end of the list.
                         #we include the first word?
                         #Because we already used the first word to initialise our prefix: prefix = str[0]
        while not word.startswith(prefix): #Python provides a string method called startswith().
                                           #It checks whether a string begins with the specified characters.
                                           #Keep repeating while the current word does NOT start with the prefix.
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix 

#input ["flower", "flow", "flight"]
"""
example 
"flower".startswith("flow")
o/p: true
while not word.startswith(prefix):
It means:
"Keep repeating while the current word does NOT start with the prefix."
word = "flow"
prefix = "flower"
First, Python checks:"flow".startswith("flower")
False
Then not reverses it:
so it become true

"""
