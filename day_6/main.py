from collections import deque
INPUT_FILE_PATH = "day_6/input.txt"


with open(INPUT_FILE_PATH) as f:
    pos = 0
    PACKET_SIZE = 4
    MESSAGE_SIZE = 14
    packet_search = deque()
    message_search = deque()
    # Fill packet search first
    while pos < PACKET_SIZE:
        next_char = f.read(1)
        packet_search.append(next_char)
        message_search.append(next_char)
        pos += 1
    # Then fill message search and begin checking packets. I know I don't need to but it feels wrong not to
    packet_pos = 0
    while pos < MESSAGE_SIZE:
        next_char = f.read(1)
        if not packet_pos:
            if len(set(packet_search)) == PACKET_SIZE:
                packet_pos = pos
            else:
                packet_search.append(next_char)
                packet_search.popleft()
        
        message_search.append(next_char)
        pos += 1
    
    # Then continue searching
    message_pos = 0
    while next_char := f.read(1):
        if not packet_pos:
            if len(set(packet_search)) == PACKET_SIZE:
                packet_pos = pos
            else:
                packet_search.append(next_char)
                packet_search.popleft()
        if not message_pos:
            if len(set(message_search)) == MESSAGE_SIZE:
                message_pos = pos
            else:
                message_search.append(next_char)
                message_search.popleft()
        if packet_pos and message_pos:
            break
        pos += 1        
    print(packet_pos)
    print(message_pos)

