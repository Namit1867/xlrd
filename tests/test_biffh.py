import sys
import unittest

from xlrd import biffh

if sys.version_info[0] >= 3:
    from io import StringIO
else:
    # Python 2.6+ does have the io module, but io.StringIO is strict about
    # unicode, which won't work for our test.
    from StringIO import StringIO
