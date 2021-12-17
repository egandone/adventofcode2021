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
        # 110100101111111000101000
        # VVVTTTAAAAABBBBBCCCCC
        #       ^
        p = 6
        num_str = ""
        while buffer[p] == "1":
            num_str = num_str + buffer[p + 1 : p + 5]
            p += 5
        num_str = num_str + buffer[p + 1 : p + 5]
        self._value = int(num_str, 2)
        p += 5
        # if round and (p % 4):
        #     p = ((p // 4) + 1) * 4
        return p


class Operator(Packet):
    def __init__(self, version: str, type: str, length_type: int):
        self.subpackets = []
        self.length_type = length_type
        super().__init__(version, int(type, 2))

    def version(self):
        return self._version + sum(p.version() for p in self.subpackets)

    def value(self):
        if self._type == 0:
            value = sum(p.value() for p in self.subpackets)
        elif self._type == 1:
            value = 0
            if self.subpackets:
                value = self.subpackets[0].value()
                for p in self.subpackets[1:]:
                    value *= p.value()
        elif self._type == 2:
            value = min([p.value() for p in self.subpackets])
        elif self._type == 3:
            value = max([p.value() for p in self.subpackets])
        elif self._type == 5:
            if len(self.subpackets) != 2:
                raise ValueError("operator 5 expecting exactly 2 subpackets")
            value = 1 if self.subpackets[0].value() > self.subpackets[1].value() else 0
        elif self._type == 6:
            if len(self.subpackets) != 2:
                raise ValueError("operator 6 expecting exactly 2 subpackets")
            value = 1 if self.subpackets[0].value() < self.subpackets[1].value() else 0
        elif self._type == 7:
            if len(self.subpackets) != 2:
                raise ValueError("operator 7 expecting exactly 2 subpackets")
            value = 1 if self.subpackets[0].value() == self.subpackets[1].value() else 0
        else:
            raise ValueError(f"unexpected operator - {self._type}")
        return value


class Operator0(Operator):
    def __init__(self, version: str, type: str):
        super().__init__(version, type, 0)

    def parse(self, buffer: str, round=False) -> int:
        p = 7
        length_str = buffer[p : p + 15]
        p += 15
        end_p = p + int(length_str, 2)
        while p < (end_p - 6):
            subpacket = _create_packet(buffer[p:])
            p += subpacket.parse(buffer[p:])
            self.subpackets.append(subpacket)
        p = end_p
        return p

    def __repr__(self):
        return (
            f"operator0({self._version}):["
            + ",".join([str(p) for p in self.subpackets])
            + "]"
        )


class Operator1(Operator):
    def __init__(self, version: str, type: str):
        super().__init__(version, type, 1)

    def parse(self, buffer: str) -> int:
        p = 7
        count_str = buffer[p : p + 11]
        p += 11
        count = int(count_str, 2)
        for i in range(count):
            subpacket = _create_packet(buffer[p:])
            p += subpacket.parse(buffer[p:])
            self.subpackets.append(subpacket)
        return p

    def __repr__(self):
        return (
            f"operator1({self._version}):["
            + ",".join([str(p) for p in self.subpackets])
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
