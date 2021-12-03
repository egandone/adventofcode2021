depth, horizontal = 0, 0
with open("input.txt") as input:
    for line in input.readlines():
        (dir, amount) = line.strip().split()
        print(f"{dir} -> {amount}")
        if dir == "up":
            depth -= int(amount)
        elif dir == "down":
            depth += int(amount)
        elif dir == "forward":
            horizontal += int(amount)
        else:
            raise ValueError(f"Unknown dir - {dir}")
print(f"depth = {depth}, horizontal = {horizontal}, product = {depth * horizontal}")
