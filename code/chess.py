#!/usr/bin/python
import os,sys

#######################################################################
## Functions for initializing the board and displaying it            ##
#######################################################################
 
def newBoard():
    """ make new board """
    board = dict()
    for y in range(8):
        for x in range(8):
            board[(1,x)] = 'WP'
            board[(6,x)] = 'bp'

    board[(0,0)] = board[(0,7)] = 'R'
    board[(0,1)] = board[(0,6)] = 'KN'
    board[(0,2)] = board[(0,5)] = 'B'
    board[(0,3)] = 'Q'
    board[(0,4)] = 'K'

    board[(7,0)] = board[(7,7)] = 'r'
    board[(7,1)] = board[(7,6)] = 'kn'
    board[(7,2)] = board[(7,5)] = 'b'
    board[(7,3)] = 'q'
    board[(7,4)] = 'k'

    return board

#######################################################################
## Print the chess board                                             ##
#######################################################################
    
def printBoard(board):
    """ print the board """
    topbottom=['*','a','b','c','d','e','f','g','h','*']
    sides=['1','2','3','4','5','6','7','8']
    tbspacer=' '*6
    rowspacer=' '*5
    cellspacer=' '*4
    empty=' '*3
    
    print
    for field in topbottom:
        print("%4s") % field,
    print
    print(tbspacer+("_"*4+' ')*8)
    
    for row in range(8):
        print(rowspacer+(('|'+cellspacer)*9))
        print("%4s") % sides[row],('|'),
        for col in range(8):
            if (row, col) not in board:
                print(empty+'|'),
            else:
                print("%2s") % board[(row, col)],('|'),
        print("%2s") % sides[row],
        print
        print(rowspacer+'|'+(("_"*4+'|')*8))
    print
    
    for field in topbottom:
        print("%4s") % field,

    print("\n")
    

#######################################################################
## Refresh the screen                                                ##
#######################################################################

def refreshScreen(board, playera, playerb):
    """ Refreshes the screen... """
    os.system('clear')
    printHeader(playera, playerb)
    printBoard(board)

    
#######################################################################
## Print a nice header to show who's playing whom                    ##
#######################################################################

def printHeader(playera, playerb):
    """ Just for the looks of it """
    tt="   Now playing: "+playera+" vs "+playerb
    uline='-'*len(tt)
    print tt,"\n"
    #print uline

    
#######################################################################
## Piece rules and functions that refuse or allow a move             ##  
#######################################################################

    
def getPosition(move):
    """ Converting a2a3 to (1,0)-(2,0) etc. """    
    startcol=int(ord(move[0].lower())-97)
    startrow=int(move[1])-1
    targetcol=int(ord(move[2].lower())-97)
    targetrow=int(move[3])-1
    start=(startrow,startcol)
    target=(targetrow,targetcol)
    return start, target

#######################################################################
## Verify the move is a valid move and falls into the allowed range  ##
#######################################################################

def formOk(move):
    """ Checks that form has valid form, ie 'a1b2' """
    
    if not len(move) == 4: return False

    if move[0] not in 'abcdefghABCDEFGH': return False
    elif move[2] not in 'abcdefghABCDEFGH': return False
    elif move[1] not in '12345678': return False
    elif move[3] not in '12345678': return False
    
    return True

#######################################################################
## Identify if two players are counterparts or the same player       ##
#######################################################################

def isEnemy(str1,str2):
    """ Checks whether str1 and str2 has different case,
    which in this game separates friend from foe.
    Presumes that strings has same case for all chars. """
    
    if str1.isupper() and str2.isupper():
        return False
    elif str1.islower() and str2.islower():
        return False
    else:
        return True


