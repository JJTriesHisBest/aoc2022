INPUT_FILE_PATH = "day_2/input.txt"

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

part1_permutations = {
    "A": {
        "X": ROCK_SCORE + DRAW_SCORE,
        "Y": PAPER_SCORE + WIN_SCORE,
        "Z": SCISSORS_SCORE + LOSS_SCORE,
    },
    "B": {
        "X": ROCK_SCORE + LOSS_SCORE,
        "Y": PAPER_SCORE + DRAW_SCORE,
        "Z": SCISSORS_SCORE + WIN_SCORE,
    },
    "C": {
        "X": ROCK_SCORE + WIN_SCORE,
        "Y": PAPER_SCORE + LOSS_SCORE,
        "Z": SCISSORS_SCORE + DRAW_SCORE,
    },
}

part2_permutations = {
    "A": {
        "X": LOSS_SCORE + SCISSORS_SCORE,
        "Y": DRAW_SCORE + ROCK_SCORE,
        "Z": WIN_SCORE + PAPER_SCORE,
    },
    "B": {
        "X": LOSS_SCORE + ROCK_SCORE,
        "Y": DRAW_SCORE + PAPER_SCORE,
        "Z": WIN_SCORE + SCISSORS_SCORE,
    },
    "C": {
        "X": LOSS_SCORE + PAPER_SCORE,
        "Y": DRAW_SCORE + SCISSORS_SCORE,
        "Z": WIN_SCORE + ROCK_SCORE,
    },
}

p1score = 0
p2score = 0
with open(INPUT_FILE_PATH) as games:
    for game in games:
        p1score += part1_permutations[game[0]][game[2]]
        p2score += part2_permutations[game[0]][game[2]]
print(p1score)
print(p2score)
