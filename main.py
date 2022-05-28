from pydoc import splitdoc
filename = "story"
def read_file_content(filename):
    with open("./story.txt" , "r") as f:
        file_content= f.read()
        return file_content
print(read_file_content(filename))         
       


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words_of_text = text. split()
    count = dict()
    

    for word in words_of_text:
        if word in words_of_text:
             count[word]  += 1
        else:
                count[word] = 1

    return count
b = count_words()
print(b)


              

