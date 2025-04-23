from enum import Enum

class Criteria(int, Enum):
    max_dimension = 150
    max_volume= 1000000
    max_mass= 20

class Stacks(str, Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def validate_bulky(x: float, y: float, z: float) -> bool:
    bulky_dimensions = x > Criteria.max_dimension or y > Criteria.max_dimension or z > Criteria.max_dimension
    bulky_volume = (x*y*z) > Criteria.max_volume
    return bulky_dimensions and bulky_volume


def sort(width: float, height: float, length: float, mass: float) -> str:
    # Type validation
    assert isinstance(width, float), "Wrong width type"
    assert isinstance(height, float), "Wrong height type"
    assert isinstance(length, float), "Wrong length type"
    assert isinstance(mass, float), "Wrong mass type"


    is_heavy = mass > Criteria.max_mass
    is_bulky = validate_bulky(width, height, length)


    if is_heavy and is_bulky:
        return Stacks.REJECTED
    elif is_heavy or is_bulky:
        return Stacks.SPECIAL
    else:
        return Stacks.STANDARD


