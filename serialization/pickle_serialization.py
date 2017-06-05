import pickle
from os.path import dirname, join

from serialization.serialization import Serializer


class PICKLESerializer(Serializer):
    """
        A pickle calculator serializer.

        Methods derived from Serializer class:

            add_bmr -- add BMR entry to the object.
            add_bmi -- add BMI entry to the object.
            add_calories -- add daily rate entry to the object.

        Methods:
        dump -- dump the object to the binary file.
    """
    _filename = 'data.p'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path, 'rb')

    def s_load(self, f):
        """
        Wrap pickle loader function.
        :return: deserialized object
        """
        return pickle.load(f)

    def s_dump(self, f):
        """
        Wrap pickle dumper function.
        :return: None
        """
        pickle.dump(self._obj, f)

    def dump(self):
        """
        Serialize object to the binary file.
        """
        with open(self._path, 'wb') as f:
            self.s_dump(f)
