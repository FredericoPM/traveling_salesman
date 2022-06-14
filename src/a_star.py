from typing import Any, List, Dict, Set
from citys_map import City, CitysMap


class AStar:
    ammount_of_tests = 0

    @classmethod
    def get_best_route(cls, citys_map: CitysMap, origin: City) -> Dict[str, Any]:
        possible_routes: List[Dict[str, Any]] = [{"route": [origin], "value": 0}]
        best_route: Dict[str, Any] = None
        current_best_route: Dict[str, Any] = min(
            possible_routes,
            key=lambda route: route.get("value") / len(route.get("route")),
        )
        while best_route != current_best_route:
            cls.ammount_of_tests += 1
            possible_routes.remove(current_best_route)

            next_possible_citys: List[List[City]] = cls._get_citys_option(
                citys_map.citys, current_best_route.get("route"), origin
            )
            new_routes: List[Dict[str, Any]] = [
                current_best_route.get("route") + [city] for city in next_possible_citys
            ]
            possible_routes += cls._calc_routes_value(new_routes)

            new_best_route: Dict[str, Any] = min(
                possible_routes,
                key=lambda route: route.get("value") / len(route.get("route")),
            )
            if (
                current_best_route.get("route")[-1] == origin
                and new_best_route.get("value") > current_best_route.get("value")
                and len(current_best_route.get("route")) == len(citys_map.citys) + 1
            ):
                best_route = current_best_route
            else:
                current_best_route = new_best_route

        best_route.update({"ammount_of_tests": cls.ammount_of_tests})
        return best_route

    @staticmethod
    def _get_citys_option(
        citys: Set[City], route: List[City], destiny: City
    ) -> List[City]:
        if len(citys) == len(route):
            return [destiny]
        else:
            return citys - set(route + [destiny])

    @classmethod
    def _calc_routes_value(cls, routes: List[List[City]]) -> Dict[str, Any]:
        calculated_routes: List[Dict] = []
        for route in routes:
            value: int = 0
            for index in range(0, len(route) - 1):
                value += route[index].get_distance_to(route[index + 1])
            calculated_routes += [{"route": route, "value": value}]

        return calculated_routes
