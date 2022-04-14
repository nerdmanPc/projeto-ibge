import json
import unittest
import urllib3
import json

from ibge import *

class TestIBGE(unittest.TestCase):
    def should_return_all_aggregates():
        query = IBGEQuery()
        response = query.run()
        assert

    def should_return_specific_aggregate():
        pass
    def should_return_specific_periods():
        pass
    def should_return_specific_variables():
        pass
    def should_return_specific_locations():
        pass
    def should_return_specific_classifications():
        pass
    #def should_return_all_aggregate_codes():
    #    pass
    #def should_return_aggregate_codes_by_research():
    #    pass