from itertools import permutations
from typing import Any, List, Dict
from citys_map import City, CitysMap


class BruteForce:
    @classmethod
    def get_best_route(cls, citys_map: CitysMap, origin: City) -> Dict[str, Any]:
        citys_in_between: List[City] = list(citys_map.citys)
        citys_in_between.remove(origin)

        possible_midle_routes: List[List[City]] = [
            list(route) for route in list(permutations(citys_in_between))
        ]

        complete_routes: List[List[City]] = [
            [origin] + route + [origin] for route in possible_midle_routes
        ]

        result = cls._calc_best_route(complete_routes)
        result.update({"ammount_of_tests": len(complete_routes)})
        return result

    @classmethod
    def _calc_best_route(cls, possible_routes: List[List[City]]) -> Dict[str, Any]:
        calculated_routes: List[Dict] = []
        for route in possible_routes:
            value: int = 0
            for index in range(0, len(route) - 1):
                value += route[index].get_distance_to(route[index + 1])
            calculated_routes += [{"route": route, "value": value}]

        calculated_routes.sort(
            key=lambda calculated_route: calculated_route.get("value")
        )

        return calculated_routes[0]
