def main():

    words = input().split(" ") # input three space seperated words

    # for first word

    word = words[0]
    for i in range(len(word)):
        if word[i] in "aeiou":
            word = word[:i] + "%" + word[i+1:]
    
    words[0] = word

    # for second word

    word = words[1] 
    for i in range(len(word)):
        if word[i] not in "aeiou":
            word = word[:i] + "#" + word[i+1:]

    word[1] = word
    
    # for third word

    words[2] = words[2].upper()

    for i in range(len(words)):
        print( words[i]) 
    
main()