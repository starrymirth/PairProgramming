import random

def main():
    #keep track of the final scores
    totalcomputerwins = 0
    totalplayerwins = 0
    
    while (True):
        playermove = raw_input("Make your move: ")
        if playermove not in ['r','p','s','R','P','S']:
            #they want out of the tournament: 
            break;
        #now we're sure we have a legit move
        #print "this is a legal move"
        
        #get rid of case sensitivity: 
        playermove = playermove.upper() #make it uppercase.
        computermove = random.choice(['R','P','S']) #makes a random choice.
        print "Computer moved: {}".format(computermove)
        #implement the rules: 
        #if they are the same, it's a draw:
        if playermove == computermove:
            print "Draw"
            continue #we're done with this round, go to the next one. 
        #cases where the player wins: 
        elif (playermove == 'S' and computermove == 'P') or \
                (playermove == 'P' and computermove == 'R') or \
                (playermove == 'R' and computermove == 'S'):
            print "You Win"
            totalplayerwins += 1
        else: #player must have lost
            print "Computer Win"
            totalcomputerwins += 1
    
   


    #print "tournament over"
    #Print out the final scores. 
    print "PLAYER: {}, COMPUTER: {}".format(totalplayerwins, totalcomputerwins)
    if totalcomputerwins == totalplayerwins:
        print "TOURNAMENT RESULTS: DRAW!"
    elif totalcomputerwins > totalplayerwins:
        print "TOURNAMENT RESULTS: COMPUTER WINS!"
    else:
        print "TOURNAMENT RESULTS: YOU WIN!"
        
        
    
    
if __name__ == "__main__":
    main()
    