def listPieces(board, player, friendorfoe):
    """ Returns list of player's or opponent's pieces """
    
    # make list of enemies' pieces
    enemylist = []
    for row in range(8):
        for col in range(8):
            if (row, col) in board:
                piece = board[(row, col)]
                if isEnemy(piece, player):
                    enemylist.append((row, col))

    # make list of player's pieces
    piecelist = []
    for row in range(8):
        for col in range(8):
            if (row, col) in board:
                piece = board[(row, col)]
                if not isEnemy(piece, player):
                    piecelist.append((row, col))

    if friendorfoe == 'foe':
        return enemylist
    else:
        return piecelist


def listValidTargets(board, player, teststart):
    """ Returns list of valid moves """

    # Get list of player's pieces
    piecelist = listPieces(board, player, 'friends')

    # List all valid moves for square 'teststart'
    validtargets = []
    for row in range(8):
        for col in range(8):
            if (row, col) not in piecelist:
                testtarget = (row, col)
                startpiece = board[teststart]
                if evalPieces(board, teststart, testtarget, startpiece, player):
                    if not makesUsCheck(teststart, testtarget, board, player):
                        validtargets.append(testtarget)
                        
    return validtargets

#######################################################################
## Identify if the path to the target is free or not                 ##
#######################################################################

def isClearPath(board, start, target):
    """ Checks if move has line-of-sight """
    startcol = start[1]
    startrow = start[0]
    targetcol = target[1]
    targetrow = target[0]

    if abs(startrow - targetrow) <= 1 and abs(startcol - targetcol) <= 1:
        return True
        
    else:
        if targetrow > startrow and targetcol == startcol:
        # Straight down
            tmpstart = (startrow+1,startcol)
        elif targetrow < startrow and targetcol == startcol:
            # Straight up
            tmpstart = (startrow-1,startcol)
        elif targetrow == startrow and targetcol > startcol:
            # Straight right
            tmpstart = (startrow,startcol+1)
        elif targetrow == startrow and targetcol < startcol:
            # Straight left
            tmpstart = (startrow,startcol-1)
        elif targetrow > startrow and targetcol > startcol:
            # Diagonal down right
            tmpstart = (startrow+1,startcol+1)
        elif targetrow > startrow and targetcol < startcol:
            # Diagonal down left
            tmpstart = (startrow+1,startcol-1)
        elif targetrow < startrow and targetcol > startcol:
            # Diagonal up right
            tmpstart = (startrow-1,startcol+1)
        elif targetrow < startrow and targetcol < startcol:
            # Diagonal up left
            tmpstart = (startrow-1,startcol-1)

        # If no pieces in the way, test next square
        if board.get(tmpstart):
            return False
        else:
            return isClearPath(board, tmpstart, target)


def IsCheckmate(board, player):
    """ If True, player is checkmate """

    # Get list of player's pieces
    piecelist = listPieces(board, player, 'friends')
    
    # Check for possible move for player's pieces
    validMoves = []
    for piece in piecelist:
        validtargets = listValidTargets(board, player, piece)
        validMoves.extend(validtargets)
    
    # If no moves possible we are checkmate
    if len(validMoves) == 0:
        return True
    else:
        return False


def makesUsCheck(start, target, board, player):
    """ Check if move will put player's king in check """

    startpiece = board.get(start)
    targetpiece = board.get(target)
    
    # Make temporary move to test for check
    del board[start]
    board[target] = startpiece
    
    retval = isKinginCheck(board, player)

    # Undo temporary move
    board[start] = startpiece
    if targetpiece:
        board[target] = targetpiece
    else:
        del board[target]

    return retval


def isKinginCheck(board, player):
    """ Check if player's King is in check """

    # Separate friend from foe
    if player.isupper():
        king = 'K'
    else:
        king = 'k'

    # Locate player's king
    for row in range(8):
        for col in range(8):
            if (row, col) in board:
                if board[(row, col)] == king:
                    playersking = (row, col)

    # make list of enemies
    enemylist = listPieces(board, player, 'foe')
    
    # Check for possible enemy attack on king's position            
    for enemy in enemylist:
        startpiece = board.get(enemy)
        if evalPieces(board, enemy, playersking, startpiece, player):
            return True

