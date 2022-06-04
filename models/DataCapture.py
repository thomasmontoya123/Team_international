from models.BuildStats import BuildStats


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
