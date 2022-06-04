class BuildStats:

    def __init__(self, obj) -> None:
        self.elements = obj.elements

    def less(self, number: int) -> list:
        """get values in the datacapture element list less than the number

        Args:
            number (int): number to filter

        Returns:
            list: values in datacapture object less than number
        """
        return list(filter(lambda x: (x < number), self.elements))

    def greater(self, number: int) -> list:
        """get values in the datacapture element list greater than the number

        Args:
            number (int): number to filter

        Returns:
            list: values in datacapture object greater than number
        """
        return list(filter(lambda x: (x > number), self.elements))

    def between(self, start: int, end: int) -> list:
        """get values in the datacapture element list between start and end

        Args:
            start (int): number to start filter
            end (int): number to end filter

        Returns:
            list: values in datacapture object between start and end 
        """
        return list(filter(lambda x: (start <= x <= end), self.elements))
