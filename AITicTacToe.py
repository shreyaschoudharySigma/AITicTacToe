import random

def tryAI(b):
	
	for i in range(3):
		if b[i][0]=="O" and b[i][1]=="O" and b[i][2]==" ":
			return (i,2)
		if b[i][0]=="O" and b[i][1]==" " and b[i][2]=="O":
			return (i,1)
		if b[i][0]==" " and b[i][1]=="O" and b[i][2]=="O":
			return (i,0)
		if b[0][i]=="O" and b[1][i]=="O" and b[2][i]==" ":
			return (2,i)
		if b[0][i]=="O" and b[1][i]==" " and b[2][i]=="O":
			return (1,i)
		if b[0][i]==" " and b[1][i]=="O" and b[2][i]=="O":
			return (0,i)
	if b[0][0]=="O" and b[1][1]=="O" and b[2][2]==" ":
		return (2,2)
	if b[0][0]==" " and b[1][1]=="O" and b[2][2]=="O":
		return (0,0)
	if b[0][0]=="O" and b[1][1]==" " and b[2][2]=="O":
		return (1,1)	
	if b[2][0]=="O" and b[1][1]=="O" and b[0][2]==" ":
		return (0,2)
	if b[2][0]==" " and b[1][1]=="O" and b[0][2]=="O":
		return (2,0)
	if b[2][0]=="O" and b[1][1]==" " and b[0][2]=="O":
		return (1,1)
	for i in range(3):
		if b[i][0]=="X" and b[i][1]=="X" and b[i][2]==" ":
			return (i,2)
		if b[i][0]=="X" and b[i][1]==" " and b[i][2]=="X":
			return (i,1)
		if b[i][0]==" " and b[i][1]=="X" and b[i][2]=="X":
			return (i,0)
		if b[0][i]=="X" and b[1][i]=="X" and b[2][i]==" ":
			return (2,i)
		if b[0][i]=="X" and b[1][i]==" " and b[2][i]=="X":
			return (1,i)
		if b[0][i]==" " and b[1][i]=="X" and b[2][i]=="X":
			return (0,i)
	if b[0][0]=="X" and b[1][1]=="X" and b[2][2]==" ":
		return (2,2)
	if b[0][0]==" " and b[1][1]=="X" and b[2][2]=="X":
		return (0,0)
	if b[0][0]=="X" and b[1][1]==" " and b[2][2]=="X":
		return (1,1)	
	if b[2][0]=="X" and b[1][1]=="X" and b[0][2]==" ":
		return (0,2)
	if b[2][0]==" " and b[1][1]=="X" and b[0][2]=="X":
		return (2,0)
	if b[2][0]=="X" and b[1][1]==" " and b[0][2]=="X":
		return (1,1)
	if b[1][1]==" ": 
		return (1,1)
	if b[0][0] == " ":
		return (0,0) 
	if b[2][0] == " ":
		return (2,0) 
	if b[0][2] == " ":
		return (0,2) 
	if b[2][2] == " ":
		return (2,2) 
	while True:
		r = random.randint(0,2)
		c = random.randint(0,2)
		if b[r][c] == " ":
			return (r,c)
    
def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] != " ") or \
       (board[0][2] == board[1][1] == board[2][0] != " "):
        return board[1][1]
    return None

def play_game():
    print("--- WELCOME TO THE ARENA ---\n\n")
    name1 = input("Enter name for Player: ") or "Player X"
    players = {"X": name1, "O": 'AI'}
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"
    
    print(f"\n{players['X']} (X) vs {players['O']} (O)")
    print("Use positions 1-9 to play!")

    while True:
        print_board(board)
        current_name = players[current_symbol]
        
        try:
            if current_symbol == 'X':
            	choice = int(input(f"Choose (1-9): ")) - 1
            	row, col = divmod(choice, 3)
            if current_symbol == 'O':
            	print('AI is thinking ;)............')
            	tup = tryAI(board)
            	row = tup[0]
            	col = tup[1]
            	choice = 3*row + col
            	print(f"AI's choice: {choice+1}")
            
            if board[row][col] == " ":
                board[row][col] = current_symbol
            else:
                print("Spot already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        winner_symbol = check_winner(board)
        if winner_symbol:
            print_board(board)
            print(f"VICTORY! {players[winner_symbol]} wins the match!")
            break
            
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print(" It's a draw! Well played both.")
            break
            
        # Switch turns
        current_symbol = "O" if current_symbol == "X" else "X"
while True:
	if __name__ == "__main__":
		play_game()