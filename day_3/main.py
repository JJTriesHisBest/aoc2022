INPUT_FILE_PATH = "day_3/input.txt"

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

def priority(letter):
    return letters.index(letter) + 1

def find_common(*containers):
    sets = [set(container) for container in containers]
    return set.intersection(*sets).pop()


priority_count = 0
badge_count = 0
with open(INPUT_FILE_PATH) as f:
    elf_group = []
    for line in f:
        line = line.strip()
        elf_group.append(line)
        halfway = len(line) // 2
        first_half = line[:halfway]
        second_half = line[halfway:]
        # For part 1, find common in halves
        common = find_common(first_half, second_half)
        priority_count += priority(common)
        # For part 2, find common in every batch of 3 lines
        if len(elf_group) % 3 == 0:
            badge_common = find_common(*elf_group)
            badge_count += priority(badge_common)
            elf_group.clear()
print(priority_count)
print(badge_count)


