INPUT_FILE_PATH = "day_4/input.txt"

def sections(start, end):
    return set(range(int(start), int(end) + 1))

total_overlaps = 0
partial_overlaps = 0
with open(INPUT_FILE_PATH) as f:
    for line in f:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1_sections = sections(*elf1.split("-"))
        elf2_sections = sections(*elf2.split("-"))
        if elf1_sections <= elf2_sections or elf2_sections <= elf1_sections:
            total_overlaps += 1
        elif elf1_sections & elf2_sections:
            partial_overlaps += 1
print(total_overlaps)
print(partial_overlaps + total_overlaps)