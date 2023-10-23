import getset as gs

table = [[None, None, None],
         [None, None, None],
         [None, None, None]]

choice = {
    1: gs.set_top_left,
    2: gs.set_top_mid,
    3: gs.set_top_right,
    4: gs.set_mid_left,
    5: gs.set_mid_mid,
    6: gs.set_mid_right,
    7: gs.set_bottom_left,
    8: gs.set_bottom_mid,
    9: gs.set_bottom_right,
}

moves = []


def two_players():
    while True:

        gs.print_table(table)
        moves.append(gs.player_input(1, moves))
        choice[moves[len(moves)-1]](table, 1)

        if gs.win_check(1, table):
            break
        elif len(moves) == 9:
            print("\n-----DRAW-----")
            break

        print('\n')

        gs.print_table(table)
        moves.append(gs.player_input(2, moves))
        choice[moves[len(moves)-1]](table, 2)

        if gs.win_check(2, table):
            break

        print("\n********************\n")


def computer_easy():
    while True:

        gs.print_table(table)
        moves.append(gs.player_input(1, moves))
        choice[moves[len(moves) - 1]](table, 1)

        if gs.win_check(1, table):
            break
        elif len(moves) == 9:
            print("\n-----DRAW-----")
            break

        print('\n')

        gs.print_table(table)
        moves.append(gs.computer_easy_moves(moves))
        choice[moves[len(moves) - 1]](table, 2)

        if gs.win_check(2, table):
            print("***YOU LOSER***")
            break

        print("\n********************\n")


print("\n\n")

play = int(input("ENTER '1' for 2 player or 2 for CPU EASY: "))

while not(play in [1, 2]):
    play = int(input("ENTER '1' for 2 player or 2 for CPU EASY: "))

print("\n\n\n")

if play == 1:
    two_players()
elif play == 2:
    computer_easy()

gs.print_table(table)
