# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
#Name: Osarenkhoe Chima-Nwogwugwu
#Student Id: I4G033993TR5
def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt", "r") as readfile:
        read_file = readfile.read()
    return read_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    textsplit = text.split()
    count_dict = {}
    for i in textsplit:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

print(count_words())