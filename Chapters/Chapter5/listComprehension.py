print("################################################################################") 
print("""
LIST COMPREHENSION\n""")
print("################################################################################") 

print("""
List comprehension provides a concise way to apply an ooperation to th evalues 
in a sequence. It creates a new list in which each element is the reult of 
applying a given operation to a value from a sequence (e.g., the elements in
another list). For example:""")

print("""
L = [x**2 for x in range(1,7)]
print(L)""")

L = [x**2 for x in range(1,7)]
print(L)

print("""
The for clause in a list comprehension can be followed by one or more if and for
statements that are applied to the values produced by the for clause. These
additional cluases modify the sequence of values generated by the first for
clause and produce a new sequence of values, to which the operation associated
with the comprehension is applied. For example, the code:""")

print("""
mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int])""")

mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int])

print("""
Some python programmers are able to use list comprehensions in marvelous and
subtle ways, but if you are sharing this code with others this may not always be
a good idea because 'subtle' may not usually be a desirable property.""")
