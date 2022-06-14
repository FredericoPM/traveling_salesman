from dataclasses import dataclass
from typing import Set, Tuple
from math import sqrt


@dataclass
class City:
    coordinate: Tuple[int]

    def get_distance_to(self, other_city: object) -> int:
        return sqrt(
            pow(abs(self.coordinate[0] - other_city.coordinate[0]), 2)
            + pow(abs(self.coordinate[1] - other_city.coordinate[1]), 2)
        )

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, __o: object) -> bool:
        return self.coordinate == __o.coordinate

    def __lt__(self, __o: object) -> bool:
        return hash(repr(self)) < hash(repr(__o))


@dataclass
class CitysMap:
    def __init__(self, file_path: str) -> None:
        self._citys: Set(City) = set()
        with open(file_path, "r") as file:
            for line in list(file)[1:]:
                data = line.strip().split(",")
                self._citys.add(City(coordinate=(int(data[0]), int(data[1]))))

    @property
    def citys(self) -> Set[City]:
        return self._citys.copy()
