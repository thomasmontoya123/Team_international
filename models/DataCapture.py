from pickle import TRUE
from models.BuildStats import BuildStats
from decorators.positive_validation import positive_validation
from decorators.type_validator import type_validation


class DataCapture:
    """Datacapture class
        The DataCapture object accepts numbers and returns an object for querying
        statistics about the inputs.
    """

    __slots__ = ["__elements"]

    def __init__(self) -> None:
        self.__elements = []

    @property
    def elements(self):
        """Getter

        Returns:
            list: elements in list
        """
        return self.__elements

    @type_validation([int], decorating_class=True)
    @positive_validation(decorating_class=True)
    def add(self, item: int):
        """adds one number to the element list

        Args:
            item (int):item to add
        """
        self.__elements.append(item)

    def __repr__(self) -> str:
        return str(self.__elements)

    def build_stats(self):
        """Create the stats instance

        Returns:
            BuildStats: instance to perform operations
        """
        return BuildStats(self)
