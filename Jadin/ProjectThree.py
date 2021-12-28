def test():
    Correct = 0
    Q1 = input("What is the power house of the cell? A) mitochondria B) nucleous C) ribosome")
    if (Q1 == "A" or Q1 == "a"):
        print("Correct")
        Correct = Correct+1
    elif (Q1 == "B" or Q1 == "b"):
        print("Incorrect")
    elif (Q1 == "C" or Q1 == "c"):
        print("Incorrect")
    else:
        print("Please type, A, B, or C")
    
    Q2 = input("How many states comprise the United States? A) 13 B) 45 C) 50")
    if (Q2 == "A" or Q2 == "a"):
        print("Incorrect")
    elif (Q2 == "B" or Q2 == "b"):
        print("Incorrect")
    elif (Q2 == "C" or Q2 == "c"):
        print("Correct")
        Correct = Correct+1
    else:
        print("Please type, A, B, or C")
        
    Q3 = input("In English, a person, place or thing is called: A) verb B) adjective C) noun")
    if (Q3 == "A" or Q3 == "a"):
        print("Incorrect")
    elif (Q3 == "B" or Q3 == "b"):
        print("Incorrect")
    elif (Q3 == "C" or Q3 == "c"):
        print("Correct")
        Correct = Correct+1
    else:
        print("Please type, A, B, or C")
        
    print("You got " + str(Correct) + " answers right")
    return