# Write your solution here
def first_word(string):
    firstWord = ""
    i=0
    while string[i]!=" " :
        firstWord+=string[i]
        i+=1
        if i>=len(string):
            break
    return firstWord

def second_word(string):
    return first_word(string[len(first_word(string))+1:])

def last_word(string):
    i=len(string)-1
    while string[i]!=" ":
        lastSpaceIndex = i
        i-=1
    return string[lastSpaceIndex:]
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
