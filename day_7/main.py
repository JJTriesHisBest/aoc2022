from collections import defaultdict
INPUT_FILE_PATH = "day_7/input.txt"

hierarchy = dict()
breadcrumbs = ["/"]
sizes = {}
total = 0
def resolve_breadcrumbs(depth=0, dir=hierarchy):
    """Return dict for dir"""
    try:
        dir = dir.setdefault(breadcrumbs[depth], {})
    except IndexError:
        return dir
    else:
        depth += 1
        return resolve_breadcrumbs(depth=depth, dir=dir)
    
def add_file(size, name):
    cwd = resolve_breadcrumbs()
    global total
    total += size
    cwd[name] = size

with open(INPUT_FILE_PATH) as f:
    # Skip first line because its just going to root dir
    next(f)
    # Begin parsing lines
    for line in f:
        line = line.strip("$ ")
        parts = line.split()
        if parts[0] in ["ls", "dir"]:
            # We only need to know current dir and its size
            continue
        elif parts[0] == "cd":
            if parts[1] == "..":
                breadcrumbs.pop()
            else:
                breadcrumbs.append(parts[1])
        else:
            add_file(int(parts[0]), parts[1])

total_sizes = {}
def get_total_size(node, nodename):
    if isinstance(node, dict):
        total_size = sum([get_total_size(subnode, nodename + "/" + subnode_name) for subnode_name, subnode in node.items()])
        total_sizes[nodename] = total_size
        return total_size
    else:
        return node

# P1
get_total_size(hierarchy, "/")
print(sum(val for val in total_sizes.values() if val <= 100000))

# P2
sizes = sorted(total_sizes.values())
SPACE_NEEDED = 30000000
DISK_SPACE = 70000000
NEED_TO_FREE = DISK_SPACE - SPACE_NEEDED - total_sizes["/"]
print(next(size for size in sizes if size >= abs(NEED_TO_FREE)))