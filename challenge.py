from typing import NamedTuple
import sys
import argparse

DIRECTION_FILE: str = "Adventurer Path.md"

class Vector(NamedTuple):
    x: int
    y: int

    def __init(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

def get_directions() -> str:
    parser = argparse.ArgumentParser(description='Gets the adventurer directions and prints the euclidian distance from the destination')
    parser.add_argument('-t', '--test', type=str, default='', dest='test_string', help='Specify a test string to use instead of the default file.')
    args = parser.parse_args()

    if args.test_string == '':
        directions = get_directions_from_file()
    else:
        directions = args.test_string
    return directions

def get_directions_from_file() -> str:
    """
    Get the string of directions from file, or test cases.
    Returns: String of directions, alternating n num of numeric chars and 1 letter
    """
    directions: str = ''
    with open(DIRECTION_FILE, "r") as raw_direction_file:
        raw_direction_string: str = raw_direction_file.read()
        begin_directions_index = raw_direction_string.find("`") + 1
        end_directions_index = raw_direction_string.find("`", begin_directions_index)
        directions = raw_direction_string[begin_directions_index:end_directions_index]
    return directions

def interpret_directions(direction_string: str) -> list:
    """
    From a string of directions, return a list of Vectors.
    Parameters:
        direction_string:   Alternating n num of numeric chars and 1 letter
                            F = forward, B = backward, R = right, L = left
    Returns: A list of Vectors
    """
    return []

def calculate_final_coordinate(vector_list: list) -> Vector:
    """
    Calculate the final coordinate from the list of directions.
    Parameters:
        vector_list:    A list of Vectors
    Returns: A Vector containing the final coordinate
    """
    return Vector(0, 0)

def calculate_distance(coordinate: Vector) -> float:
    """
    Calculate the final distance between the coordinate and the origin.
    Parameters:
        coordinate: the ending coordinate as a Vector
    Returns: The euclidian distance to the coordinate as a Vector
    """
    return 0

def main() -> int:
    """
    Interpret the directions and prints the Euclidian distance.
    Returns: error status
             0: Success
            -1: Could not get directions
            -2: Bad directions
    """
    return_status: int = 0
    
    directions: str = get_directions()
    if directions == '':
        return_status = -1

    vector_list: list = interpret_directions(directions)
    final_coordinate: Vector = calculate_final_coordinate(vector_list)
    final_distance: float = calculate_distance(final_coordinate)
    print(final_distance)
    return return_status

if __name__ == '__main__':
    sys.exit(main())