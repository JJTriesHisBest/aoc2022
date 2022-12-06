import re

INPUT_FILE_PATH = "day_5/input.txt"


def crate_count(input_txt):
    crate_labels_re = re.compile(r"(\s*\d\s*)+")
    match = crate_labels_re.search(input_txt).group()
    return max(int(crate) for crate in match.split())

def create_initial_stacks(input_txt, count):
    stack_row_re = re.compile(r"(^\[.+$)", re.MULTILINE)
    matches =  stack_row_re.findall(input_txt)
    stacks = [[] for i in range(count)]
    while matches:
        row = matches.pop()
        crates = [row[i:i+4].strip() for i in range(0, len(row), 4)]
        for index, crate in enumerate(crates):
            if crate:
                stacks[index].append(crate.strip("[]"))
    return stacks

def parse_instructions(input_txt):
    instruction_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
    instructions = instruction_re.finditer(input_txt)
    return instructions

def execute_instruction_9000(instruction, stacks):
    count, fr, to = [int(n) for n in instruction.groups()]
    for i in range(count):
        stacks[to-1].append(stacks[fr-1].pop())

def execute_instruction_9001(instruction, stacks):
    count, fr, to = [int(n) for n in instruction.groups()]
    stacks[to-1] += stacks[fr-1][-count:]
    stacks[fr-1] = stacks[fr-1][:-count]    

with open(INPUT_FILE_PATH) as f:
    input_txt = f.read()
    stacks_9000 = create_initial_stacks(input_txt, crate_count(input_txt))
    stacks_9001 = create_initial_stacks(input_txt, crate_count(input_txt))
    instructions = parse_instructions(input_txt)
    for instruction in instructions:
        execute_instruction_9000(instruction, stacks_9000)
        execute_instruction_9001(instruction, stacks_9001)
    print(*[stack[-1] for stack in stacks_9000])
    print(*[stack[-1] for stack in stacks_9001])