class Packet:
    def __init__(self, version: str, type: int):
        self._version = int(version, 2)
        self._type = type

    def version(self):
        return self._version


class LiteralValue(Packet):
    def __init__(self, version: str):
        self._value = None
        super().__init__(version, 4)

    def __repr__(self):
        return f"literal({self._version}):{self.value}"

    def value(self):
        return self._value

    def parse(self, buffer: str) -> int:
        # Skip the version and type fields (3 bits each)
        p = 6
        # Read each 5 bit chunk until the 
        # end packet (first bit is 0) is found
        num_str = ""
        while buffer[p] == "1":
            num_str = num_str + buffer[p + 1 : p + 5]
            p += 5
        # Read the end packet (another 5 bits)
        num_str = num_str + buffer[p + 1 : p + 5]
        p += 5
        # Convert the full binary string into a number
        self._value = int(num_str, 2)
        # Return how many bits were consumed.
        return p


class Operator(Packet):
    def __init__(self, version: str, type: str, length_type: int):
        self._subpackets = []
        self.length_type = length_type
        super().__init__(version, int(type, 2))

    def version(self):
        # For operator the version is my version plus the
        # sum of all the version of the subpackets 
        return self._version + sum(p.version() for p in self._subpackets)

    def value(self):
        values = [p.value() for p in self._subpackets]
        if self._type == 0:
            value = sum(values)
        elif self._type == 1:
            value = 0
            if values:
                value = values[0]
                for v in values[1:]:
                    value *= v
        elif self._type == 2:
            value = min(values)
        elif self._type == 3:
            value = max(values)
        elif self._type == 5:
            if len(values) != 2:
                raise ValueError("operator 5 expecting exactly 2 subpackets")
            value = 1 if values[0] > values[1] else 0
        elif self._type == 6:
            if len(values) != 2:
                raise ValueError("operator 6 expecting exactly 2 subpackets")
            value = 1 if values[0] < values[1] else 0
        elif self._type == 7:
            if len(values) != 2:
                raise ValueError("operator 7 expecting exactly 2 subpackets")
            value = 1 if values[0] == values[1] else 0
        else:
            raise ValueError(f"unexpected operator - {self._type}")
        return value


class Operator0(Operator):
    def __init__(self, version: str, type: str):
        super().__init__(version, type, 0)

    def parse(self, buffer: str, round=False) -> int:
        # Skip version, type and length marker (7 bits)
        p = 7
        # Parse the lenght (15 bits)
        length_str = buffer[p : p + 15]
        p += 15
        # Compute the final end offset
        end_p = p + int(length_str, 2)
        # As long as there are at lead 10 bits to process
        # we can process it.  The smallest valid packet is
        # a literal one with one value
        while p < (end_p - 10):
            # Create the subpacket based on the buffer
            subpacket = _create_packet(buffer[p:])
            # Parse the subpacket and update the offset
            p += subpacket.parse(buffer[p:])
            self._subpackets.append(subpacket)
        p = end_p
        return p

    def __repr__(self):
        return (
            f"operator0({self._version}):["
            + ",".join([str(p) for p in self._subpackets])
            + "]"
        )


class Operator1(Operator):
    def __init__(self, version: str, type: str):
        super().__init__(version, type, 1)

    def parse(self, buffer: str) -> int:
        # Skip version, type and length marker (7 bits)
        p = 7
        # Extract the 11 counter bits
        count_str = buffer[p : p + 11]
        p += 11
        count = int(count_str, 2)
        # Parse and add the specified number of packets
        for i in range(count):
            subpacket = _create_packet(buffer[p:])
            p += subpacket.parse(buffer[p:])
            self._subpackets.append(subpacket)
        return p

    def __repr__(self):
        return (
            f"operator1({self._version}):["
            + ",".join([str(p) for p in self._subpackets])
            + "]"
        )


def _create_packet(buffer: str) -> Packet:
    version = buffer[0:3]
    type = buffer[3:6]
    if type == "100":
        packet = LiteralValue(version)
    else:
        length_type = buffer[6]
        if length_type == "0":
            packet = Operator0(version, type)
        else:
            packet = Operator1(version, type)
    return packet


def create_packet(buffer: str) -> Packet:
    packet = _create_packet(buffer)
    packet.parse(buffer)
    return packet
