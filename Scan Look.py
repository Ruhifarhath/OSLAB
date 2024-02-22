size = 8
disk_size = 200

def SCAN(arr, head, direction):
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(disk_size - 1)

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()
    run = 2

    while run != 0:
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
                direction = "right"
        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
                direction = "left"
        run -= 1

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is")
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

def LOOK(arr, head, direction1):
    seek_count = 0
    distance = 0
    cur_track = 0
    left = []
    right = []
    seek_sequence = []

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()
    run = 2

    while run:
        if direction1 == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
                direction1 = "right"
        elif direction1 == "right":
            for i in range(len(right)):
                cur_track = right[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
                direction1 = "left"
        run -= 1

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is")
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

arr = list(map(int, input().strip().split()))
head = 50
direction = "left"

print("SCAN disk Scheduling\n")
print("Initial position of head:", head)
SCAN(arr, head, direction)

direction1 = "right"
print("LOOK disk Scheduling\n")
print("Initial position of head:", head)
LOOK(arr, head, direction1)
