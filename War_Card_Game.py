import random
##### FUNCTIONS #####
def fn_doc():
    types = ['h','d','s','c']
    facecards = ['A','J','K','Q']
    doc = []
    for type in types:
        for card in facecards:
            doc.append(card+type)
        for num in range(2,11):
            doc.append(str(num)+type)
    return doc
def shuffle(x):
    deck = fn_doc() + fn_doc()
    for each in range(x):
        random.shuffle(deck)
    return deck
def fn_getnumeric(x):
    if (x=='A'):
        return 14
    elif (x=='J'):
        return 11
    elif (x=='Q'):
        return 12
    else:
        return 13
##### Get and Shuffle Deck #####
deck = shuffle(4)
print('Deck =',len(deck),'Cards.')
P1 = deck[::2]
P2 = deck[1::2]
print(P1)
print(P2)
##### BEGIN GAME #####
p1wins = 0
p2wins = 0
ties = 0
while (len(P1)>0 and len(P2)>0) and (p1wins+p2wins+ties<1000):
    p1card = P1[0]
    p2card = P2[0]
    p1cardnum = p1card[:-1]
    p2cardnum = p2card[:-1]

    if (p1cardnum.isnumeric() == False):
        p1cardnum = fn_getnumeric(p1cardnum)
    else:
        p1cardnum = int(p1cardnum)

    if (p2cardnum.isnumeric() == False):
        p2cardnum = fn_getnumeric(p2cardnum)
    else:
        p2cardnum = int(p2cardnum)
    print(p1cardnum, p2cardnum)

    if (int(p1cardnum)>int(p2cardnum)):
        P1.append(P2[0])
        P2.pop(0)
        print('Player 1 Won and now has',len(P1),'Cards')
        print('Player 2 Lost and now has',len(P2),'Cards')
        p1wins +=1
        random.shuffle(P1)
        random.shuffle(P2)
        print('Player 1 wins =',p1wins)
    elif (int(p1cardnum)<int(p2cardnum)):
        P2.append(P1[0])
        P1.pop(0)
        print('Player 2 Won and now has',len(P2),'Cards')
        print('Player 1 Lost and now has',len(P1),'Cards')
        p2wins +=1
        random.shuffle(P1)
        random.shuffle(P2)
        print('Player 2 wins =', p2wins)
    else:
        print('Tie! Shuffling...')
        for x in range(4):
            random.shuffle(P1)
            random.shuffle(P2)
        ties +=1
##### END GAME #####
print(' '*75,'##### GAME OVER! #####')
if len(P1)==0:
    print(' '*75,'##### Player 2 Wins! #####')
elif len(P2)==0:
    print(' '*75,'##### Player 1 Wins! #####')
else:
    print(' '*75,'##### 1000 Turns Played #####')
    if len(P1)<len(P2):
        print(' ' * 75, '##### Player 2 Wins! #####')
    elif len(P2)<len(P1):
        print(' ' * 75, '##### Player 1 Wins! #####')

print('Player 1 Wins =',p1wins,'| Player 2 Wins =',p2wins)
print('Player 1 Cards =',len(P1),'| Player 2 Cards =',len(P2))
print('Total Games =',p1wins+p2wins)
print('Total Ties =',ties)
