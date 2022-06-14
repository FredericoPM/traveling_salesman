from typing import Tuple, Dict, Any
from citys_map import City, CitysMap
from brute_force import BruteForce


class DynamicSearch(BruteForce):
    already_searched: Dict[Tuple, Dict] = {}

    @classmethod
    def get_best_route(cls, citys_map: CitysMap, origin: City) -> Dict[str, Any]:
        known_route: Dict[str, Any] = cls._get_already_searched_route(citys_map)
        if known_route:
            return known_route
        else:
            new_route: Dict[str, Any] = super().get_best_route(citys_map, origin)
            cls.already_searched.update(
                {cls._get_citys_formated_as_key(citys_map): new_route}
            )
            return new_route

    @classmethod
    def _get_already_searched_route(cls, citys_map: CitysMap) -> Dict[str, Any]:
        citys = cls._get_citys_formated_as_key(citys_map)
        return cls.already_searched.get(citys)

    @staticmethod
    def _get_citys_formated_as_key(citys_map: CitysMap) -> Tuple[City]:
        citys = list(citys_map.citys)
        citys.sort()
        return tuple(citys)
