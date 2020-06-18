'''
2020-06-17 
[from www.dailycodingproblem.com]

Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

    dir
        subdir1
        subdir2
            file.ext

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t
subsubdir2\n\t\t\tfile2.ext" represents:

    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

We are interested in finding the longest (number of characters) absolute path 
to a file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its 
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the 
length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.
'''

import re

def longest_filepath(string):
    if '.' not in string:
        return 0

    dirs_and_files = list(reversed(re.findall(r'[^\n\t]+', string)))
    boundaries = list(reversed(re.findall(r'\n\t+', string)))
    root = dirs_and_files.pop()
    result = ''

    for i, (df, b) in enumerate(zip(dirs_and_files, boundaries)):
        filepath = []
        j = i
        if '.' in df:
            filepath.append(df)
            level = len(re.findall(r'\t', b))
            while j < len(boundaries) - 1:
                j += 1
                if '.' in dirs_and_files[j]:
                    continue
                if sum(c == '\t' for c in boundaries[j]) == level - 1:
                    level -= 1
                    filepath.append(dirs_and_files[j])
        
            if len(filepath) > 0:
                filepath = '/'.join(list(reversed(filepath)))
                result = filepath if len(filepath) > len(result) else result

    return '{}/{}'.format(root, result)
    

'''
# Quick tests

string1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
string2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

longest_filepath(string1) == "dir/subdir2/file.ext"
longest_filepath(string2) == "dir/subdir2/subsubdir2/file2.ext"
'''
