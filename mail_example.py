from os import stat
from models.BuildStats import BuildStats
from models.DataCapture import DataCapture


if __name__ == "__main__":
    d1 = DataCapture()
    d1.add(3)
    d1.add(3)
    d1.add(4)
    d1.add(6)
    d1.add(9)
    
    
    stats = d1.build_stats()

    less = stats.less(4)
    print(less)

    greather = stats.greater(4)
    print(greather)

    between = stats.between(3, 6)
    print(between)
    
