name = "kartavya"
print("Hello, " , name ,"!")
print("hello, " + name + "!") #we can also use + operator to concatenate strings as well as , operator

nameshort = name[0:4]
print("The first four letters of name are:", nameshort) # we can use slicing to get a part of the string
# we exclude the character at the ending index while slicing
print("The length of name is:", len(name)) # we can use len() function to get the length of the string
# in programming, indexing starts from 0 or from last with -ve index
print("The last letter of name is:", name[-1]) # we can use -1 index to get the last character of the string