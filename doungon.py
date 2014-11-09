import turtle
import random
import math


def rectangle(t):
    for i in range(4):
        t.forward(32)
        t.right(90)

def getPlayerNames():
    
    player1 = input('Name of adventurer: ')

    return player1

def getBoardInfo():
    
    spaces=100
    enemy=25
    bonus=15
    return spaces, enemy, bonus

def enemy():

    thing = random.randint(1,3)
    if thing == 1:
        goblin = { 'goblin' : 5}
    elif thing == 2:
        dragon = { 'dragon' : 15}
    else:
        snake = { 'snake' : 2}

def boardSetup(boardSize, enemyNum, bonusNum):

    enemy = {}
    bonus = {}
    victory = {}

    while len(enemy) < enemyNum:
        space = random.randint(2, boardSize)
        if space in enemy:
            continue
     
        enemy[space] = random.randint(1,5)  
    
    while len(bonus) < bonusNum:
        space = random.randint(2,boardSize)
        if space in bonus or space in enemy:
            continue

        bonus[space] = random.randint(1,5)        
        
    while len(victory) < 1:
        space = random.randint(5, boardSize)
        if space in bonus or space in enemy:
            continue
        
        victory[space] = space
    
    return enemy, bonus, victory

def movement():
    move = input('Where do you want to move?')
    turn=0
    if move == 'd':
        turn=1
    if move == 'a':
        turn=-1
    if move == 's':
        turn=10
    if move == 'w':
        turn=-10

    return turn

def tex(t,wri):
    t.clear()
    t.penup()
    t.goto(0,30)
    t.pendown()
    t.write('Health: ' + wri,font=('arial',24,'bold')) 

def playGame():
    pl=turtle.Turtle()
    pl.shape("turtle")
    pl.penup()
    pl.forward(16)
    pl.right(90)
    pl.forward(16)
    pl.left(90)
    
    text=turtle.Turtle()
    
    board=turtle.Turtle()

    rectangle(board)
    player = getPlayerNames()
    
    boardSize, enemyNum, bonusNum = getBoardInfo()
    
    enemy, bonus, victory = boardSetup(boardSize, enemyNum, bonusNum)

    positions = {player:1}

    health = 25



    right = 0

    print('Hello', player,', YOu are a turtle trapped in a dungeon with some dragons.')
    print('Try to escape and survive the hazards that await you.')
    print('You move by writing a for left, s for down, d for right, w for up and then clicking enter')
    print('Good Luck!')
    while True:
        tex(text,str(health))
        move = movement()
        
        if move == 1 and right+ 1 > 9:
            print(', dude, wall...')
        elif move == -1 and right-1 < 0:
            print(', dude, wall...')
        else:      
            if positions[player] + move <= boardSize and positions[player] + move > 0:
                positions[player] += move
            
                if move == 1:
                    pl.forward(32)
                    board.forward(32)                
                    rectangle(board)
                    right+=1

                if move == -1:
                    pl.right(180)
                    pl.forward(32)
                    pl.right(180)
                    board.right(180)
                    board.forward(32)
                    board.right(180)
                    rectangle(board)
                    right-=1
                if move == 10:
                    pl.right(90)
                    pl.forward(32)
                    pl.left(90)
                    board.right(90)
                    board.forward(32)
                    board.left(90)
                    rectangle(board)
                if move == -10:
                    pl.left(90)
                    pl.forward(32)
                    pl.right(90)
                    board.left(90)
                    board.forward(32)
                    board.right(90)
                    rectangle(board)
            
                if positions[player] in victory:
                    print(player, 'survived....')
                    break
                
                if positions[player] in enemy:

                    if enemy[positions[player]] == 1:
                        print('SNAKE, you lose ' , enemy[positions[player]] , ' HP')
                        health-= enemy[positions[player]]
                    elif enemy[positions[player]] == 2:
                        print('SKELETON, you lose ' , enemy[positions[player]] , ' HP')
                        health-= enemy[positions[player]]
                    elif enemy[positions[player]] == 3:
                        print('GOBLIN, you lose ' , enemy[positions[player]] , ' HP')
                        health-= enemy[positions[player]]
                    elif enemy[positions[player]] == 4:
                        print('WOLF, you lose ' , enemy[positions[player]] , ' HP')
                        health-= enemy[positions[player]]
                    elif enemy[positions[player]] == 5:
                        print('BABY DRAGON, you lose ' , enemy[positions[player]] , ' HP')
                        health-= enemy[positions[player]]
                    del enemy[positions[player]]

                if positions[player] in bonus:
                    print('oh look, a potion (plus ' , bonus[positions[player]] , ')')
                    health+= bonus[positions[player]]
                    del bonus[positions[player]]
            else:
                print(player , ', dude, wall...')

        if health <= 0:
            print(player, 'died...')
            break

            

playGame()
        
