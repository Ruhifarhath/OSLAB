print("Enter the number of frames: ",end="")
capacity = int(input())
print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))


def FIFO(s, capacity):
    f, fault, top = [], 0, 0
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            fault += 1
    print("\nFIFO Page Replacement:")
    print("Total requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" %(len(s), fault, (fault/len(s)*100)))


FIFO(s, capacity)
