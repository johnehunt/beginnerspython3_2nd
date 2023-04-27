from enum import Enum, auto, unique, IntEnum


# Class syntax
class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


print(DaysOfWeek.MONDAY)
print(DaysOfWeek.TUESDAY)
print(DaysOfWeek.WEDNESDAY)

today = DaysOfWeek.THURSDAY
print(today)


class Compass(Enum):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270


print(Compass.SOUTH)

print(Compass.SOUTH.name)
print(Compass.SOUTH.value)

class Sizes(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"


print(Sizes.XL)


class SwitchPosition(Enum):
    ON = True
    OFF = False


switch = SwitchPosition.OFF
print(switch)

# Functional syntax
# Weekend = Enum('Weekend', ['SATURDAY', 'SUNDAY'])

Weekend = Enum('Weekend',
               ['SATURDAY', 'SUNDAY'],
               start=10)
day = Weekend.SATURDAY
print(day)

HTTPStatusCode = Enum(
        value="HTTPStatusCode",
        names=[
                ("OK", 200),
                ("CREATED", 201),
                ("BAD_REQUEST", 400),
                ("NOT_FOUND", 404),
                ("SERVER_ERROR", 500),
        ],
)

print(HTTPStatusCode.OK)


class Day(Enum):
    MONDAY = 5
    TUESDAY = auto()
    WEDNESDAY = 9
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = 15


print(list(Day))

class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"

print(OperatingSystem.UBUNTU)
print(OperatingSystem.DEBIAN)
print(OperatingSystem.MACOS)
print(OperatingSystem.WINDOWS)

# Can indicate that each value should be unique

@unique
class Lights(Enum):
    RED = 1
    AMBER = 2
    GREEN = 3
    # RED_AMBER = 1

print(Lights.RED)

for day in DaysOfWeek:
    print(day)

os1 = OperatingSystem.UBUNTU
os2 = OperatingSystem.MACOS
os3 = OperatingSystem.UBUNTU
print(os1 is os3)
print(os1 is os2)
print(os1 is not os2)

os4 = OperatingSystem.DEBIAN
print(os1 is os4)

class Size(IntEnum):
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5
    XXL = 6

print(Size.XS < Size.L)
print(Size.XL > Size.S)
print(Size.XL >= Size.S)