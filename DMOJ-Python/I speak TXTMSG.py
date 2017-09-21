T = {"CU":"see you", ":-)":"I'm happy", ":-(":"I'm unhappy", ";-)":"wink", ":-P":"stick out my tongue", "(~.~)":"sleepy", "TA":"totally awesome", "CCC":"Canadian Computing Competition", "CUZ":"because", "TY":"thank-you", "YW":"you're welcome", "TTYL":"talk to you later"}
b = True

while b == True:
    word = raw_input()
    if word == "TTYL":
        print T[word]
        b = False
    elif word in T:
        print T[word]
    else:
        print word
