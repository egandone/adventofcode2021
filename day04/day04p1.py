from bingo_board import BingoBoard

with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

moves = [int(move) for move in lines[0].split(",")]
boards = []
for board_position in range(1, len(lines), 6):
    boards.append(BingoBoard(lines[board_position + 1 : board_position + 6]))
# print(f"moves = {lines[0]}")
# board_listing = "\n\n".join([str(b) for b in boards])
# print(f"{board_listing}")

# Create a reversed version of the moves list so we can use pop() to pull
# them off in sequence
moves = list(reversed(moves))
bingo_board = None
while not bingo_board and moves:
    move = moves.pop()
    print(f"calling {move}")
    for board in boards:
        board.mark(move)
        if board.bingo:
            bingo_board = board

if not bingo_board:
    raise ValueError("Ran out of moves before finding a winning board")
else:
    print(f"{move} {bingo_board}")
    print(
        f"{move} * {bingo_board.get_unmarked_sum()} = {move * bingo_board.get_unmarked_sum()}"
    )

# for move in moves:
#     print(f"{move}")
#     for board in boards:
#         board.mark(move)
#     board_listing = "\n\n".join([str(b) for b in boards])
#     print(f"{board_listing}")
#     print("================================")
