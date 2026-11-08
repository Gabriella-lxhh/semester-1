# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.data = [float(line.strip()) for line in lines if line.strip()]

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)
    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]
    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        return sum(self.data) / len(self.data) if self.data else 0.0
    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        values = sorted(self.data)
        size = len(values)
        middle = size // 2
        if size % 2 == 1:
            return values[middle]
        else:
            return (values[middle - 1] + values[middle]) / 2.0