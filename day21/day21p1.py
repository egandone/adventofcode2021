from itertools import cycle

scores = [0, 0]
positions = [4, 3]

p = 0
rolls = 0
dice = cycle(range(1, 101))
winner = -1
while winner < 0:
    moves = (next(dice), next(dice), next(dice))
    rolls += 3
    positions[p] = (positions[p] - 1 + sum(moves)) % 10 + 1
    scores[p] += positions[p]
    if scores[p] >= 1000:
        winner = p

    print(
        f"player {p+1} rolls {moves} to end up at {positions[p]} score now {scores[p]}"
    )
    p = (p + 1) % 2

loser = (winner + 1) % 2
loser_score = scores[loser]
answer = scores[loser] * rolls
print(f"{loser_score} after {rolls} rolls -> {answer}")
