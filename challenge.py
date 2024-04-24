from typing import NamedTuple
import sys

class Vector(NamedTuple):
    x: int
    y: int

    def __init(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

def get_directions() -> str:
    """
    Get the string of directions from file, or test cases.
    Returns: String of directions, alternating n num of numeric chars and 1 letter
    """
    return ""

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
            -1: Could not read file
            -2: Bad directions
    """
    directions: str = get_directions()
    vector_list: list = interpret_directions(directions)
    final_coordinate: Vector = calculate_final_coordinate(vector_list)
    final_distance: float = calculate_distance(final_coordinate)
    print(final_distance)
    return 0

if __name__ == '__main__':
    sys.exit(main())