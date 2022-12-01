
INPUT_FILE_PATH = "input.txt"

def snacks_per_elf(elf_file_path):
    # Just for fun, I'm going to pretend elves have tiny memory constrained computers
    # so I'll use this instead of split('\n\n') so that we only ever hold one elf's snacks in memory
    # at once
    elf_snacks = []
    with open(elf_file_path) as f:
        for line in f:
            line = line.strip()
            if line:
                # Line contains snack with calorie count
                elf_snacks.append(line)
            else:
                # Line is blank, end of this elf's snacks. Yield then reset
                yield elf_snacks
                elf_snacks = []

def calories_in_snacks(snack_list):
    return sum(int(snack) for snack in snack_list)

if __name__ == "__main__":
    total_calories_per_elf = sorted((calories_in_snacks(snack_list) for snack_list in snacks_per_elf(INPUT_FILE_PATH)), reverse=True)
    
    print("Most well stocked elf total: ", total_calories_per_elf[0])
    print("Total for top three most well stocked elves: ", sum(total_calories_per_elf[:3]))