#######################################################################
## Verify the move is a valid for the existing tactic situation      ##
#######################################################################

def ismoveValid(start, target, board, player):
    """ Check for validity of the move """
   
    startpiece = board.get(start)
    targetpiece = board.get(target)
    
    # Get list of player's and enemy's pieces
    piecelist = listPieces(board, player, 'friends')
    enemylist = listPieces(board, player, 'foe')

    # Break if moving enemy, attacking self or moving empty square
    if start not in piecelist or target in piecelist:
        return False

    # Break if move is illegal according to rules
    if not evalPieces(board, start, target, startpiece, player):
        return False

    # All ok, ready to do move (no move executed yet)
    return True


def evalPieces(board, start, target, startpiece, player):
    """ Evaluates legality based on piece """

    startpiece = startpiece.upper()

    # Only the Knight may jump over pieces
    if startpiece not in 'KN':
        if not isClearPath(board, start, target):
            return False

    if ( startpiece == 'R' and checkRook(board, start, target) ):
        return True
    elif ( startpiece == 'KN' and checkKnight(board, start, target) ):
        return True
    elif ( 'P' in startpiece and checkPawn(board,start,target,player) ):
        return True
    elif ( startpiece == 'B' and checkBishop(board, start, target) ):
        return True
    elif ( startpiece == 'Q' and checkQueen(board, start, target) ):
        return True
    elif ( startpiece == 'K' and checkKing(board, start, target) ):
        return True

    return False


def checkRook(board, start, target):
    """ Returns true if move of Rook is legal """
    
    # Check for straight lines of movement(start/target on same axis)
    if start[0] == target[0] or start[1] == target[1]:
        return True

        
def checkKnight(board, start, target):
    """ Returns true if move of Knight is legal """

    # 'Knight' may move 2+1 in any direction and jump across pieces
    if abs(target[0]-start[0]) == 2 and abs(target[1]-start[1]) == 1:
        return True
    elif abs(target[0]-start[0]) == 1 and abs(target[1]-start[1]) == 2:
        return True


def checkPawn(board, start, target, player):
    """ Returns true if move of Pawn is legal """

    # Disable backwards and sideways movement
    startpiece = board.get(start)
    if startpiece.isupper() and target[0] < start[0]:
        return False
    elif startpiece.islower() and target[0] > start[0]:
        return False
    if start[0] == target[0]:
        return False

    if target in board:
        # Only attack if one square diagonaly away
        if abs(target[1]-start[1]) == 1:
            if abs(target[0]-start[0]) == 1:
                return True
    else:
        # Make peasants move only one forward (except first move)
        if start[1] == target[1]:
            # Normal one square move
            if abs(target[0]-start[0]) == 1:
                return True
            # Exception to the rule, 2 square move first time
            elif ( start[0] == 1 and target[0] == 3 ) or \
                ( start[0] == 6 and target[0] == 4 ):
                return True


def checkBishop(board, start, target):
    """ Returns true if move of Bishop is legal """
    
    # Check for non-horizontal/vertical and linear movement
    if abs(target[1]-start[1]) == abs(target[0]-start[0]):
        return True


def checkQueen(board, start, target):
    """ Returns true if move of Queen is legal """
    
    # Will be true if move can be done as Rook or Bishop
    if checkRook(board, start, target) or \
       checkBishop(board, start, target):
        return True


def checkKing(board, start, target):
    """ Returns true if move of King is legal """

    # King can move one square in any direction
    if abs(target[0]-start[0]) <= 1 and abs(target[1]-start[1]) <= 1:
        return True


#######################################################################
## Starting and running the game, executing a (validated) move       ##
#######################################################################


