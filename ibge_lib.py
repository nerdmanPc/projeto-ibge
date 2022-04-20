import urllib3
import json

class IBGEQuery:
    def __init__(self) -> None:
        self._url = 'https://servicodados.ibge.gov.br/api/v3/agregados'

    def select_subject(self, code):
        self._url += f'?assunto={code}'

    def select_aggregate(self, code):
        self._url += f'/{code}'

    def select_location_levels(self, levels):
        level_ids = [f'N{level}' for level in levels]
        suffix = '|'.join(level_ids)
        self._url += f'/localidades/{suffix}'

    def filter_metadata(self):
        self._url += '/metadados'

    def filter_periods(self):
        self._url += '/periodos'

    def select_periods(self, periods):
        self._url += f'/{periods}'

    def filter_variables(self):
        self._url += '/variaveis'

    def select_locations(self, locations):
        self._url += f'?localidades={locations}'

    def url(self):
        return self._url

def query_ibge(aggregate, variables, classification, periods, locales, http=None):
    query_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/{aggregate}/periodos/{periods}/variaveis/{variables}?localidades={locales}&classificacao={classification}'
    response = http.request('GET', query_url)
    if response.status != 200:
        print(f'ERRO: {response.status}')
        raise
    response_str = response.data.decode('utf-8')
    return json.loads(response_str)[0]['resultados']