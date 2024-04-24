from typing import NamedTuple
import sys
import argparse
import math

DIRECTION_FILE: str = "Adventurer Path.md"

class Codes:
    SUCCESS: int = 0 
    NO_DIRECTIONS: int = -1
    BAD_DIRECTIONS: int = -2

class Vector(NamedTuple):
    x: int
    y: int

    def __init(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
    
    def __add__(self, other_vector):
        """
        Add two vectors together.
        """
        if isinstance(other_vector, Vector):
            return Vector(self.x + other_vector.x, self.y + other_vector.y)
    
    def magnitude(self):
        """
        Determines the magnitude of the vector.
        """
        return math.sqrt((self.x ** 2) + (self.y ** 2))

def get_directions() -> str:
    """
    Get the string of directions from file, or command line argument.
    Returns: String of directions, alternating n num of numeric chars and 1 letter
    """
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
    Get the string of directions from file.
    Returns: String of directions, alternating n num of numeric chars and 1 letter
    """
    directions: str = ''
    with open(DIRECTION_FILE, "r") as raw_direction_file:
        raw_direction_string: str = raw_direction_file.read()
        begin_directions_index = raw_direction_string.find("`") + 1
        end_directions_index = raw_direction_string.find("`", begin_directions_index)
        directions = raw_direction_string[begin_directions_index:end_directions_index]
    return directions

def interpret_directions(direction_string: str, vector_list: list) -> bool:
    """
    From a string of directions, return a list of Vectors.
    Parameters:
        direction_string:   Alternating n num of numeric chars and 1 letter
                            F = forward, B = backward, R = right, L = left
    Returns: 
    """
    good_directions: bool = True
    current_direction: str = ''
    vector_magnitude: int = 0
    for next_char in direction_string:
        if next_char.isnumeric():
            current_direction = current_direction + next_char
        else:
            if current_direction != '':
                vector_magnitude = int(current_direction)
            
                match next_char:
                    case 'F':
                        vector_list.append(Vector(0, vector_magnitude))
                    case 'B':
                        vector_list.append(Vector(0, vector_magnitude * -1))
                    case 'R':
                        vector_list.append(Vector(vector_magnitude, 0))
                    case 'L':
                        vector_list.append(Vector(vector_magnitude * -1, 0))
                    case _  :
                        good_directions = False
            else:
                # We received two letters in a row, which means we received a direction with no distance
                good_directions = False
            current_direction = ''

    return good_directions

def calculate_final_coordinate(vector_list: list) -> Vector:
    """
    Calculate the final coordinate from the list of directions.
    Parameters:
        vector_list:    A list of Vectors
    Returns: A Vector containing the final coordinate
    """
    final_vector: Vector = Vector(0, 0)
    for direction_vector in vector_list:
        final_vector = final_vector + direction_vector
    return final_vector

def calculate_distance(coordinate: Vector) -> float:
    """
    Calculate the final distance between the coordinate and the origin.
    Parameters:
        coordinate: the ending coordinate as a Vector
    Returns: The euclidian distance to the coordinate as a Vector
    """
    return coordinate.magnitude()

def main() -> int:
    """
    Interpret the directions and prints the Euclidian distance.
    Returns: error status
             0: Success
            -1: Could not get directions
            -2: Bad directions
    """
    return_status: int = Codes.SUCCESS
    
    directions: str = get_directions()
    if directions == '':
        return_status = Codes.NO_DIRECTIONS
        print("Could not read from file or test case.")
        return return_status

    vector_list: list = []
    good_directions: bool = interpret_directions(directions, vector_list)
    if not good_directions:
        return_status = Codes.BAD_DIRECTIONS
        print("Directions could not be interpreted.")
        return return_status
    
    final_coordinate: Vector = calculate_final_coordinate(vector_list)
    final_distance: float = calculate_distance(final_coordinate)
    print(final_distance)

    return return_status

if __name__ == '__main__':
    sys.exit(main())