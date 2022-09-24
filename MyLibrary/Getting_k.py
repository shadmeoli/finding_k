# math for mathimatical functions

import math
import setuptools
from functools import *

from rich import *

# entry point class
class GettValue:

    # main method
    def get_k_value(self, df) -> int:

        __step = 1

        __square_root_of_dataset = round(math.sqrt(df))

        try:

            if (__square_root_of_dataset%2) != 0:
                return __square_root_of_dataset

            elif (__square_root_of_dataset%2) == 0:
                __square_root_of_dataset = __square_root_of_dataset + __step
                return __square_root_of_dataset

        except Exception as e:
            return e
    

    def  __str__(self) -> str:
        return "[blue bold]The value of K has been successfully determined [/blue bold]"