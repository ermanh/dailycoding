'''
2020-07-05
[from dailycodingproblem.com]

Given an array of strictly the characters 'R', 'G', and 'B', segregate the 
values of the array so that all the Rs come first, the Gs come second, and the 
Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should 
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

class RGB:

    def __init__(self, array):
        if any([char not in 'RGB' for char in array]):
            raise ValueError("array cannot contain a char other than " +
                             "'R', 'G', or 'B'")
        self.array = array
        self.indices = {'R': None, 'G': None, 'B': None}
    
    def sort(self):
        for i, elem in enumerate(self.array):
            char = str(elem)

            # First, set the last-place index of current char where it will be
            # placed
            if self.indices[char] is not None:
                self.indices[char] += 1
            else:
                if char == 'R':
                    self.indices['R'] = 0
                elif char == 'G':
                    if self.indices['R'] is not None:
                        self.indices['G'] = self.indices['R'] + 1
                    else:
                        self.indices['G'] = 0
                else:
                    self.indices['B'] = i
            
            # Increase indices of chars lower in order (R < G < B)
            if char in 'RG':
                if self.indices['B'] is not None:
                    self.indices['B'] += 1
            if char == 'R':
                if self.indices['G'] is not None:
                    self.indices['G'] += 1
            
            # Place current char in correct index after shifting the chars 
            # after that index up one place until current index 
            for j in range(i, self.indices[char], -1):
                self.array[j] = self.array[j - 1]
            self.array[self.indices[char]] = char
            
        return self.array


'''
# TESTS 

# All three elements
RGB(['R', 'G', 'B']).sort() == ['R', 'G', 'B']
RGB(['R', 'B', 'G']).sort() == ['R', 'G', 'B']
RGB(['G', 'R', 'B']).sort() == ['R', 'G', 'B']
RGB(['G', 'B', 'R']).sort() == ['R', 'G', 'B']
RGB(['B', 'G', 'R']).sort() == ['R', 'G', 'B']
RGB(['B', 'R', 'G']).sort() == ['R', 'G', 'B']
RGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']).sort() == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
RGB(['B', 'G', 'R', 'G', 'B', 'R', 'R']).sort() == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
RGB(['G', 'G', 'R', 'R', 'B', 'R', 'B']).sort() == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
RGB(['B', 'B', 'G', 'G', 'R', 'R', 'R']).sort() == ['R', 'R', 'R', 'G', 'G', 'B', 'B']

# Only two elements
RGB(['B', 'B', 'G']).sort() == ['G', 'B', 'B']
RGB(['B', 'B', 'R']).sort() == ['R', 'B', 'B']
RGB(['G', 'B', 'G']).sort() == ['G', 'G', 'B']
RGB(['G', 'G', 'R']).sort() == ['R', 'G', 'G']
RGB(['R', 'B', 'R']).sort() == ['R', 'R', 'B']
RGB(['G', 'R', 'R']).sort() == ['R', 'R', 'G']

# Only one element
RGB(['G', 'G', 'G']).sort() == ['G', 'G', 'G']

# Empty array
RGB([]).sort() == []

# Raises ValueError
RGB(['D']).sort()
'''
