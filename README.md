# Console based Mancala
this is an implementation of Mancala game in python we used  MiniMax algorithm with alpha-beta prunning

##  Youtube video link showing the game in action

https://youtu.be/DPY4gRGmd2M

## Set-up

The game has the following set up:

* Mancala is a board game where board is made up of two rows of six pockets each
* Four pieces are placed in each of the 12 pockets
* Each player has a “store” (also called a “Mancala”) to his/her right side of the Mancala board


The game has the following rules:

* User input which mode plays with Easy mode , Medium mode or Difficult mode
* User input whether to play at normal mode or stealing mode 
* The game begins with one player picking up all of the pieces in any one of the pockets on his/her side
* Moving counter-clockwise, the player deposits one of the stones in each pocket until the stones run out
* If you run into your own Mancala (store), deposit one piece in it. If you run into your opponent's Mancala, skip it and continue moving to the next pocket
* If the last piece you drop is in your own Mancala, you take another turn
* If you are playing at stealing mode and the last piece you drop is in an empty pocket on your side, you capture that piece and any pieces in the pocket directly opposite

* The game ends when all six pockets on one side of the Mancala board are empty
* The player who still has pieces on his/her side of the board when the game ends captures all of those pieces
* Count all the pieces in each Mancala. The winner is the player with the most pieces


## To run the game
* In the command line type python game.py 
* Or run from exe file


