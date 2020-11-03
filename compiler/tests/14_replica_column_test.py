#!/usr/bin/env python3
# See LICENSE for licensing information.
#
# Copyright (c) 2016-2019 Regents of the University of California 
# All rights reserved.
#
import unittest
from testutils import *
import sys, os
sys.path.append(os.getenv("OPENRAM_HOME"))
import globals
from globals import OPTS
from sram_factory import factory
import debug


class replica_column_test(openram_test):

    def runTest(self):
        config_file = "{}/tests/configs/config".format(os.getenv("OPENRAM_HOME"))
        globals.init_openram(config_file)

        debug.info(2, "Testing replica column for cell_6t")
        a = factory.create(module_type="replica_column", rows=4, rbl=[1, 0], replica_bit=1)
        self.local_check(a)

        debug.info(2, "Testing replica column for cell_1rw_1r")
        globals.setup_bitcell()
        a = factory.create(module_type="replica_column", rows=4, rbl=[1, 1], replica_bit=6)
        self.local_check(a)
        
        debug.info(2, "Testing replica column for cell_1rw_1r")
        globals.setup_bitcell()
        a = factory.create(module_type="replica_column", rows=4, rbl=[2, 0], replica_bit=2)
        self.local_check(a)
        
        globals.end_openram()

# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main(testRunner=debugTestRunner())
