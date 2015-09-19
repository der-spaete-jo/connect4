

from __future__ import print_function   # used in Class view
import random                           # used in Class Player



class Board:
    """ THE MODEL PART I
        returns a board where you can throw coins in
        attributes: Columns, the board and a counter for the rounds
        methods: 
    """
    
    def __init__(self):       
                
        self.__Column1 = []                               
        self.__Column2 = []                               
        self.__Column3 = []
        self.__Column4 = []
        self.__Column5 = []
        self.__Column6 = []
        self.__Column7 = []
                    
        self.__gamingBoard = [self.__Column1, self.__Column2, self.__Column3, self.__Column4, self.__Column5, self.__Column6, self.__Column7]
                
        self.__rndCounter = 0
        
        
    def setBoard(self, iCol, sValue): 
        """ inserts a coin (sValue) into a given Column (iCol)"""        
        found = False
        i = 5
                        
        while found != True:
            
            if self.__gamingBoard[iCol][i] == " ":
                self.__gamingBoard[iCol][i] = sValue
                found = True                
            else:
                i = i-1
                
    def getBoard(self):        
        return self.__gamingBoard
    
    def fillBoard(self, sValue):
        """ fills the hole board with coins of the type (sValue)"""        
        for i in range(7): 
            for j in range(6):
                self.__gamingBoard[i].insert(j, sValue) 
    
    def setRndCounter(self, iRnd):
        self.__rndCounter = iRnd
        
    def getRndCounter(self):
        return self.__rndCounter



class Player:
    """ THE MODEL PART II
        returns either a human player or a player controlled by the computer
        attributes: playerID, name, mode, coin
        methods:
    """
    
    def __init__(self, iID, sName, iMode):
        
        
        self.__playerID = iID              #string
        self.__name = sName                                     
        self.__mode = iMode                #integer: 0 => humanPlayer, 1 => aiPlayer
        self.__coin = ""                   # can take values 0 , X 
    
     
                                         
    def setID(self, iID):
        self.__playerID = iID
    
    def getID(self):
        return self.__playerID
    
    def setName(self, sName):
        self.__name = sName
    
    def getName(self):
        return self.__name
    
    def setMode(self, iMode):
        self.__mode = iMode
    
    def getMode(self):
        return self.__mode
    
    def setCoin(self, sValue):        
        self.__coin = sValue        
    
    def getCoin(self):
        return self.__coin
    
    
    
    def playDraw(self, oGUI):
        """ make the GUI (oGUI) to ask the player to select a Column to throw his coin in"""        
        if self.__mode == 0:
            col = oGUI.getDraw(self.__name)
            return col
        
        else: #self.__mode == 1:
            col = random.randrange(0,7)
            #call some methods
            return col
        
        

class RuleSet:
    """ THE MODEL PART III
        returns and object knowing all rules of connect4
        attributes: boardToCheck, teamcolorToCheck
        methods: 
    """
    
    def __init__(self):
        
        self.__boardToCheck = None
        self.__teamcolorToCheck = ""
    
    
    
    def checkDraw(self, oBoard, iCol):
        """ checks whether a column (iCol) can be selected as player's draw given the board (oBoard)"""
        self.__boardToCheck = oBoard.getBoard()
        valid = False
                
        if self.isOnBoard(iCol) and self.isFree(iCol):
            valid = True
        
        return valid
    
    def isOnBoard(self, iCol):
        return iCol >= 0 and iCol <= 6              # this is program view! from players perspective this should be 1 <= iCol <= 7
    
    def isFree(self, iCol):
        """ checks whether a column of the boardToCheck has free sectors"""
        board = self.__boardToCheck
        free = False
        
        for i in range(6):
            
            if board[iCol][i] == " ":
                
                free = True
                
        return free
  
    
    
    
    def checkGameOver(self, oBoard):        
        return oBoard.getRndCounter() >= 43
  
  
  
  
  
    def checkPlayerWon(self, oBoard, oPlayer):
        
        self.__boardToCheck = oBoard.getBoard()
        self.__teamcolorToCheck = oPlayer.getCoin()
        
        if self.testRows() or self.testColumns() or self.testDiags():
            return True

    
    def isWin(self, lSectors):  
        """ checks whether a list (LSectors) contains 4 coins of the same color (teamcolorToCheck)"""        
        win = False
        counter = 0
          
        for i in range(4):
            if lSectors[i] == self.__teamcolorToCheck:
                counter = counter + 1
        
        if counter == 4:
            win = True
        
        return win
     
           
    def testColumns (self):
        
        board = self.__boardToCheck
        
        for i in range(7):
            for j in range(3):
                a = []
                for k in range(j,j+4):
                    a.append(board[i][k])
                if self.isWin(a):
                    return True      
    
    def testRows(self):
    
        board = self.__boardToCheck
        
        for i in range(6):
            for j in range(4):
                a = []
                for k in range(j,j+4):
                    a.append(board[k][i])                  #5-i to firstly test bottom rows (-> better performance)
                if self.isWin(a):
                    return True
    
    def testDiags(self):  
        
        board = self.__boardToCheck      
        
        for i in range(3):
            for j in range(3-i):
                a=[]
                b=[]
                for k in range(4):
                    a.append(board[j+k][j+k+i])
                    b.append(board[6-j-k][j+k+i])
                if self.isWin(a) or self.isWin(b):
                    return True
                    
        for i in range(1,4):
            for j in range(4-i):
                a=[]
                b=[]
                for k in range(4):
                    a.append(board[j+k+i][j+k])
                    b.append(board[6-j-k-i][j+k])
                if self.isWin(a) or self.isWin(b):
                    return True
        
        
 
 
 
        
