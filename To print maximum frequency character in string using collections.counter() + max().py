from collections import Counter

test_str = "mississippi"

print ("The original string is : " + test_str)

res = Counter(test_str)
res = max(res, key = res.get)

print ("The maximum of all characters in mississippi is : " + str(res))