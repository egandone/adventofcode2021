from packet import create_packet

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
with open("input.txt") as input:
    lines = [line.strip().upper() for line in input.readlines()]

for line in lines:
    binary_string = "".join([hex2bin[c] for c in line])
    packet = create_packet(binary_string)
    print(f"{line} -> {packet.value()}")
