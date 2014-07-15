# Levi Mollison
# testing how list intersection works

list1 = [1,3,4,5,6,7,8,8]

list2 = [4,4,5,6,7,8,9,0]

# Does the intersection work without turning lists into bit representation?
# - No. The & ^ and other BIT operations require bit represented lists. turn them into this

# Interesting binary lists with & filters out copies and only puts in values that are found in both lists
intersection = list( set(list1) & set(list2))

print intersection

# intersecting lists with ^ only puts values that are uniquie to ONE list in the intersecting list
exclusive = list( set(list1) ^ set(list2) )

print exclusive

# How about intersecting 2 binary lists, but only wanting the values found in list 1 and not list 2?

filtering = list ( set(list1) & set(list2) ^ set(list1) )
print filtering