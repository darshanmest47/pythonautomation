import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")

class Mainclass:

    def setlogger(self):
        name=inspect.stack()[1][3]
        logger= logging.getLogger(name)
        filehandler=logging.FileHandler('files.log')
        formatter=logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel('DEBUG')
        return logger

