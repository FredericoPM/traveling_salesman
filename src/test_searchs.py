import random
import pytest
import os
from citys_map import CitysMap, City

from typing import Any, Dict, List
from brute_force import BruteForce
from a_star import AStar
from dynamic_search import DynamicSearch


def generate_input(
    ammount_of_inputs: int,
    min_number_of_citys: int,
    max_number_of_citys: int,
    randon_seed: int,
):
    random.seed(randon_seed)
    generated_inputs = []
    for index in range(ammount_of_inputs):
        number_of_citys = random.randint(min_number_of_citys, max_number_of_citys)
        cordenates = random.sample(range(1, number_of_citys * 10), number_of_citys * 2)
        citys = [
            f"{cordenates[city_index*2]},{(city_index+1)*2}"
            for city_index in range(number_of_citys)
        ]
        current_input = tuple([str(number_of_citys)] + citys)
        generated_inputs.append(current_input)

    return generated_inputs


@pytest.mark.parametrize("input", generate_input(5, 5, 10, 3))
def test_searchs(input: List[str]):
    if os.path.exists("./tests/"):
        os.mkdir(f"./tests/test_{hash(repr(input))}/")
    else:
        os.mkdir("./tests/")
        os.mkdir(f"./tests/test_{hash(repr(input))}/")

    test_path = f"./tests/test_{hash(repr(input))}"

    with open(f"{test_path}/input.txt", "w") as file:
        for line in input:
            file.write(line.strip() + "\n")

    citys_map: CitysMap = CitysMap(f"{test_path}/input.txt")
    citys: List[City] = list(citys_map.citys)
    origin: City = citys[0]

    brute_force_output: Dict[str, Any] = BruteForce.get_best_route(citys_map, origin)
    a_star_output: Dict[str, Any] = AStar.get_best_route(citys_map, origin)
    dynamic_search_output: Dict[str, Any] = DynamicSearch.get_best_route(
        citys_map, origin
    )

    save_output(brute_force_output, citys, f"{test_path}/brute_force_output.txt")
    save_output(a_star_output, citys, f"{test_path}/a_star_output.txt")
    save_output(dynamic_search_output, citys, f"{test_path}/dynamic_search_output.txt")
    save_comparasion(
        brute_force_output,
        a_star_output,
        dynamic_search_output,
        f"{test_path}/metrics.txt",
    )


def save_output(output: Dict[str, Any], citys: List[City], path):
    with open(path, "w") as file:
        file.write(f"{output.get('value')}\n")
        for city in output.get("route"):
            file.write(f"{citys.index(city)+1}\n")


def save_comparasion(
    brute_force_output: Dict[str, Any],
    a_star_output: Dict[str, Any],
    dynamic_search_output: Dict[str, Any],
    path: str,
):
    with open(path, "w") as file:
        file.write(f"Brute force:\n")
        file.write(
            f"\tammount of tests: {brute_force_output.get('ammount_of_tests')}\n"
        )
        file.write(f"\tvalue founded: {brute_force_output.get('value')}\n")
        file.write(f"A star:\n")
        file.write(f"\tammount of tests: {a_star_output.get('ammount_of_tests')}\n")
        file.write(f"\tvalue founded: {a_star_output.get('value')}\n")
        file.write(f"Dynamic search:\n")
        file.write(
            f"\tammount of tests: {dynamic_search_output.get('ammount_of_tests')}\n"
        )
        file.write(f"\tvalue founded: {dynamic_search_output.get('value')}\n")
