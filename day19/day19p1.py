import re
from scanner import Scanner
import numpy as np

def read_input(filename: str):
    scanners = []
    with open(filename) as input:
        while line := input.readline():
            line = line.strip()
            if line.startswith("--- scanner"):
                id = int(line[12:].split(" ")[0])
                scanner = Scanner(id)
                scanners.append(scanner)
            elif line:
                pt = tuple([int(n) for n in line.split(",")])
                scanner.add_point(pt)
    return scanners

def main():
    scanners = read_input("test_input.txt")
    for scanner in scanners:
        differentials = scanner.get_all_differentials()
        print(f"{scanner} has {len(differentials)} point differentials")

    d0 = scanners[0].get_all_differentials()
    d1 = scanners[1].get_all_differentials()
    overlap = d0.intersection(d1)
    print(len(overlap))

    d4 = scanners[4].get_all_differentials()
    overlap = d1.intersection(d4)
    print(len(overlap))
    
if __name__ == "__main__":
    main()
