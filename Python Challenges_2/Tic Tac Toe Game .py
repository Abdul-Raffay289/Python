The_Board = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' ' ,}
Board_Keys = []
for key in The_Board:
    Board_Keys.append(key)
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-+')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-+')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-+')
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        print(The_Board)
        print("Its your turn "+ turn + "Move to which place?")
        move = input()
        if The_Board [move] ==' ':
            The_Board[move] = turn
            count+=1
        else:
            print("The place is already filled. \nMove to which place?")
            continue
        if count >= 5:
            if The_Board ['7'] == The_Board['8'] == The_Board['9'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['4'] == The_Board['5'] == The_Board['6'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['1'] == The_Board['2'] == The_Board['3'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['3'] == The_Board['6'] == The_Board['9'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['1'] == The_Board['4'] == The_Board['7'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['2'] == The_Board['5'] == The_Board['8'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['7'] == The_Board['5'] == The_Board['3'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
            elif The_Board ['1'] == The_Board['5'] == The_Board['9'] != '':
                printboard(The_Board)
                print("\nGame over.\n ")
                print("****" +turn+ "won. ****")
                break
        if count == 9:
            print("\nGame over.\n ")
            print("It's A tie")
        if turn == 'x':
            turn = '0'
        else:
            turn = 'X'
    restart = inpt("Do You want to play again? Yes Or No")
    if restart == Yes:
        for key in Board_Keys:
            The_Board[key] = ' '

        game()
        
if__name__ == "__main__":
game()