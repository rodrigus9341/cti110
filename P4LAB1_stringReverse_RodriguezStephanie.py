''' Type your code here. '''
text = input()


while text != "Done" and text != "done" and text != "d":

    for char in range(len(text)-1,-1,-1):

        print(text[char], end="")
    
    print()

    text = input()