class GUI:
    """ THE VIEW
        returns a graphical user interface for playing connect4
        attrbutes: -
        methods: 
    """
    
    def __init__(self):
        pass
        

    def drawBoard(self, oBoard):                  
        """ prints out the board that it was passed. Returns None."""
        print(str("Runde: " + str(oBoard.getRndCounter())))
        
        HLINE = '  +---+---+---+---+---+---+---+'
    
        print('    1   2   3   4   5   6   7   8')
        print(HLINE)
    
        for y in range(6):
    
            print(y+1, end=' ')
    
            for x in range(7):
    
                print('| %s' % (oBoard.getBoard()[x][y]), end=' ')
    
            print('|')
            print(HLINE)
    
        
    def getName(self, iID):
        
        name = input('Spieler ' + str(iID) + ", wie heisst du? ")
        
        return name 
    
    def getMode(self, sName):
        
        mode = input("Bist du menschlich, " + sName + "? ")
        
        return mode
    
    
    def getDraw(self, iID):
        
        col = input("Welche Spalte darf's denn sein ? ")
                
        return col-1           
        
        




class Connect4Game:
    """ THE CONTROLLER
        returns an object that controlls the game, i.e. calls the methods of the classes above to make the game running
        attributes: board, player1, player2, ruleSet, gui, draw
        methods:
    """
        
    
    def __init__(self, oGUI, oBoard, oRuleSet, oPlayer1, oPlayer2):
        self.__gui = oGUI
        self.__board = oBoard
        self.__ruleSet = oRuleSet
        self.__player1 = oPlayer1
        self.__player2 = oPlayer2
        self.__draw = -1
    
    
    
           
    def initializeGame(self): 
        """ before starting the game loop (and let the players play connect4)
            this methods asks for the names of the players and their mode [0/1], 
            i.e. whether they are human or ai"""
        
        self.__board.setRndCounter(1)                 # Init Board       
        self.__board.fillBoard(" ") 
        
        
        Name1 = self.__gui.getName(self.__player1.getID())                        # Init Player1
        Modus1 = self.__gui.getMode(Name1)        
        
        self.__player1.setName(Name1)
        self.__player1.setMode(Modus1)
       
        self.__player1.setCoin("O")    
            
        
        Name2 = self.__gui.getName(self.__player2.getID())                        # Init Player2
        Modus2 = self.__gui.getMode(Name2)        
        
        self.__player2.setName(Name2)
        self.__player2.setMode(Modus2)
        
        self.__player2.setCoin("X")
           
                
        print("Spiel ist bereit!")


    def startGame(self):
        """ the game loop"""

        while True:               
                           
            while True:                                             # first players round
                
                self.__draw = self.__player1.playDraw(self.__gui)
                
                if self.__ruleSet.checkDraw(self.__board, self.__draw) == True:
                    break
                
            self.__board.setBoard(self.__draw, self.__player1.getCoin())
            
            print("\n"*3)
            print(self.__player1.getName() + " hat gesetzt: ")            
            self.__gui.drawBoard(self.__board)
            
            if self.__ruleSet.checkPlayerWon(self.__board, self.__player1) == True:
                print(self.__player1.getName() + " hat gewonnen!")
                break
            if self.__ruleSet.checkGameOver(self.__board) == True:
                break
            
            self.__board.setRndCounter(self.__board.getRndCounter() + 1)
            
            
            while True:                                                 # second players round
                
                self.__draw = self.__player2.playDraw(self.__gui)
                
                if self.__ruleSet.checkDraw(self.__board, self.__draw) == True:
                    break
                
            self.__board.setBoard(self.__draw, self.__player2.getCoin())
            
            print("\n"*3)
            print(self.__player2.getName() + " hat gesetzt: ")            
            self.__gui.drawBoard(self.__board)
            
            if self.__ruleSet.checkPlayerWon(self.__board, self.__player2) == True:
                print(self.__player2.getName() + " hat gewonnen!")
                break
            if self.__ruleSet.checkGameOver(self.__board) == True:
                break
            
            self.__board.setRndCounter(self.__board.getRndCounter() + 1)
            
    
        print("Game Over!")




""" instantiate the objects, call initializeGame() and startGame()"""

gui = GUI()
board = Board()
ruleSet = RuleSet()
player1 = Player(1, "", -1)
player2 = Player(2, "", -1)

game = Connect4Game(gui, board, ruleSet, player1, player2)

game.initializeGame()

game.startGame()

