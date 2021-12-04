from bingo_board import BingoBoard

with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

moves = [int(move) for move in lines[0].split(",")]
boards = []
for board_position in range(1, len(lines), 6):
    boards.append(BingoBoard(lines[board_position + 1 : board_position + 6]))
print(f"moves = {lines[0]}")
board_listing = "\n\n".join([str(b) for b in boards])
print(f"{board_listing}")

bingo_board = None
for move in moves:
    print(f"calling {move}")
    for board in boards:
        board.mark(move)
        if board.bingo:
            bingo_board = board
            break
    if bingo_board:
        break

for board in boards:
    if board.bingo:
        print(f"{move} {board}")
        print(
            f"{move} * {board.get_unmarked_sum()} = {move * board.get_unmarked_sum()}"
        )


# for move in moves:
#     print(f"{move}")
#     for board in boards:
#         board.mark(move)
#     board_listing = "\n\n".join([str(b) for b in boards])
#     print(f"{board_listing}")
#     print("================================")
