Problem E
---------

Today we're going to write an interactive game! Rock Paper Scissors, is a nice game to play with a computer as the rules are fairly straightforward. 

The task is to write a program that will run a tournament of Rock-Paper-Scissors. 

The program should take input from the console, corresponding to your move, and then print out its *random* move.
It should then work out who won or if it was a draw, and print out a message saying who won.
We want to be able to play more than one round at a time, so you will need a loop so that you can run several rounds after each other. 

Note: This is a slightly bigger project than what we normally do, so we will split it over two weeks. I have separated out which part I would focus on for which week, but you are welcome to change it around! If you finish with Part 1 early, feel free to move on to Part 2!


### Part 1: Week 1

You will need a program that runs in a loop, that will take in a value for your move.
It should check if it is one of the allowed values ('r', 'p', 's', 'R', 'P', 'S') and print "this is a legal move". 
If it is not a legal move, it should end the tournament (break out of the loop) and print "tournament over" before quitting. 

### Part 2: Week 2

You will now need to get the computer to generate a random move after you type in your value. There are random functions in Python and MATLAB which will make this easier. 

Lastly, you will need to get the computer to compare your move to its move, and work out if it's a "COMPUTER WINS!", or "YOU WIN!" or "DRAW".
This will replace the line that said "this is a legal move". 

Play your game!

### Part 3: On your own time

You could keep a running count of how many times you or the computer won and at the end of the game, print out the tournament winner!

If you're a fan of The Big Bang Theory, you might want to extend your program to play Rock-Paper-Scissors-Lizard-Spock! (RPSLK)!

