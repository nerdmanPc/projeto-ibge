import urllib3
import json

class IBGEQuery:
    def __init__(self) -> None:
        self._url = 'https://servicodados.ibge.gov.br/api/v3/agregados'

    def filter_subject(self, code):
        self._url += f'?assunto={code}'

    def select_aggregate(self, code):
        self._url += f'/{code}'

    def filter_location_levels(self, levels):
        level_ids = [f'N{level}' for level in levels]
        suffix = '|'.join(level_ids)
        self._url += f'/localidades/{suffix}'

    def filter_metadata(self):
        self._url += '/metadados'

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