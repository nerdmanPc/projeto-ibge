import urllib3
import json

class IBGEQuery:
    def __init__(self, http=None) -> None:
        if http is None:
            self.http = urllib3.PoolManager()
        else:
            self.http = http
        self.aggregates = '[all]'
        self.periods = '[all]'
        self.variables = '[all]'
        self.locales = '[all]'
        self.classifications = '[all]'

    def run():
        pass #TODO

def query_ibge(aggregate, variables, classification, periods, locales, http=None):
    query_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/{aggregate}/periodos/{periods}/variaveis/{variables}?localidades={locales}&classificacao={classification}'
    response = http.request('GET', query_url)
    if response.status != 200:
        print(f'ERRO: {response.status}')
        raise
    response_str = response.data.decode('utf-8')
    return json.loads(response_str)[0]['resultados']