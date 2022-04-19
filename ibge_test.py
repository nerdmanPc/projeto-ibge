import json
import unittest #import TestCase
#import urllib3
import json

from ibge_lib import *

class TestIBGE(unittest.TestCase):
    def test_unfiltered_aggergate_query(self):
        query = IBGEQuery()
        assert query.url() == 'https://servicodados.ibge.gov.br/api/v3/agregados'

    def test_filtered_aggregate_query(self):
        query = IBGEQuery()
        query.filter_subject(70)
        assert query.url() == 'https://servicodados.ibge.gov.br/api/v3/agregados?assunto=70'

    def test_locations_per_aggregate_query(self):
        query = IBGEQuery()
        query.select_aggregate(1705)
        query.filter_location_levels([7, 6])
        assert query.url() == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/localidades/N7|N6'

    def test_aggregate_metadata_query(self):
        query = IBGEQuery()
        query.select_aggregate(1705)
        query.filter_metadata()
        assert query.url() == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/metadados'