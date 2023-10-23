import random

liner = "-----------"

def print_table(table):
    print(" " + get_top_left(table) + " | " + get_top_mid(table) + " | " + get_top_right(table) + " ")
    print(liner)
    print(" " + get_mid_left(table) + " | " + get_mid_mid(table) + " | " + get_mid_right(table) + " ")
    print(liner)
    print(" " + get_bottom_left(table) + " | " + get_bottom_mid(table) + " | " + get_bottom_right(table) + " ")

def player_input(player, moves):
    while(True):
        move = int(input("\nPlayer " + str(player) + ": "))
        if not(move in {1,2,3,4,5,6,7,8,9}):
            print("***Invaled input! Please try again***")
        elif move in moves:
            print("***Move has already been done! Please try again***")
        else:
            break
    return move

def computer_easy_moves(moves):
    orgMoves = [1,2,3,4,5,6,7,8,9]
    computerMoves = [item for item in orgMoves if item not in moves]

    moveIndex = random.randrange(len(computerMoves))
    move = computerMoves[moveIndex]

    print("\nComputer easy: " + str(move))

    return move

def win_check(player, table):
    if ((table[0][0] == table[0][1] and table[0][1] == table[0][2] and not(None in table[0])) or
        (table[1][0] == table[1][1] and table[1][1] == table[1][2] and not(None in table[1])) or
        (table[2][0] == table[2][1] and table[2][1] == table[2][2] and not(None in table[2])) or
        (table[0][0] == table[1][0] and table[1][0] == table[2][0] and not(None in {table[0][0], table[1][0], table[2][0]})) or
        (table[0][1] == table[1][1] and table[1][1] == table[2][1] and not(None in {table[0][1], table[1][1], table[2][1]})) or
        (table[0][2] == table[1][2] and table[1][2] == table[2][2] and not(None in {table[0][2], table[1][2], table[2][2]})) or
        (table[0][0] == table[1][1] and table[1][1] == table[2][2] and not(None in {table[0][0], table[1][1], table[2][2]})) or
        (table[0][2] == table[1][1] and table[1][1] == table[2][0] and not(None in {table[0][2], table[1][1], table[2][0]}))):
        print("\n-----PLAYER " + str(player) + " WINS!-----")
        return True
    return False

def get_top_left(table):
    if table[0][0] == None:
        return ' '
    else:
        return table[0][0]

def get_top_mid(table):
    if table[0][1] == None:
        return ' '
    else:
        return table[0][1]

def get_top_right(table):
    if table[0][2] == None:
        return ' '
    else:
        return table[0][2]

def get_mid_left(table):
    if table[1][0] == None:
        return ' '
    else:
        return table[1][0]

def get_mid_mid(table):
    if table[1][1] == None:
        return ' '
    else:
        return table[1][1]

def get_mid_right(table):
    if table[1][2] == None:
        return ' '
    else:
        return table[1][2]

def get_bottom_left(table):
    if table[2][0] == None:
        return ' '
    else:
        return table[2][0]

def get_bottom_mid(table):
    if table[2][1] == None:
        return ' '
    else:
        return table[2][1]

def get_bottom_right(table):
    if table[2][2] == None:
        return ' '
    else:
        return table[2][2]

def set_top_left(table, player):
    if player == 1:
        table[0][0] = 'X'
    else:
        table[0][0] = 'O'
    return table

def set_top_mid(table, player):
    if player == 1:
        table[0][1] = 'X'
    else:
        table[0][1] = 'O'
    return table

def set_top_right(table, player):
    if player == 1:
        table[0][2] = 'X'
    else:
        table[0][2] = 'O'
    return table

def set_mid_left(table, player):
    if player == 1:
        table[1][0] = 'X'
    else:
        table[1][0] = 'O'
    return table

def set_mid_mid(table, player):
    if player == 1:
        table[1][1] = 'X'
    else:
        table[1][1] = 'O'
    return table

def set_mid_right(table, player):
    if player == 1:
        table[1][2] = 'X'
    else:
        table[1][2] = 'O'
    return table

def set_bottom_left(table, player):
    if player == 1:
        table[2][0] = 'X'
    else:
        table[2][0] = 'O'
    return table

def set_bottom_mid(table, player):
    if player == 1:
        table[2][1] = 'X'
    else:
        table[2][1] = 'O'
    return table

def set_bottom_right(table, player):
    if player == 1:
        table[2][2] = 'X'
    else:
        table[2][2] = 'O'
    return table