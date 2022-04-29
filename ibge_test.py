import json
import unittest #import TestCase
#import urllib3
import json

from ibge_lib import *

class TestIBGEQueries(unittest.TestCase):
    def test_unfiltered_aggergate_query(self):
        self.assertEqual(aggregates_url(), 'https://servicodados.ibge.gov.br/api/v3/agregados')

    def test_filtered_aggregate_query(self):
        self.assertEqual(aggregates_url(subject=70), 'https://servicodados.ibge.gov.br/api/v3/agregados?assunto=70')

    def test_locations_per_aggregate_query(self):
        self.assertEqual(locations_url(aggregate=1705, levels=['N7', 'N6']), 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/localidades/N7|N6')

    def test_metadata_per_aggregate_query(self):
        self.assertEqual(metadata_url(aggregate=1705), 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/metadados')

    def test_periods_per_aggregate_query(self):
        self.assertEqual(periods_url(aggregate=1705), 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/periodos')

    def test_all_variables_query(self):
        self.assertEqual(all_variables_url(aggregate=1705), 'https://servicodados.ibge.gov.br/api/v3/agregados/1705/variaveis/all?localidades=BR')

    def test_specific_variables_query(self):
        query_url = specific_variables_url (aggregate=1712, locations=['BR'], variables=['214', '1982'], periods=['201701-201706', '201710'])
        self.assertEqual(query_url, 'https://servicodados.ibge.gov.br/api/v3/agregados/1712/periodos/201701-201706|201710/variaveis/214|1982?localidades=BR')

    def test_variables_query_with_classification(self):
        query_url = specific_variables_url(aggregate=1712, locations=['BR'], variables=['214', '1982'], classifications=['226[4844,96608,96609]', '218[4780]'])
        self.assertEqual(query_url, 'https://servicodados.ibge.gov.br/api/v3/agregados/1712/periodos/-6/variaveis/214|1982?localidades=BR&classificacao=226[4844,96608,96609]|218[4780]')

class TestIBGEResponses(unittest.TestCase):
    def setUp(self):
        with open('aggregates_response_test.json', 'rb') as file:
            self._aggregates = json.load(file)
        with open('variables_response_test.json', 'rb') as file:
            self._variables = json.load(file)
    
    def test_filter_research(self):
        researches_by_keyword = filter_researches(self._aggregates, 'cenoura')
        self.assertEqual(researches_by_keyword[0]['id'], 'P2')

    def test_filter_aggregate(self):
        aggregates_by_keyword = filter_aggregates(self._aggregates, 'melao')
        self.assertEqual(aggregates_by_keyword[0]['id'], 200)