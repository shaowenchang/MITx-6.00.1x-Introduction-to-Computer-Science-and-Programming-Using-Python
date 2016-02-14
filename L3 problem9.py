# Paste your code into this box
x = raw_input("Please think of a number between 0 and 100!")
low = 0
high = 99
higher = 'h'
lower = 'l'
correct = 'c'
reply1 =''
ans = (low + high)/2
while ans != x:
    ans = (low + high)/2
    print "Is your secret number",
    print int(ans),
    print "?"
    reply1 = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if  reply1 == higher:
            high = ans
    elif reply1 == lower:
            low = ans
    elif reply1 ==correct:
        print"Game over. Your secret number was:",
        print int(ans)
        break
