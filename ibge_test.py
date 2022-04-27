import json
import unittest #import TestCase
#import urllib3
import json

from ibge_lib import *

class TestIBGE(unittest.TestCase):
    def test_unfiltered_aggergate_query(self):
        assert aggregates_url() == 'https://servicodados.ibge.gov.br/api/v3/agregados'

    def test_filtered_aggregate_query(self):
        assert aggregates_url(subject=70) == 'https://servicodados.ibge.gov.br/api/v3/agregados?assunto=70'

    def test_locations_per_aggregate_query(self):
        assert locations_url(aggregate=1705, levels=['N7', 'N6']) == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/localidades/N7|N6'

    def test_metadata_per_aggregate_query(self):
        assert metadata_url(aggregate=1705) == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/metadados'

    def test_periods_per_aggregate_query(self):
        assert periods_url(aggregate=1705) == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/periodos'

    def test_variable_query(self):
        assert variables_url(aggregate=1705) == 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/periodos/-6/variaveis?localidades=BR'