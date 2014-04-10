import sys
import math
import unittest
import numpy as num

from pyrocko import gf, util

r2d = 180. / math.pi
d2r = 1.0 / r2d
km = 1000.


def numeq(a, b, eps):
    return (num.all(num.asarray(a).shape == num.asarray(b).shape and
            num.abs(num.asarray(a) - num.asarray(b)) < eps))


class GFSourcesTestCase(unittest.TestCase):

    if sys.version_info < (2, 7):
        from contextlib import contextmanager

        @contextmanager
        def assertRaises(self, exc):

            gotit = False
            try:
                yield None
            except exc:
                gotit = True

            assert gotit, 'expected to get a %s exception' % exc

        def assertIsNone(self, value):
            assert value is None, 'expected None but got %s' % value

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_source_to_event(self):

        for S in [
                gf.Source,
                gf.SourceWithMagnitude,
                gf.ExplosionSource,
                gf.DCSource,
                gf.MTSource,
                gf.RingfaultSource,
                gf.PorePressurePointSource,
                gf.PorePressureLineSource]:

            s = S()
            ev = s.pyrocko_event()


if __name__ == '__main__':
    util.setup_logging('test_gf_sources', 'warning')
    unittest.main()