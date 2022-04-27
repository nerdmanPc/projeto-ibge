import urllib3
import json

def query_ibge(aggregate, variables, classification, periods, locales, http=None):
    query_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/{aggregate}/periodos/{periods}/variaveis/{variables}?localidades={locales}&classificacao={classification}'
    response = http.request('GET', query_url)
    if response.status != 200:
        print(f'ERRO: {response.status}')
        raise
    response_str = response.data.decode('utf-8')
    return json.loads(response_str)[0]['resultados']

AGGR_URL = 'https://servicodados.ibge.gov.br/api/v3/agregados'

def aggregates_url(subject=None):
    if subject is None:
        return AGGR_URL
    else:
        return AGGR_URL + f'?assunto={subject}'

def locations_url(aggregate, levels):
    levels_str = '|'.join(levels)
    return AGGR_URL + f'/{aggregate}/localidades/{levels_str}'

def metadata_url(aggregate):
    return AGGR_URL + f'/{aggregate}/metadados'

def periods_url(aggregate):
    return AGGR_URL + f'/{aggregate}/periodos'

def variables_url(aggregate, periods='-6', locations='BR'):
    return AGGR_URL + f'/{aggregate}/periodos/{periods}/variaveis?localidades={locations}'