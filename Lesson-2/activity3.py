import keyword

# print all the Python keywords
print("Python keywords are...\n")
print(keyword.kwlist)

# print keyword from index 1 to 10
print("\nPython keywords from index 1 to 10 are:\n")
print(keyword.kwlist[1:11])

# print number of keywords
print("\nTotal number of keywords: ", len(keyword.kwlist))