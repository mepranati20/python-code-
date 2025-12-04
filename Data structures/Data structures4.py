# generate a list numbers create a dictionary called counts that contains the number of times each number appears in the list.
 
numbers = [10, 45, 45, 38, 38, 38, 10, 10]
counts = {}
for n in numbers:
    counts[n] = counts.get(n, 0) + 1
print(counts)