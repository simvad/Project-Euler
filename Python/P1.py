# Naive solution (always be list comprehension maxxing)
def sum_of_multiples(max, ints):
    return sum([n for n in range(1, max) if any([n % i == 0 for i in ints])])

#Might an implementation w. np arrays be faster? Can i perhaps just avoid the nesting or is that inconcsequential?