aim, depth, horizontal = 0, 0, 0
with open("input.txt") as input:
    for line in input.readlines():
        (dir, amount) = line.strip().split()
        print(f"{dir} -> {amount}")
        if dir == "up":
            aim -= int(amount)
        elif dir == "down":
            aim += int(amount)
        elif dir == "forward":
            horizontal += int(amount)
            depth += aim * int(amount)
        else:
            raise ValueError(f"Unknown dir - {dir}")
print(f"depth = {depth}, horizontal = {horizontal}, product = {depth * horizontal}")
