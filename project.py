
while True:
    print("Welcome in reversal program, enter X for exit.")
    string = input("What sentence would you like to reverse?: ")
    if string == "X":
        break
    else:
        revstring = string[::-1]
        print("Reversed version1 =",revstring,"\n")

        words = string.split(" ")
        reverse_sentence = " ".join(reversed(words))
        print("Reversed version2 =",reverse_sentence,"\n")

        revsentence = reverse_sentence[::-1]
        print("Reversed version3 =",revsentence,"\n")
        





        

        
        

        

        

        

