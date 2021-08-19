def current_beat():
    while True:
        for n in range(1,5):
            yield n

def current_beat2():
    num = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1