def pawnPromotion(board, target):
    """ Promotes Pawn to Queen """
    
    # Promote WHITE Pawn
    if target[0] == 7:
        board[target] = 'Q'
        
    # Promote black Pawn
    if target[0] == 0:
        board[target] = 'q'


def gameWon(board, player, playera, playerb):
    looser = player
    winner = nextPlayer(player, playera, playerb)
    os.system('clear')
    printBoard(board)
    print("\n"+winner+" put "+looser+" in checkmate.")
    print("Congratulations "+winner+" !")
    raw_input("\n\nPress [Enter] to continue")


def doMove(start, target, board):
    """ Executes the validated move """
    startpiece = board.get(start)
    del board[start]
    board[target] = startpiece
    
    # Check if there is Pawn up for promotion
    if 'p' in startpiece or 'P' in startpiece:
        if str(target[0]) in '07':
            pawnPromotion(board, target)


def nextPlayer(player, playera, playerb):
    """ Rotates players """
    if player == playera:
        player = playerb
    else:
        player = playera
    return player


def playersTurn(board, player):
    """ Returns the string that will show at the bottom each turn """
    
    turnstring = "\n\n"+player+"'s turn,"
    warning = " *** Your King is in check *** "
    
    if isKinginCheck(board, player):
        turnstring = turnstring + warning
    
    return turnstring

#######################################################################
## Ask the player to provide a move in a a2a3 format and process it  ##
#######################################################################

def getMove(board,playera,playerb):
    """ Get a move from player """

    # WHITE starts
    player=playera

    print "\n"
    while True:
        print playersTurn(board, player)
        move=raw_input("\nMake a move : ")
        if move == 'exit':
            break

        if formOk(move):
            start, target = getPosition(move)
            if ismoveValid(start, target, board, player):
                if not makesUsCheck(start, target, board, player):
                    # Move was legal, let's do it
                    doMove(start, target, board)
                    
                    # Move has been done, shifting to next player
                    player=nextPlayer(player, playera, playerb)
                    
                    # Check if last move put current player in checkmate
                    if IsCheckmate(board, player):
                        gameWon(board, player, playera, playerb)
                        break
                        
                    else:
                        refreshScreen(board, playera, playerb)
                else:
                    refreshScreen(board, playera, playerb)
                    print("\n\nYou may not put your king in check.")
            else:
                refreshScreen(board, playera, playerb)
                print("\n\nPlease enter a valid move.")
        else:
            refreshScreen(board, playera, playerb)
            print("\n\nPlease use proper notation, ie 'd2d4'.")

#######################################################################
## Start, create two players and assign W to uppercase, b to lower   ##
#######################################################################

def startGame():
    """ Get player names and get the game going """
    os.system('clear')
    
    print """
      Welcome to Console Chess, the fantastic console chess environment.
      Please type in the name of the contestants."""

    playerA = playerB = None
    while not playerA:
        playerA=raw_input("\nPlayer A: ")
    while not playerB:
        playerB=raw_input("Player B: ")

    playerA=playerA.upper()
    playerB=playerB.lower()

    print "\nVery well,",playerA,"and",playerB+", let's play.\n"
    print "Player A: '"+playerA+"' will play as WHITE (uppercase)"
    print "Player B: '"+playerB+"' will play as black (lowercase)"
    print("\nUse moves on form 'a2b3' or type 'exit' at any time.")
    raw_input("\n\nPress [Enter] when ready")
    board=newBoard()
    refreshScreen(board,playerA,playerB)
    getMove(board,playerA,playerB)


def main():
    """ Displaying menu after game has ended. """
    
    menu="""
    Thanks for playing the Chess, would you like to go again?
    Type 'enter' to play again or 'exit' to quit.  >> """

    try:
        while True:
            startGame()
            
            choice=raw_input(menu)

            if choice == 'exit':
                print "\nAs you wish. Welcome back!"
                break

    except KeyboardInterrupt:
        sys.exit("\n\nOk. Aborting.")



main()
